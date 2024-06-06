from typing import List, Optional
from base_graph import BaseGraph

class EulerianGraph(BaseGraph):
    def find_eulerian_cycle(self) -> Optional[List[int]]:
        for i in self.graph:
            if len(self.graph[i]) % 2 != 0:
                return None

        graph_copy = {i: self.graph[i].copy() for i in self.graph}

        def DFS_Euler(v: int) -> None:
            while graph_copy[v]:
                u = graph_copy[v].pop()
                graph_copy[u].remove(v)
                DFS_Euler(u)
            euler_path.append(v)

        euler_path = []
        DFS_Euler(0)
        euler_path.pop()  # Remove the last redundant element
        return euler_path
