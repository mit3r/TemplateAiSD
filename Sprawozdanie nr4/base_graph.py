from collections import defaultdict
from typing import List, Tuple

class BaseGraph:
    def __init__(self, n: int = 5):
        self.graph = defaultdict(list)
        self.n = n
        self.edges: List[Tuple[int, int]] = []

    def add_edge(self, u: int, v: int) -> None:
        """Adds an edge between two vertices."""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_vertices(self) -> List[int]:
        """Returns a list of vertices in the graph."""
        return list(self.graph.keys())

    def get_edges(self) -> List[Tuple[int, int]]:
        """Returns a list of edges in the graph."""
        return [(u, v) for u in self.graph for v in self.graph[u]]

    def get_successors(self, vertex: int) -> List[int]:
        """Returns a list of successors of a vertex."""
        return self.graph[vertex]

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        return vertex2 in self.graph[vertex1]
