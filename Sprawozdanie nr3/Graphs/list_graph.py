from .graph import Graph
import math

class List_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []):
        super().__init__()

        self.succes_list = succes_list

    def __str__(self) -> str:
        s = ""
        width = int(math.log10(len(self.succes_list))) + 1
        for vert, succesors in enumerate(self.succes_list):
            s += f"{vert+1:>{width}}: {[succ+1 for succ in sorted(succesors)]}\n"

        return s

    def get_vertices(self) -> list[int]:
        return list(range(len(self.succes_list)))
    
    def get_edges(self) -> list[tuple[int, int]]:
        edges = []
        for vert, succesors in enumerate(self.succes_list):
            for succesor in succesors:
                edges.append((vert, succesor))
        return edges
    
    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        for succesor in self.succes_list[vertex1]:
            if succesor == vertex2:
                return True
        return False
    
    def resize_list(self, new_size: int) -> None:
        for x in range(new_size - len(self.succes_list)):
            self.succes_list.append([])

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        if vertex1 >= len(self.succes_list) or vertex2 >= len(self.succes_list):
            self.resize_list(max(vertex1, vertex2) + 1)
        
        self.succes_list[vertex1].append(vertex2)

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        self.succes_list[vertex1].remove(vertex2)
    
    def get_successors(self, vertex: int) -> list[int]:
        return self.succes_list[vertex]
    
    def get_predecessors(self, vertex: int) -> list[int]:
        predecessors = []
        for vert, succesors in enumerate(self.succes_list):
            for succesor in succesors:
                if succesor == vertex:
                    predecessors.append(vert)
        return predecessors