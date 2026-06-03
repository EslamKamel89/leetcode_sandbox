# graph = {
#     "A": ["B"],
#     "B": ["C"],
#     "C": ["A"],
# }
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [],
}
visited = set()


def dfs(node):
    print(f"Entering: {node}")
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
    print(f"Leaving: {node}")


# dfs("A")
dfs(0)
