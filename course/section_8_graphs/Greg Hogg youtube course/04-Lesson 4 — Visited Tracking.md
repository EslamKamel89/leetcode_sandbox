# Lesson 4 — Visited Tracking

## Lesson Goal

This is the most important lesson in the entire graph foundation.

Not DFS.

Not BFS.

Not shortest path.

The idea that separates graph traversal from tree traversal is:

```txt
visited
```

In fact, your Graph section completion criteria explicitly requires understanding:

> Visited tracking and why it's critical.

---

# Part 1 — Why Trees Don't Need Visited

Consider a tree:

```txt
      A
     / \
    B   C
```

Starting at:

```txt
A
```

You go to:

```txt
B
```

Can B lead back to A?

In a tree traversal, not usually.

The structure naturally prevents loops.

---

Graphs are different.

---

# Part 2 — The Problem

Consider:

```txt
A → B
↑   ↓
└── C
```

or:

```txt
A → B → C → A
```

This is a cycle.

---

Suppose we run naive DFS:

```python
def dfs(node):
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)
```

---

Execution:

```txt
A
↓
B
↓
C
↓
A
↓
B
↓
C
↓
A
↓
...
```

Forever.

---

The graph never tells us:

```txt
Stop.
```

---

# Core Insight

Graphs can revisit places.

Trees generally cannot.

Therefore graphs need memory.

---

# Part 3 — What Is Visited?

We create a set:

```python
visited = set()
```

---

Mental model:

```txt
Visited Cities
```

Suppose we've already visited:

```txt
A
B
```

Then:

```python
visited = {"A", "B"}
```

---

Question:

```txt
Should we explore A again?
```

Answer:

```txt
No.
```

We already know everything reachable from A.

---

# Part 4 — The Critical Question

Every graph traversal repeatedly asks:

```txt
Have I been here before?
```

In code:

```python
if node in visited:
```

or

```python
if neighbor in visited:
```

---

This single check prevents:

```txt
Infinite loops
Duplicate work
Repeated traversal
```

---

# Part 5 — Why Mark BEFORE Traversing?

This is subtle but extremely important.

Many beginners do:

```python
dfs(neighbor)

visited.add(neighbor)
```

This is dangerous.

---

Consider:

```txt
0
|\
| \
1  2
 \/
  3
```

Graph:

```python
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
```

---

Suppose we start at:

```txt
0
```

---

Path 1:

```txt
0 → 1 → 3
```

---

Path 2:

```txt
0 → 2 → 3
```

---

If 3 is not marked immediately:

both paths may try to process:

```txt
3
```

independently.

---

Correct strategy:

```python
visited.add(neighbor)

dfs(neighbor)
```

Mark first.

Explore second.

---

# Mental Rule

Always think:

```txt
Reserve the node first.

Explore it second.
```

---

# Part 6 — Lab 1: DFS Without Visited

Run this.

```python
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

def dfs(node):
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs("A")
```

---

Before running:

Predict:

```txt
Will it terminate?
```

---

Expected result:

Eventually:

```txt
RecursionError
```

because:

```txt
A → B → C → A → B → C ...
```

never ends.

---

# Part 7 — Lab 2: DFS With Visited

Now run:

```python
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

visited = set()

def dfs(node):

    visited.add(node)

    print(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)

dfs("A")
```

---

Predict first.

---

Expected:

```txt
A
B
C
```

and then stop.

---

# Visual Trace

Start:

```python
visited = {}
```

---

Visit A:

```python
visited = {"A"}
```

---

Visit B:

```python
visited = {"A", "B"}
```

---

Visit C:

```python
visited = {"A", "B", "C"}
```

---

C sees:

```txt
A
```

again.

Question:

```python
if "A" not in visited
```

Result:

```python
False
```

Skip.

Traversal ends.

---

# Part 8 — The Universal Graph Pattern

Almost every graph problem eventually contains:

```python
visited = set()

def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)
```

You will see this pattern in:

- Number of Islands
- Clone Graph
- Graph Valid Tree
- Course Schedule
- Max Area of Island
- Flood Fill

and many others.

---

# Part 9 — Why Visited Is Mandatory

Without visited:

```txt
Cycles break traversal.
```

---

Without visited:

```txt
Same node may be processed many times.
```

---

Without visited:

```txt
Graph traversal loses efficiency.
```

---

With visited:

```txt
Each node is processed once.
```

which is why DFS and BFS achieve:

```txt
O(V + E)
```

instead of repeatedly exploring the same nodes.

---

# Challenge

Without running code:

```python
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

visited = set()

def dfs(node):

    visited.add(node)

    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

dfs(0)
```

Question:

1. What is printed?
2. At what moment does node `3` enter `visited`?
3. Why is node `3` printed only once?

---

# Lesson 4 Completion Criteria

You should now be able to explain:

### Why graphs need visited tracking

Because graphs can contain cycles and multiple paths to the same node.

---

### Why we mark before traversing

To prevent the same node from being scheduled multiple times.

---

### What visited represents

```txt
Nodes whose exploration has already been claimed.
```

Not merely:

```txt
Nodes we've looked at.
```

---

When you're comfortable with the challenge, we'll move to **Lesson 5 — Iterative DFS (Stack)**, where we'll replace recursion with an explicit stack and see that DFS is really a stack behavior, not a recursion behavior.
