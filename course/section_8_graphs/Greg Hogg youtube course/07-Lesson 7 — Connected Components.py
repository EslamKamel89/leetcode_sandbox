# graph = {
#     0: [1],
#     1: [0, 2],
#     2: [1],
#     3: [4],
#     4: [3],
#     5: []
# }
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}
visited =set()

def dfs(node:int):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited :
            dfs(neighbor)
            
            
components = 0 


for node in graph :
    if node not in visited :
        print(f"Starting new component from {node}")
        dfs(node)
        components += 1
        
print("\nTotal Components:", components)