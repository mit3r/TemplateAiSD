import os
import random


def generate_random_data(n):
    filename = f"benchmark_data/random/{2 ** n}_random_elements.txt"
    print(filename)
    arr = []
    with open(filename, "w", encoding='utf-8') as f:
        for i in range(2 ** n):
            num = random.randint(1, 2 ** n)
            while num in arr:
                num = random.randint(1, 2 ** n)
            arr.append(num)
            f.write(str(num) + "\n")

def generate_degenerated_trees_data(n):
    filename = f"benchmark_data/degenerated_trees/{2 ** n}_degenerated_tree_elements.txt"
    print(filename)
    with open(filename, "w",encoding='utf-8') as f:
        for i in range(2 ** n, 2**n//2, -1):
            f.write(str(i) + "\n")
            f.write(str(2**n - int(i)) + "\n")


def main():
    if not os.path.exists("benchmark_data"):
        os.mkdir("benchmark_data")
    if not os.path.exists("benchmark_data/random"):
        os.mkdir("benchmark_data/random")

    if not os.path.exists("benchmark_data/degenerated_trees"):
        os.mkdir("benchmark_data/degenerated_trees")

    for i in range(1, 16):
        generate_random_data(i)
        generate_degenerated_trees_data(i)


if __name__ == '__main__':
    main()
