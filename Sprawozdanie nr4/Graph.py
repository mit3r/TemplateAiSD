import random
from typing import Optional
from hamiltonian_graph import HamiltonianGraph
from eulerian_graph import EulerianGraph
from graph_with_export import GraphWithExport


class MainGraph(HamiltonianGraph, EulerianGraph, GraphWithExport):
    def __init__(self, mode: Optional[str] = None, n: int = 5, saturation: int = 50):
        super().__init__(n)
        if mode == "h":
            self.create_hamilton_graph(n, saturation)
        elif mode == 'n':
            self.create_non_hamilton_graph(n, saturation)
        else:
            self.edges = [(i, (i + 1) % n) for i in range(n)]  # Sample default edges for testing
            for u, v in self.edges:
                self.add_edge(u, v)

    def create_hamilton_graph(self, n: int, saturation: int) -> None:
        """Creates a Hamiltonian graph with the specified saturation."""
        graph = self.create_hamiltonian_cycle()
        graph = self.add_edges_to_meet_saturation(graph, self.n, saturation)
        self.ensure_even_degree(graph, n)
        self.edges = graph
        for u, v in graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def create_non_hamilton_graph(self, n: int, saturation: int) -> None:
        """Creates a non-Hamiltonian graph with the specified saturation."""
        graph = self.add_edges_to_meet_saturation([], n, saturation)
        isolated_vertex = random.randint(0, n - 1)
        graph = [(u, v) for u, v in graph if u != isolated_vertex and v != isolated_vertex]
        self.edges = graph
        for u, v in graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def pretty_print_graph(self):
        """Utility function to pretty print the graph."""
        result = []
        for vertex in sorted(self.graph):
            connections = ', '.join(map(str, sorted(self.graph[vertex])))
            result.append(f"{vertex}: {connections}")
        return "\n".join(result)
