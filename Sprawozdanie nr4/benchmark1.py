
from Graph import MainGraph
import time
import os
from math import log2

try:
    os.mkdir("results", )
except FileExistsError:
    pass

# Wygeneruj grafy hamiltonowskie nieskierowane 
# dla różnych wartości n oraz dla nasycenia grafu 30

up_to = 14


start_from = 0
with open("results/hamilton_graph_find_ham.txt", "r") as file:
    for line in file:
        try:
            start_from = int(log2(int(line.split(";")[0])))
        except ValueError:
            pass

print(f"Starting from {start_from} to {up_to}...")

hamilton_graphs = []
for i in range(start_from+1, up_to+1):
    print(f"Creating graph {2**i}...")
    hamilton_graphs.append(MainGraph(mode='h', n=2**i, saturation=30))
print(f"{len(hamilton_graphs)} Graphs created.")

with open("results/hamilton_graph_find_ham.txt", "a") as file:
    if start_from == 0:
        file.write("Size, Saturation, Time\n")

    for graph in hamilton_graphs:
        start = time.time()
        graph.find_hamiltonian_cycle()
        end = time.time()

        print(f"Graph {graph.n} done.")

        file.write(f"{graph.n}; {30}; {end-start:.10f}\n")
print("Hamilton graphs find hamilton done.")


with open("results/hamilton_graph_find_eul.txt", "a") as file:
    if start_from == 0:
        file.write("Size, Saturation, Time\n")

    for graph in hamilton_graphs:
        start = time.time()
        graph.find_eulerian_cycle()
        end = time.time()

        print(f"Graph {graph.n} done.")

        file.write(f"{graph.n}; {30}; {end-start:.10f}\n")
print("Hamilton graphs find euler done.")




    


