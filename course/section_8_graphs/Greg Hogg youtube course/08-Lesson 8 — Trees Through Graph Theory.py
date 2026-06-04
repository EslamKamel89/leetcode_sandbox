examples = [
    ("Valid Tree", 4, 3),
    ("Cycle Graph", 4, 4),
    ("Disconnected Graph", 4, 2)
]

for name, nodes, edges in examples:

    print(f"\n{name}")

    print(f"Nodes: {nodes}")
    print(f"Edges: {edges}")

    if edges == nodes - 1:
        print("Tree candidate")
    else:
        print("Cannot be a tree")