from Graphs import List_graph, Matrix_graph, Table_graph

from typing import Union
from toolz import pipe

import random

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

def collect_user_provided() -> Union[List_graph, Matrix_graph, Table_graph]:
    graph_type = input_type()
    graph_nodes = input_nodes()
    graph_successors = input_successors(graph_nodes)

    return {
        "list": List_graph,
        "matrix": Matrix_graph,
        "table": Table_graph
    }[graph_type](graph_successors)

def input_digit(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt)) - 1
        except ValueError:
            print("Please, enter a digit")

def collect_generated() -> Union[List_graph, Matrix_graph, Table_graph]:

    graph_type = input_type()
    graph_nodes = input_nodes()

    saturation = 0
    while True:
        saturation = input_digit("saturation 0-100>")
        if saturation < 0 or saturation > 100:
            print("Please, enter a number between 0 and 100")
        else:
            break

    # Generacja grafu - W przypadku uruchomienia programu z argumentem ‘–generate‘. Wygeneruj
    # spójny skierowany graf acykliczny o nodes wierzchołkach oraz nasyceniu saturation. O wartości
    # nodes i saturation, zapytaj użytkownika, wyświetlając odpowiedni znak zachęty.
    # Najłatwiej jest utworzyć graf acykliczny skierowany poprzez wypełnienie odpowiednią liczbą jedynek
    # górnego trójkąta macierzy sąsiedztwa.


    m = [[0 for _ in range(graph_nodes)] for _ in range(graph_nodes)]

    percent = int(100 / saturation)
    shift = random.randint(0, graph_nodes-1)

    for i in range(graph_nodes):
        for j in range(i+1, graph_nodes):
            # index of first in line
            fst = (graph_nodes*2 - i + 1) * i // 2
            index = fst+j-i # unique for each cell

            if((index+shift) % percent == 0):
                m[i][j] = 1
    
    succ_list = [[] for _ in range(graph_nodes)]
    for i in range(graph_nodes):
        for j in range(graph_nodes):
            if m[i][j] == 1:
                succ_list[i].append(j)

    return {
        "list": List_graph,
        "matrix": Matrix_graph,
        "table": Table_graph
    }[graph_type](succ_list)
    