from collections import defaultdict

edges = [
    [0, 1],
    [0, 3],
    [1, 2],
    [3, 4],
    [3, 6],
    [3, 7],
]

graph = defaultdict(list)

for start, end in edges:
    graph[start].append(end)

print("Adjacency List: ")
for node in graph:
    print(node, "->", graph[node])
