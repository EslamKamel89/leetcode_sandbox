# Lesson 5 — DFS (Iterative)

## Lesson Goal

In Lesson 3, DFS looked like a recursion lesson.

But recursion is not actually the important part.

The important part is:

```txt
DFS = Stack Behavior
```

Recursion was simply hiding the stack from us.

This lesson reveals what was happening behind the scenes.

---

# Part 1 — What Recursion Was Secretly Doing

Recall:

```python
def dfs(node):

    for neighbor in graph[node]:
        dfs(neighbor)
```

When we call:

```python
dfs(0)
```

Python creates a call stack.

Example:

```txt
dfs(0)
  dfs(1)
    dfs(2)
```

Internally:

```txt
Top
-----
dfs(2)
dfs(1)
dfs(0)
-----
Bottom
```

This is literally a stack.

---

# Key Insight

Recursive DFS is actually:

```txt
DFS
+
Hidden Stack
```

Iterative DFS is:

```txt
DFS
+
Visible Stack
```

Same algorithm.

Different implementation.

---

# Part 2 — What Is a Stack?

A stack follows:

```txt
LIFO

Last In
First Out
```

Think of plates:

```txt
Put plate on top

Put plate on top

Put plate on top
```

To remove one:

```txt
Remove top plate first
```

You cannot remove the middle plate.

---

Python implementation:

```python
stack = []
```

Push:

```python
stack.append(x)
```

Pop:

```python
stack.pop()
```

---

# Mini Example

Run:

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())
print(stack.pop())
print(stack.pop())
```

Predict first.

Expected:

```txt
C
B
A
```

Because:

```txt
Last In
First Out
```

---

# Part 3 — DFS Without Graphs

Before using a graph, let's understand the mechanism.

Imagine:

```txt
Start at 0
```

We discover:

```txt
1
3
```

Instead of recursively calling:

```python
dfs(1)
```

we place work onto a stack.

---

State:

```python
stack = [0]
```

---

Process:

```python
node = stack.pop()
```

State:

```txt
Processing 0
```

---

Discover neighbors:

```txt
1
3
```

Add them:

```python
stack.append(1)
stack.append(3)
```

State:

```python
[1, 3]
```

---

Question:

Which gets processed next?

Answer:

```txt
3
```

Because:

```txt
Last In
First Out
```

---

This is exactly why iterative DFS goes deep.

---

# Part 4 — Visual DFS Simulation

Graph:

```txt
0
├── 1
│   └── 2
└── 3
```

Adjacency list:

```python
graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: []
}
```

---

Initial:

```python
stack = [0]
```

---

Process 0

Pop:

```txt
0
```

Push:

```txt
1
3
```

Stack:

```python
[1, 3]
```

---

Process next

Pop:

```txt
3
```

Stack:

```python
[1]
```

---

Process next

Pop:

```txt
1
```

Push:

```txt
2
```

Stack:

```python
[2]
```

---

Process next

Pop:

```txt
2
```

Stack:

```python
[]
```

Traversal complete.

---

Visited order:

```txt
0
3
1
2
```

Notice:

```txt
Different from recursive DFS.
```

But still DFS.

---

# Important Lesson

DFS does NOT guarantee one exact order.

DFS guarantees:

```txt
Depth-first behavior
```

The exact order depends on:

```txt
Neighbor order
Stack operations
Implementation details
```

---

# Part 5 — First Iterative DFS

Run:

```python
graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: []
}

stack = [0]

while stack:

    node = stack.pop()

    print(node)

    for neighbor in graph[node]:
        stack.append(neighbor)
```

---

Before running:

Predict:

```txt
Which node prints first?

Which node prints second?
```

---

Expected:

```txt
0
3
1
2
```

---

# Part 6 — Adding Visited

Real graph:

```txt
0
↙ ↘
1   2
 \ /
  3
```

Adjacency list:

```python
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
```

Without visited:

```txt
3
```

could be pushed multiple times.

---

Correct approach:

```python
visited = set()
```

---

# Full Iterative DFS

Run:

```python
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
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
```

---

Watch carefully:

```python
visited.add(neighbor)
```

happens before:

```python
stack.append(neighbor)
```

Same principle as recursive DFS.

Reserve first.

Explore later.

---

# Part 7 — Recursive DFS vs Iterative DFS

Recursive:

```python
def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)
```

---

Iterative:

```python
stack = [source]

while stack:

    node = stack.pop()

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)
            stack.append(neighbor)
```

---

Notice:

The logic is almost identical.

The only difference is:

```txt
Recursion stack

vs

Manual stack
```

---

# Mental Model

Recursive version:

```txt
Python remembers future work.
```

Iterative version:

```txt
You remember future work.
```

The stack stores:

```txt
Nodes we still need to process.
```

That is the state of DFS.

---

# Python Lab Challenge

Without running:

```python
graph = {
    0: [1, 2],
    1: [4],
    2: [3],
    3: [],
    4: []
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
```

Predict:

```txt
What is the exact print order?
```

Trace the stack step-by-step.

---

# Lesson 5 Completion Criteria

You should now be able to explain:

### Why iterative DFS works

Because DFS is fundamentally stack behavior.

---

### What the stack stores

```txt
Future nodes that still need processing.
```

---

### Difference between recursive and iterative DFS

```txt
Recursive:
Python manages the stack.

Iterative:
You manage the stack.
```

---

### Convert recursive DFS into iterative DFS

From memory, you should be able to derive:

```python
stack = [source]

while stack:
    node = stack.pop()
```

and build the rest of the algorithm around it.

---

Before moving to Lesson 6, answer:

**For the challenge graph, what is the exact stack state after processing node 0, and what is the final traversal order?**
