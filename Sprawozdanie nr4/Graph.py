import random
from collections import defaultdict

class Graph:
    def __init__(self, mode=None, n=5, saturation=50):
        self.graph = defaultdict(list)
        self.n = n
        self.edges = []
        if mode == "h":
            self.create_hamilton_graph(n, saturation)
        elif mode == 'n':
            self.create_non_hamilton_graph(n, saturation)
        else:
            self.edges = [(i, (i + 1) % n) for i in range(n)]  # Sample default edges for testing

    def create_hamiltonian_cycle(self, n):
        vertices = list(range(n))
        random.shuffle(vertices)
        cycle = [(vertices[i], vertices[(i + 1) % n]) for i in range(n)]
        return cycle

    def add_edges_to_meet_saturation(self, graph, n, saturation):
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

    def ensure_even_degree(self, graph, n):
        degree = [0] * n
        for u, v in graph:
            degree[u] += 1
            degree[v] += 1

        for i in range(n):
            if degree[i] % 2 != 0:
                for j in range(n):
                    if i != j and (i, j) not in graph and (j, i) not in graph:
                        graph.append((i, j))
                        degree[i] += 1
                        degree[j] += 1
                        break

    def create_hamilton_graph(self, n, saturation):
        graph = self.create_hamiltonian_cycle(n)
        graph = self.add_edges_to_meet_saturation(graph, n, saturation)
        self.ensure_even_degree(graph, n)
        self.edges = graph
        for u, v in graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def create_non_hamilton_graph(self, n, saturation):
        graph = self.add_edges_to_meet_saturation([], n, saturation)
        isolated_vertex = random.randint(0, n - 1)
        graph = [(u, v) for u, v in graph if u != isolated_vertex and v != isolated_vertex]
        self.edges = graph
        for u, v in graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def export_to_latex(self):
        output = (
            """\\documentclass{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes,positioning}\n\\begin{document}\n\\begin{tikzpicture}[every node/.style={circle,draw,minimum size=10mm, font=\\Large, inner sep=1mm, text=white, fill=red}, thick,>=stealth, line width=3.5pt,shorten >=5pt]\n"""
        )
        angle_step = 360 / self.n

        for i in range(self.n):
            angle = i * angle_step
            output += f"\\node (v{i}) at ({angle}:6cm) {{{i}}};\n"

        for u, v in self.edges:
            output += f"\\draw (v{u}) -- (v{v});\n"

        output += "\\end{tikzpicture}\n\\end{document}"
        return output

    def depth_first_search(self) -> list[int]:
        explored = []

        def DFS(v, visited):
            if visited[v]:
                return

            visited[v] = True
            explored.append(v)
            for succesor in sorted(self.get_successors(v)):
                try:
                    if not visited[succesor]:
                        DFS(succesor, visited)
                except:
                    pass
        visited = [False] * len(self.get_vertices())
        for vert in sorted(self.get_vertices()):
            DFS(vert, visited)

        return explored

    def find_eulerian_cycle(self):
        start_vertex = next((i for i in range(self.n) if self.graph[i]), None)
        if start_vertex is None:
            return None
        result = self.depth_first_search()

        if len(result) != len(self.get_vertices()):
            return None

        return result[::-1]

    def get_vertices(self) -> list[int]:
        return list(range(len(self.graph)))

    def get_edges(self) -> list[tuple[int, int]]:
        edges = []
        for vert, succesors in enumerate(self.graph):
            for succesor in succesors:
                edges.append((vert, succesor))
        return edges

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        for succesor in self.graph[vertex1]:
            if succesor == vertex2:
                return True
        return False

    def get_successors(self, vertex: int) -> list[int]:
        return self.graph[vertex]

    def find_hamiltonian_cycle(self):
        path = [-1] * self.n
        path[0] = 0

        def is_safe(v, pos):
            if v not in self.graph[path[pos - 1]]:
                return False
            if v in path:
                return False
            return True

        def ham_cycle_util(pos):
            if pos == self.n:
                if path[0] in self.graph[path[pos - 1]]:
                    return True
                else:
                    return False

            for v in range(1, self.n):
                if is_safe(v, pos):
                    path[pos] = v
                    if ham_cycle_util(pos + 1):
                        return True
                    path[pos] = -1

            return False

        if ham_cycle_util(1):
            return path + [path[0]]  # Returning the cycle including the return to the start vertex
        else:
            return None

# Example usage
