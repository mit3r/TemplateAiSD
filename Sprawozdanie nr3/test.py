from Graphs import List_graph, Matrix_graph, Table_graph

l = list(range(0, 20+1))
l[0] = [2]
l[1] = [10, 6]
l[2] = [3, 1]
l[3] = [5]
l[4] = []
l[5] = [10, 7]
l[6] = [9, 4]
l[7] = [4]
l[8] = [7]
l[9] = [8]
l[10] = []
for i in range(10):
    l[11+i] = []


# how to start from 1 when indexing starts from 0
# for i in range(1, len(l)):
#     l[i-1] = [x-1 for x in l[i]]
# l.pop()
plus1 = lambda arr: [x+1 for x in arr]

reps = [Matrix_graph, List_graph, Table_graph]

# d = Matrix_graph(l)
# d = Table_graph(l)
d = List_graph(l)

print(d)

# for rep in reps:
#     g: Graph = rep(l)
#     print(rep)
#     print(g.breadth_first_search())
#     print(g.depth_first_search())
#     print(g.sort_Kahn())
#     print(g.sort_Tarjan())

