import sys
from typing import Union
from toolz import pipe

from inputs import collect_generated, collect_user_provided
from Graphs import List_graph, Matrix_graph, Table_graph
import actions

if len(sys.argv) != 2:
    print("Usage: python main.py -user-provided | -generate")
    exit(1)

c = sys.argv[1]

graph: Union[List_graph, Matrix_graph, Table_graph] | None = None
match c:
    case '-user-provided' | '-u':
        graph = collect_user_provided()
    case '-generate' | '-g':
        graph = collect_generated()

    case _:
        print("There is no such option")
        exit(1)

print("Graph is created. Type 'help' to see available actions.")
while True:

    try:
        action = pipe(
            input("action>"),
            lambda x: x.strip(),
            lambda x: x.lower()
        )
    except EOFError:
        exit(0)

    print()

    match action:
        case 'help':
            actions.ActionHelp()
        case 'print':
            actions.ActionPrint(graph)
        case 'exit':
            exit(0)
        case 'find':
            actions.ActionFind(graph)
        case 'bfs' | 'breath-first search':
            actions.ActionBFS(graph)
        case 'dfs' | 'depth-first search':
            actions.ActionDFS(graph)
        case 'kahn':
            actions.ActionKahn(graph)
        case 'tarjan':
            actions.ActionTarjan(graph)
        case 'export':
            actions.ActionExport(graph)
