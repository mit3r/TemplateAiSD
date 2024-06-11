import sys
from Graph import MainGraph

if len(sys.argv) != 2:
    print("Usage: python main.py -hamilton | -nonhamilton")
    exit(1)

c = sys.argv[1]

match c:
    case '-hamilton' | '-h':
        n = int(input("nodes> "))
        saturation = int(input("saturation> "))
        graph = MainGraph(mode='h', n=n, saturation=saturation)
    case '-nonhamilton' | '-n':
        n = int(input("nodes> "))
        saturation = int(input("saturation> "))
        graph = MainGraph(mode='n', n=n, saturation=saturation)
    case _:
        print("There is no such option")
        exit(1)

print("Graph is created. Type 'help' to see available actions.")
print(graph)


def pretty_print_graph(graph):
    """Utility function to pretty print the graph."""
    for key in graph:
        print(f"{key}: {graph[key]}")


while True:
    action = input("action> ").strip().lower()

    match action:
        case 'help':
            print("Available actions:")
            print("  help - Show this help message")
            print("  print - Print the graph")
            print("  latex - Export graph to LaTeX")
            print("  euler - Find Eulerian cycle")
            print("  hamilton - Find Hamiltonian cycle")
            print("  exit - Exit the program")
        case 'print' | 'p':
            print(graph.pretty_print_graph())
        case 'latex' | 'l':
            latex_code = graph.export_to_latex()
            print(latex_code)
        case 'euler' | 'e':
            eulerian_cycle = graph.find_eulerian_cycle()
            print("Eulerian Cycle:", eulerian_cycle if eulerian_cycle else "No Eulerian cycle found")
        case 'hamilton' | 'h':
            hamiltonian_cycle = graph.find_hamiltonian_cycle()
            print("Hamiltonian Cycle:", hamiltonian_cycle if hamiltonian_cycle else "No Hamiltonian cycle found")
        case 'exit':
            print("Exiting the program.")
            break
        case _:
            print("Unknown action. Type 'help' for the list of available actions.")
