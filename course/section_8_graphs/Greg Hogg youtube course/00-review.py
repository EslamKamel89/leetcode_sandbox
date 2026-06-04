from collections import deque

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: [],
}

queue = deque([0])
visited = {0}
level = 0 
while queue :
    print(f"\nLEVEL {level}")
    for _ in range(len(queue)) :
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited :
                visited.add(neighbor)
                queue.append(neighbor)
    level += 1 
