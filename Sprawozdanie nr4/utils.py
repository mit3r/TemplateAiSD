def pretty_print_graph(edge_list):
    from collections import defaultdict

    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # Because the graph is undirected

    result = []
    for vertex in sorted(adjacency_list):
        connections = ', '.join(map(str, sorted(adjacency_list[vertex])))
        result.append(f"{vertex}: {connections}")

    return "\n".join(result)