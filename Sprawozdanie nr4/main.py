import sys
from Graph import Graph
from inputs import Action
from utils import pretty_print_graph
from Euler import Euler
if len(sys.argv) != 2:
    print("Usage: python main.py -hamilton | -nonhamilton")
    exit(1)

c = sys.argv[1]
Graph = Graph()
Euler = Euler()
match c:
    case '-hamilotn' | '-h':
        n = int(input("nodes> "))
        saturation = int(input("saturation> "))
        graph = Graph.create_hamilton_graph(n=n, saturation=saturation)
    case '-n' | '-n':
        n = int(input("nodes> "))
        saturation = int(input("saturation> "))
        graph = Graph.create_non_hamilton_graph(n=n, saturation=saturation)

    case _:
        print("There is no such option")
        exit(1)

print("Graph is created. Type 'help' to see available actions.")
print(graph)
# print(pretty_print_graph(graph.graph))
# print(Graph.find_euler_cycle(graph))
print(Graph.export_to_latex())
print(Graph.find_eulerian_cycle())
print(Graph.find_hamiltonian_cycle())

