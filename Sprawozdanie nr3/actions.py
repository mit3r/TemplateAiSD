from typing import Union
from Graphs import *


def input_digit(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt)) - 1
        except ValueError:
            print("Please, enter a digit")


def ActionHelp():
    print(
        "Available actions:\n"
        "print - prints the graph in a human-readable format\n"
        "help - prints this message\n"
        "exit - exits the program\n"
        "find - finds if the edge exists\n"
        "breath-first search / bfs - performs the BFS\n"
        "depth-first search / dfs - performs the DFS\n"
        "kahn - performs the Kahn's algorithm\n"
        "tarjan - performs the Tarjan's algorithm\n"
    )


def ActionPrint(graph: Union[List_graph, Matrix_graph, Table_graph]):
    print(graph)


def ActionFind(graph: Union[List_graph, Matrix_graph, Table_graph]):
    v1 = input_digit("{:>5}>".format("from"))
    v2 = input_digit("{:>5}>".format("to"))

    if graph.is_edge(v1, v2):
        print(f"True: edge ({v1 + 1},{v2 + 1}) exists in the graph")
    else:
        print(f"False: edge ({v1 + 1},{v2 + 1}) does not exist in the graph")


def ActionBFS(graph: Union[List_graph, Matrix_graph, Table_graph]):
    try:
        print("inline: ", *map(lambda x: x + 1, graph.breadth_first_search()))
    except Exception as e:
        print(e)


def ActionDFS(graph: Union[List_graph, Matrix_graph, Table_graph]):
    try:
        print("inline: ", *map(lambda x: x + 1, graph.depth_first_search()))
    except Exception as e:
        print(e)


def ActionKahn(graph: Union[List_graph, Matrix_graph, Table_graph]):
    try:
        print("sorted: ", *map(lambda x: x + 1, graph.sort_Kahn()))
    except Exception as e:
        print(e)


def ActionTarjan(graph: Union[List_graph, Matrix_graph, Table_graph]):
    try:
        print("sorted: ", *map(lambda x: x + 1, graph.sort_Tarjan()))
    except Exception as e:
        print(e)


def ActionExport(graph: Union[List_graph, Matrix_graph, Table_graph]):
    code = graph.export_to_latex()

    with open("exported_graph.tex", "w") as f:
        f.write(code)
    print(code)