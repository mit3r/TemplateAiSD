import time
from AVL.AVLTree import AVL
import os


def measure_time_of_creating_AVL():
    f1 = open("benchmark_results/results.txt", "a")
    files = os.listdir("benchmark_data/random")
    for i in files:
        tab = []
        f2 = open(f"benchmark_data/random/{i}", "r")
        x = int(f2.readline())
        for j in range(0, x):
            tab.append(int(f2.readline()))

        for k in range(0, 4):
            start_time = time.time()
            tree = AVL(",".join(tab))
            finish_time = time.time() - start_time
            finish_time = str(finish_time).replace(".", ",")
            f1.write(f"creating AVL\t{i}\t{x}\t{finish_time}\n")
        tab.clear()
