import time
from AVL.AVLTree import AVL
from BST.BSTree import BST

from typing import Union

import os

# set max recursion depth
import sys
sys.setrecursionlimit(32768*16)
# set max stack size for this process
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

def init_measure_folder():
    try:
        os.mkdir("benchmark_results")
    except FileExistsError:
        pass

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def measure_time_of(label: str, dir: str, prepare: callable, function: callable, max_size: int = 0):
    filename = label.replace(" ", "_")
    filename = f"benchmark_results/{filename}_results.csv"

    if os.path.exists(filename):
        os.system(f"rm {filename}")

    os.system(f"touch \"{filename}\"")

    files = os.listdir(dir)
    files.sort(key=lambda x: int(x.split("_")[0]))

    result = [[] for i in range(0, max(map(lambda x: int(x.split("_")[0]), files)) + 1)]

    for file in files:
        src = open(f"{dir}/{file}", "r")

        tab = []
        x = int(file.split("_")[0])

        # if x > 5000:
        #     return result

        if max_size != 0 and x > max_size:
            return result

        for j in range(0, x):
            num = src.readline().strip()
            tab.append(num)

        for k in range(0, 4):
            
            print(f"{label}\t{file}\t{x}\t{k}")

            data: AVL = prepare(",".join(tab), x)

            start_time = time.time()

            with HiddenPrints():
                result[x].append(function(data))
            
            finish_time = time.time() - start_time
            with open(filename, "a") as dist:
                dist.write(f"{label}\t{file}\t{x}\t{finish_time:.10f}\n")  
            print(f"{finish_time:.10f}")

        
        tab.clear()
        src.close()
    
    return result


if __name__ == "__main__":
    init_measure_folder()

    # tworzenie drzewa AVL metodą połowienia binarnego,
    # tworzenie drzewa BST poprzez wstawianie kolejno elementów (drzewo zdegnerowane),
    # wyszukiwanie elementów o minimalnej
    # wyszukiwanie elementów o maksymalnej wartości,
    # wypisywanie wszystkich elementów drzewa (in-order),

    # równoważenia drzewa BST.

    randomAVLtrees: list[AVL] = []
    degeneratedAVLtrees: list[AVL] = []

    randomBSTtrees: list[BST] = []
    degeneratedBSTtrees: list[BST] = []


    def prepareRandomAVL(data, size: int = 0):
        return randomAVLtrees[size][0]
    
    def prepareRandomBST(data, size: int = 0):
        return randomBSTtrees[size][0]
    
    def prepareDegeneratedAVL(data, size: int = 0):
        return degeneratedAVLtrees[size][0]
    
    def prepareDegeneratedBST(data, size: int = 0):
        return degeneratedBSTtrees[size][0]
        

    randomAVLtrees = measure_time_of("creating AVL random", "benchmark_data/random", lambda x, s: x, AVL, 0)
    degeneratedAVLtrees = measure_time_of("creating AVL degenerated", "benchmark_data/degenerated_trees", lambda x, s: x, AVL, 0)

    randomBSTtrees = measure_time_of("creating BST random", "benchmark_data/random", lambda x, s: x, BST, 0)
    degeneratedBSTtrees = measure_time_of("creating BST degenerated", "benchmark_data/degenerated_trees", lambda x,s: x, BST, 16384*2)

    def search_for_min(tree: Union[AVL, BST]):
        tree.find_min(tree.root)
    
    def search_for_max(tree: Union[AVL, BST]):
        tree.find_max(tree.root)

    maks = 0
    measure_time_of("searching for min AVL random", "benchmark_data/random", prepareRandomAVL, search_for_min, 0)
    measure_time_of("searching for max AVL random", "benchmark_data/random", prepareRandomAVL, search_for_max, 0)
    measure_time_of("searching for min BST random", "benchmark_data/random", prepareRandomBST, search_for_min, 0)
    measure_time_of("searching for max BST random", "benchmark_data/random", prepareRandomBST, search_for_max, 0)

    def print_tree(tree: Union[AVL, BST]):
        print(*tree._get_in_order_tree(tree.root))

    maks = 16384*2
    measure_time_of("printing AVL random", "benchmark_data/random", prepareRandomAVL, print_tree, maks)
    measure_time_of("printing BST random", "benchmark_data/random", prepareRandomBST, print_tree, maks)
    measure_time_of("printing AVL degenerated ", "benchmark_data/degenerated_trees", prepareDegeneratedAVL, print_tree, maks)
    measure_time_of("printing BST degenerated", "benchmark_data/degenerated_trees", prepareDegeneratedBST, print_tree, 16384*2)


    measure_time_of("balancing BST degenerated", "benchmark_data/degenerated_trees", prepareDegeneratedBST, lambda x: x.balance(), 16384*2)
    measure_time_of("balancing BST random", "benchmark_data/random", prepareRandomBST, lambda x: x.balance(), maks)


