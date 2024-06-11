
from Graph import MainGraph
import time
import os
from math import log2

try:
    os.mkdir("results", )
except FileExistsError:
    pass


# Wygeneruj grafy nie-hamiltonowskie nieskierowane dla kilku 
# różnych wartości n (n jest małe, ok 20-30) oraz dla nasycenia grafu 50


start_from = 20
# try:
#     with open("results/nonhamilton_graph_find_ham.txt", "r") as file:
#         for line in file:
#             try:
#                 # size = int(log2(int(line.split(";")[0])))
#                 size = int(line.split(";")[0])

#                 if size > start_from:
#                     start_from = size
#             except ValueError:
#                 pass
# except FileNotFoundError:
#     pass

up_to = 30

sat = 50

print(f"Starting from {start_from} to {up_to}...")

nonhamilton_graphs = []
for i in range(start_from, up_to+1):
    print(f"Creating graph {i}...")
    nonhamilton_graphs.append(MainGraph(mode='n', n=i, saturation=sat))
print(f"{len(nonhamilton_graphs)} Graphs created.")

with open("results/nonhamilton_graph_find_ham.txt", "w+") as file:
    if start_from == 0:
        file.write("Size; Saturation; Time; Found;\n")

    for graph in nonhamilton_graphs:
        res = None
        start = time.time()
        res = graph.find_hamiltonian_cycle()
        end = time.time()

        print(f"Graph {graph.n} done.")

        file.write(f"{graph.n}; {sat}; {end-start:.10f}; ")
        file.write("yes;\n" if res is not None else "no;\n")
        
print("Non-Hamilton graphs find eulerian cycle done.")




    


