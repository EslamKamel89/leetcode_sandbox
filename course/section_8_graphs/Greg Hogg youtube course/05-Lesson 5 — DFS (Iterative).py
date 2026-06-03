# graph = {
#     0: [1, 3],
#     1: [2],
#     2: [],
#     3: [],
# }
# graph = {
#     0: [1, 2],
#     1: [3],
#     2: [3],
#     3: [],
# }
graph = {
    0: [1, 2],
    1: [4],
    2: [3],
    3: [],
    4: [],
}
stack = [0]
visited = {0}
while stack:
    node = stack.pop()
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
