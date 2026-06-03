# Lesson 6 — BFS (Breadth First Search)

## Lesson Goal

So far you've learned:

```txt
Traversal
    ↓
DFS (Recursive)
    ↓
DFS (Iterative)
```

DFS has one personality:

```txt
Go deep first.
```

BFS has a completely different personality:

```txt
Stay shallow.
Expand outward.
```

This lesson is about understanding why changing **one data structure** changes the entire behavior of traversal.

---

# Part 1 — DFS vs BFS

Consider:

```txt
        0
      /   \
     1     2
    / \   / \
   3  4  5  6
```

---

## DFS Thinking

DFS sees:

```txt
0
↓
1
↓
3
```

and keeps going.

Possible order:

```txt
0
1
3
4
2
5
6
```

Notice:

```txt
Depth
Depth
Depth
```

---

## BFS Thinking

BFS sees:

```txt
Distance 0:
0
```

Then:

```txt
Distance 1:
1
2
```

Then:

```txt
Distance 2:
3
4
5
6
```

Order:

```txt
0
1
2
3
4
5
6
```

Notice:

```txt
Layer
Layer
Layer
```

---

# Core Mental Model

DFS:

```txt
Pick a path.
Follow it.
```

BFS:

```txt
Explore everything nearby first.
```

---

# Part 2 — Why BFS Needs a Queue

BFS must remember:

```txt
Who was discovered first?
```

because BFS promises:

```txt
Visit nodes by distance.
```

---

To do that we need:

```txt
FIFO

First In
First Out
```

---

# Queue Example

Imagine people waiting in line.

```txt
A
B
C
```

Who gets served first?

```txt
A
```

because:

```txt
First In
First Out
```

---

Python implementation:

```python
from collections import deque

queue = deque()
```

Add:

```python
queue.append(x)
```

Remove:

```python
queue.popleft()
```

---

# Mini Lab — Queue Behavior

Run:

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
```

Predict first.

Expected:

```txt
A
B
C
```

Compare this to the stack lesson:

```txt
Stack:
C B A

Queue:
A B C
```

This difference creates BFS.

---

# Part 3 — BFS Visualization

Graph:

```txt
0
├── 1
├── 2
└── 3
```

Start:

```python
queue = [0]
```

---

Process:

```txt
0
```

Discover:

```txt
1
2
3
```

Queue becomes:

```txt
[1, 2, 3]
```

---

Next node?

Not:

```txt
3
```

Unlike DFS.

Instead:

```txt
1
```

because it arrived first.

---

Then:

```txt
2
```

---

Then:

```txt
3
```

---

Traversal:

```txt
0
1
2
3
```

This is breadth-first behavior.

---

# Part 4 — First BFS

Graph:

```python
graph = {
    0: [1, 2, 3],
    1: [],
    2: [],
    3: []
}
```

Run:

```python
from collections import deque

queue = deque([0])

visited = {0}

while queue:

    node = queue.popleft()

    print(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)
            queue.append(neighbor)
```

---

Predict before running.

Expected:

```txt
0
1
2
3
```

---

# Part 5 — Layer Expansion

This is the most important BFS idea.

Graph:

```txt
          0
        /   \
       1     2
      /       \
     3         4
```

Distances from 0:

```txt
Distance 0:
0

Distance 1:
1
2

Distance 2:
3
4
```

BFS naturally visits:

```txt
0
1
2
3
4
```

Notice:

```txt
Nearest first
Farthest later
```

This property does NOT exist in DFS.

---

# Part 6 — Why BFS Finds Shortest Paths

Consider:

```txt
0
├── 1
│   └── 4
└── 2
    └── 3
```

Question:

```txt
What is the minimum number of edges from 0 to 4?
```

---

BFS explores:

```txt
Distance 0
↓
Distance 1
↓
Distance 2
```

Therefore:

> The first time BFS reaches a node, it has found the shortest path to that node (in an unweighted graph).

This is one of the most important graph facts.

---

# Interview Recognition Signals

Whenever you see:

```txt
minimum steps
fewest moves
shortest path
nearest
minimum jumps
distance
```

your first thought should be:

```txt
BFS
```

---

# Part 7 — Printing Levels

Run this visualization.

```python
from collections import deque

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

queue = deque([0])
visited = {0}

level = 0

while queue:

    level_size = len(queue)

    print(f"\nLEVEL {level}")

    for _ in range(level_size):

        node = queue.popleft()

        print(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    level += 1
```

---

Expected output shape:

```txt
LEVEL 0
0

LEVEL 1
1
2

LEVEL 2
3
4
5
```

This is exactly how BFS sees the graph.

---

# DFS vs BFS Summary

## DFS

Data Structure:

```txt
Stack
```

Behavior:

```txt
Go deep
Backtrack
```

Common Use:

```txt
Connected Components
Cycle Detection
Flood Fill
```

---

## BFS

Data Structure:

```txt
Queue
```

Behavior:

```txt
Expand by distance
```

Common Use:

```txt
Shortest Path
Minimum Steps
Level Order Traversal
```

---

# Python Lab Challenge

Without running:

```python
from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

queue = deque([0])

visited = {0}

while queue:

    node = queue.popleft()

    print(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)
            queue.append(neighbor)
```

---

## Questions

1. What is the exact traversal order?
2. What is the queue state immediately after processing node `0`?
3. Which nodes belong to:
   - Distance 0
   - Distance 1
   - Distance 2

---

# Lesson 6 Completion Criteria

You should now be able to explain:

### Why BFS uses a queue

Because BFS must process nodes in discovery order.

---

### Why BFS expands in layers

Because FIFO guarantees earlier-discovered nodes are processed first.

---

### Why BFS finds shortest paths

Because nodes are visited in increasing distance order.

---

### Difference between DFS and BFS

```txt
DFS = Stack = Depth

BFS = Queue = Distance
```

When you're comfortable with the challenge, we'll move to **Lesson 7 — Connected Components**, where traversal becomes your first real graph problem-solving pattern.
