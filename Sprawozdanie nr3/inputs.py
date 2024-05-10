from Graphs import List_graph, Matrix_graph, Table_graph

from typing import Union
from utils import input_digit, input_nodes, input_successors, input_type, matrix2succesors

import numpy as np
import networkx as nx
import random

import math

def collect_user_provided() -> Union[List_graph, Matrix_graph, Table_graph]:
    graph_type = input_type()
    graph_nodes = input_nodes()
    graph_successors = input_successors(graph_nodes)

    return {
        "list": List_graph,
        "matrix": Matrix_graph,
        "table": Table_graph
    }[graph_type](graph_successors)


def collect_generated(graph_type=None, graph_nodes=None, saturation=None) -> Union[List_graph, Matrix_graph, Table_graph]:

    if graph_type is None:
        graph_type = input_type()
    if graph_nodes is None:
        graph_nodes = input_nodes()

    while True and saturation == None:
        saturation = input_digit("saturation 0-100>")
        if saturation < 0 or saturation > 100:
            print("Please, enter a number between 0 and 100")
            saturation = None
        else:
            break

    saturation /= 100

    # Generacja grafu - W przypadku uruchomienia programu z argumentem ‘–generate‘. Wygeneruj
    # spójny skierowany graf acykliczny o nodes wierzchołkach oraz nasyceniu saturation. O wartości
    # nodes i saturation, zapytaj użytkownika, wyświetlając odpowiedni znak zachęty.
    # Najłatwiej jest utworzyć graf acykliczny skierowany poprzez wypełnienie odpowiednią liczbą jedynek
    # górnego trójkąta macierzy sąsiedztwa.

    m = [[0 for _ in range(graph_nodes)] for _ in range(graph_nodes)]

    # sum of edges in upper triangle (suma n początkowych wyrazów ciągu arytmetycznego)
    #  0  1  2  3  4
    #  5  6  7  8
    #  9 10 11
    # 12 13
    # 14

    all_edges = int((graph_nodes-1)*graph_nodes / 2)
    target_edges = math.ceil(saturation * all_edges)

    edges = list(range(int(all_edges)))
    random.shuffle(edges)

    edges = sorted(edges[:int(target_edges)])


    # fill upper triangle
    for i in range(graph_nodes+1):
        for j in range(i+1, graph_nodes):

            index = (graph_nodes - i + 2)*i // 2 + j - 1

            if index in edges:
                m[i][j] = 1
    
    return {
        "list": List_graph,
        "matrix": Matrix_graph,
        "table": Table_graph
    }[graph_type](matrix2succesors(m))

