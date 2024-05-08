import math

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
            for succesor in sorted(self.get_successors(v)):
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





