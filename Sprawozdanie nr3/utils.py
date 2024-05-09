from toolz import pipe

def input_digit(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt)) - 1
        except ValueError:
            print("Please, enter a digit")

def input_type() -> str:
    graph_type = input("{:>5}>".format("type"))

    if(graph_type not in ["list", "matrix", "table"]):
        print("Invalid input type. Please choose from list, matrix, table")
        exit(1)

    return graph_type

def input_nodes() -> int:
    graph_nodes = input("{:>5}>".format("nodes"))

    if(not graph_nodes.isdigit()):
        print("Invalid input. Please provide a number")
        exit(1)
    
    return int(graph_nodes)

def input_successors(n: int) -> list[list[int]]:

    graph_successors = [[] for _ in range(n)]

    for i in range(n):
        graph_successors[i] = pipe(
            input("{:>5}>".format(i+1)),
            lambda x: x.replace(",", " "),
            lambda x: x.split(),
            lambda l: [int(x)-1 for x in l if x.isdigit()]
        )

        for x in graph_successors[i]:
            if(x < 0 or x >= n):
                print(f"Invalid input. Successor is {x+1} but there are only {n} nodes.")
                exit(1)
    
    return graph_successors

def matrix2succesors(m: list[list[int]]) -> list[list[int]]:
    n = len(m)
    succ = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                succ[i].append(j)
    return succ