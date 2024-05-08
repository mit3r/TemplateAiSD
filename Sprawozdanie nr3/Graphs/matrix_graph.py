from .graph import Graph
import math

class Matrix_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []):
        super().__init__()

        self.matrix: list[list[bool]] = []

        for x in range(len(succes_list)):
            self.matrix.append([0] * len(succes_list))

        for vert, succesors in enumerate(succes_list):
            for succesor in succesors:
                self.matrix[vert][succesor] = True

    def __str__(self) -> str:
        s = "\n"
        width = len(self.matrix)
        num = int(math.log10(width)) + 1

        s += " "*num + " | " 
        s += " ".join([f"{x+1:>{num}} " for x in list(range(width))]) + "\n"

        s += "-"*(num+1) + "+"
        s += "-"*(width*(num+2)) + "\n"

        for i, row in enumerate(self.matrix):
            s += f"{i+1:>{num}} | "
            s += " ".join([f"{n:>{num}} " for n in row])
            s += "\n"
        
        return s

    def get_vertices(self) -> list[int]:
        return list(range(len(self.matrix)))
    
    def resize_matrix(self, new_size: int) -> None:
        for x in range(new_size - len(self.matrix)):
            self.matrix.append([0] * new_size)
    
    def get_edges(self) -> list[tuple[int, int]]:
        edges = []
        for begin in range(len(self.matrix)):
            for end in range(len(self.matrix)):
                if self.matrix[begin][end]:
                    edges.append((begin, end))
        return edges
    
    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        return self.matrix[vertex1][vertex2]
    
    def add_edge(self, vertex1: int, vertex2: int) -> None:
        if(vertex1 >= len(self.matrix) or vertex2 >= len(self.matrix)):
            self.resize_matrix(max(vertex1, vertex2) + 1)            

        self.matrix[vertex1][vertex2] = True

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        self.matrix[vertex1][vertex2] = False

    def get_successors(self, vertex: int) -> list[int]:
        return [i for i, x in enumerate(self.matrix[vertex]) if x]
    
    def get_predecessors(self, vertex: int) -> list[int]:
        return [i for i, x in enumerate(self.matrix) if x[vertex]]