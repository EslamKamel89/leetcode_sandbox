graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4],
    4: [],
}


def dfs(node):
    print(f"Enter: {node}")
    for neighbor in graph[node]:
        dfs(neighbor)
    print(f"Leaving: {node}")


dfs(0)
