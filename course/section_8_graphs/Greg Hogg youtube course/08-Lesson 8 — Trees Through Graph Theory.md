# Lesson 8 — Trees Through Graph Theory

## Lesson Goal

Up until now, we've been treating:

```txt
Trees
```

and

```txt
Graphs
```

as different topics.

This lesson changes that.

The biggest conceptual shift is:

```txt
Tree
=
Special Graph
```

Everything you've learned about DFS, BFS, traversal, visited sets, and connected components now helps explain what a tree actually is.

---

# Part 1 — A New Definition of Tree

When most people think about trees, they think:

```txt
        A
       / \
      B   C
     /
    D
```

But graph theory defines a tree differently.

A tree is:

```txt
Connected
+
Acyclic
```

Let's understand both pieces.

---

# Part 2 — Connected

A graph is connected if:

```txt
Every node can reach every other node.
```

---

Example:

```txt
0 -- 1 -- 2
     |
     3
```

Can 0 reach 2?

```txt
0 → 1 → 2
```

Yes.

---

Can 3 reach 0?

```txt
3 → 1 → 0
```

Yes.

---

Every node can reach every other node.

Therefore:

```txt
Connected
```

---

Now consider:

```txt
0 -- 1

2 -- 3
```

Can 0 reach 3?

No.

Therefore:

```txt
Disconnected
```

---

# Part 3 — Cycles

Recall Lesson 4.

A cycle means:

```txt
A → B → C → A
```

You can leave a node and eventually come back.

---

Example:

```txt
0 -- 1
|    |
|    |
3 -- 2
```

Start at 0:

```txt
0 → 1 → 2 → 3 → 0
```

You returned to the start.

This graph contains a cycle.

---

Therefore:

```txt
Not a tree
```

---

# Part 4 — Tree Definition Revisited

A graph is a tree if:

### Condition 1

```txt
Connected
```

Every node reachable.

AND

### Condition 2

```txt
Acyclic
```

No cycles.

---

Both are required.

---

# Example 1 — Valid Tree

```txt
0
|
1
|
2
|
3
```

Connected?

```txt
Yes
```

Cycle?

```txt
No
```

Result:

```txt
Tree
```

---

# Example 2 — Cycle

```txt
0 -- 1
|    |
|    |
3 -- 2
```

Connected?

```txt
Yes
```

Cycle?

```txt
Yes
```

Result:

```txt
Not a Tree
```

---

# Example 3 — Disconnected

```txt
0 -- 1

2 -- 3
```

Connected?

```txt
No
```

Cycle?

```txt
No
```

Result:

```txt
Not a Tree
```

---

# Part 5 — The Most Important Tree Property

This comes directly from the graph lesson transcript.

If a graph is a tree:

```txt
Edges = Nodes - 1
```

or:

```txt
E = V - 1
```

---

# Why?

Suppose:

```txt
4 nodes
```

A tree might be:

```txt
0 -- 1 -- 2 -- 3
```

Count:

```txt
Nodes = 4
Edges = 3
```

---

Now add one edge:

```txt
0 -- 1
|    |
|    |
3 -- 2
```

Now:

```txt
Nodes = 4
Edges = 4
```

A cycle appeared.

---

If you remove too many edges:

```txt
0 -- 1

2 -- 3
```

Now:

```txt
Nodes = 4
Edges = 2
```

Graph becomes disconnected.

---

This leads to a remarkable fact:

For an undirected graph:

```txt
Connected
+
Edges = Nodes - 1
```

implies:

```txt
Tree
```

---

# Interview Insight

This fact appears directly in:

Graph Valid Tree

Many solutions are built around:

```txt
1. Check edge count
2. Check connectivity
```

---

# Part 6 — Classifying Graphs Mentally

Whenever you see a graph, ask:

### Question 1

```txt
Is it connected?
```

---

### Question 2

```txt
Does it contain a cycle?
```

---

Decision table:

| Connected | Cycle | Result   |
| --------- | ----- | -------- |
| Yes       | No    | Tree     |
| Yes       | Yes   | Not Tree |
| No        | No    | Not Tree |
| No        | Yes   | Not Tree |

---

Notice:

```txt
Only one row produces a tree.
```

---

# Python Lab

Run this code.

```python
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
```

---

## What This Lab Teaches

This is NOT a complete tree check.

It only demonstrates:

```txt
E = V - 1
```

which is a necessary property.

Later, when we study cycle detection, we'll see how to verify the full definition.

---

# Visual Classification Exercise

Classify each graph.

---

## Graph A

```txt
0
|
1
|
2
|
3
```

Connected?

Cycle?

Tree?

---

## Graph B

```txt
0 -- 1
|    |
|    |
3 -- 2
```

Connected?

Cycle?

Tree?

---

## Graph C

```txt
0 -- 1

2 -- 3
```

Connected?

Cycle?

Tree?

---

# Pattern Extraction

```txt
Need:
    Determine if graph is a tree

Pattern:
    Connectivity + Cycle Check

Structure:
    DFS/BFS + Graph Properties

Flow:
    Is graph connected?
    Does graph contain a cycle?
    If connected and acyclic:
        Tree
```

---

# Challenge

Without running code:

Graph:

```txt
0 -- 1
|
2
|
3
```

Questions:

1. Is the graph connected?
2. Does it contain a cycle?
3. Number of nodes?
4. Number of edges?
5. Is it a tree?
6. Which tree rule(s) prove your answer?

---

# Lesson 8 Completion Criteria

You should now be able to explain:

### What a tree really is

```txt
Connected
+
Acyclic
```

---

### Why cycles matter

A cycle means there are multiple paths between nodes, which violates the tree definition.

---

### Why connectivity matters

Every node must belong to the same connected component.

---

### The fundamental property

```txt
Edges = Nodes - 1
```

for every valid tree.

---

### Tree Recognition

Given a graph drawing, you should be able to determine:

```txt
Tree
or
Not Tree
```

without writing code.

---

Next comes **Lesson 9 — Cycle Detection**, where we'll learn how traversal can actively discover cycles and complete the core graph foundation curriculum.
