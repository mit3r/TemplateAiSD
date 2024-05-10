
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from inputs import collect_generated

graph = collect_generated('matrix', 20, 20)

m = np.array(graph.matrix)
G = nx.from_numpy_array(m, create_using=nx.DiGraph)

# Rysowanie grafu
pos = nx.spring_layout(G)  # Ustawienie pozycji wierzchołków
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrowsize=20)
plt.title("Directed Acyclic Graph (DAG)")
plt.show()

graph.sort_Kahn()
