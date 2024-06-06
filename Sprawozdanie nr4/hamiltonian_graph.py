import random
from typing import List, Optional
from base_graph import BaseGraph


class HamiltonianGraph(BaseGraph):
    def create_hamiltonian_cycle(self) -> List[tuple[int, int]]:
        """Creates a Hamiltonian cycle."""
        vertices = list(range(self.n))
        random.shuffle(vertices)
        return [(vertices[i], vertices[(i + 1) % self.n]) for i in range(self.n)]

    def add_edges_to_meet_saturation(self, graph: List[tuple[int, int]], n: int, saturation: int) -> List[
        tuple[int, int]]:
        """Adds edges to the graph to meet the saturation."""
        num_edges = int(saturation * n * (n - 1) / 200)
        existing_edges = set(graph)
        while len(existing_edges) < num_edges:
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v and (u, v) not in existing_edges and (v, u) not in existing_edges:
                graph.append((u, v))
                existing_edges.add((u, v))
                existing_edges.add((v, u))
        return graph

    def find_hamiltonian_cycle(self) -> Optional[List[int]]:
        """Finds a Hamiltonian cycle in the graph."""
        licznik = 0
        for i in self.graph:
            node = []
            if len(self.graph[i]) % 2 != 0:
                licznik += 1
                node.append(i)
        if licznik > 2:
            return None
        path = [-1] * self.n
        path[0] = 0

        def is_valid_vertex(v: int, pos: int) -> bool:
            if v not in self.graph[path[pos - 1]]:
                return False
            if v in path:
                return False
            return True

        def hamiltonian_cycle_util(pos: int) -> bool:
            """Utility function to find a Hamiltonian cycle."""
            if pos == self.n:
                return path[0] in self.graph[path[pos - 1]]
            for v in range(self.n):
                if is_valid_vertex(v, pos):
                    path[pos] = v
                    if hamiltonian_cycle_util(pos + 1):
                        return True
                    path[pos] = -1
            return False

        if hamiltonian_cycle_util(1):
            path.append(path[0])
            return path
        return None
