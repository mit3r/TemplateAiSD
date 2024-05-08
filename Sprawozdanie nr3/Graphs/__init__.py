import copy

class Graph:

    def get_vertices(self) -> list[int]:
        pass

    def get_edges(self) -> list[tuple[int, int]]:
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        pass

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        pass

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        pass

    def get_successors(self, vertex: int) -> list[int]:
        pass

    def get_predecessors(self, vertex: int) -> list[int]:
        pass

    def breadth_first_search(self) -> list[int]:

        visited = [False] * len(self.get_vertices())
        explored = []

        while not all(visited):
            stack = [min([i for i, x in enumerate(visited) if not x])]
            visited[stack[0]] = True
            
            explored.append(stack[0])

            while len(stack) > 0:
                v = stack.pop()

                for succesor in sorted(self.get_successors(v)):
                    if not visited[succesor]:
                        visited[succesor] = True
                        stack.append(succesor)

                        explored.append(succesor)
        
        return explored
    
    def depth_first_search(self) -> list[int]:
        explored = []

        def DFS(v, visited):
            if visited[v]:
                return
            
            visited[v] = True
            explored.append(v)
            for succesor in self.get_successors(v):
                if not visited[succesor]:
                    DFS(succesor, visited)
        
        visited = [False] * len(self.get_vertices())
        for vert in sorted(self.get_vertices()):
            DFS(vert, visited)
        
        return explored
        
    def sort_Kahn(self) -> list[int]:
        
        sorted_list = []
        removed = [False] * len(self.get_vertices())
        in_degree = [len(self.get_predecessors(v)) for v in self.get_vertices()]

        while not all(removed):
            v = None
            for i, degree in enumerate(in_degree):
                if degree == 0 and not removed[i]:
                    v = i
                    break
            else:
                return None

            removed[v] = True
            sorted_list.append(v)
            for succesor in self.get_successors(v):
                in_degree[succesor] -= 1
        
        return sorted_list
    
    def sort_Tarjan(self) -> list[int]:
        WHITE, GRAY, BLACK = 0, 1, 2

        colors = [WHITE] * len(self.get_vertices())
        explored = []
        
        def visit(v):
            colors[v] = GRAY

            while True:
                for succesor in self.get_successors(v):
                    if colors[succesor] == WHITE:
                        visit(succesor)
                        break
                else:
                    break

            colors[v] = BLACK
            explored.append(v)
        
        while not all([color == BLACK for color in colors]):

            for i in range(len(colors)):
                if colors[i] == WHITE:
                    visit(i)
                    break

        return explored[::-1]

class List_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []):
        super().__init__()

        self.succes_list = succes_list

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

class Matrix_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []):
        super().__init__()

        self.matrix: list[list[bool]] = []

        for x in range(len(succes_list)):
            self.matrix.append([0] * len(succes_list))

        for vert, succesors in enumerate(succes_list):
            for succesor in succesors:
                self.matrix[vert][succesor] = True

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

class Table_graph(Graph):

    def __init__(self, succes_list: list[list[int]] = []) -> None:
        super().__init__()

        self.vertecies: list[int] = []
        self.edges: list[tuple[int, int]] = []

        for vert, succesors in enumerate(succes_list):
            for succesor in succesors:
                self.add_edge(vert, succesor)
        
        self.vertecies = list(range(len(succes_list)))

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