# graph = {
#     0: [1, 3],
#     1: [0, 2],
#     2: [1, 3],
#     3: [0, 2]
# }
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}

visited = set()

def has_cycle(node, parent):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if has_cycle(neighbor, node):
                return True

        elif neighbor != parent:

            return True

    return False

print(has_cycle(0, -1))