from .graph import Graph
import math

class Table_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []) -> None:
        super().__init__()

        self.vertecies: list[int] = []
        self.edges: list[tuple[int, int]] = []

        for vert, succesors in enumerate(succes_list):
            for succesor in succesors:
                self.add_edge(vert, succesor)
        
        self.vertecies = list(range(len(succes_list)))

    def __str__(self) -> str:
        
        width = int(math.log10(len(self.vertecies))) + 1

        return "".join(
            [f"{begin+1:>{width}} -> {end+1:>{width}}\n" for begin, end in self.edges]
        )
        
    def get_vertices(self) -> list[int]:
        return self.vertecies
    
    def get_edges(self) -> list[tuple[int, int]]:
        return self.edges
    
    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        for v1, v2 in self.edges:
            if v1 == vertex1 and v2 == vertex2:
                return True
        return False
    
    def add_edge(self, vertex1: int, vertex2: int) -> None:
        self.edges.append((vertex1, vertex2))
        v1 = False
        v2 = False
        for vert in self.vertecies:
            if vert == vertex1:
                v1 = True
            if vert == vertex2:
                v2 = True

        if not v1:
            self.vertecies.append(vertex1)
        if not v2:
            self.vertecies.append(vertex2)

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        self.edges.remove((vertex1, vertex2))

    def get_successors(self, vertex: int) -> list[int]:
        succesors = []

        for v1, v2 in self.edges:
            if v1 == vertex:
                succesors.append(v2)
        
        return succesors
    
    def get_predecessors(self, vertex: int) -> list[int]:
        predecessors = []

        for v1, v2 in self.edges:
            if v2 == vertex:
                predecessors.append(v1)
        
        return predecessors