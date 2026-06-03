graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4, 5],
    4: [],
    5: [],
}

current = 0

print(f"Currently at :{current}")
print(f"Neighbors: {graph[current]}")

for neighbor in graph[current]:
    print("Can move to ", neighbor)
