# Lesson 9 — Cycle Detection

## Lesson Goal

This lesson completes the second major graph pattern in your curriculum:

```txt
Traversal
    ↓
Visited
    ↓
Connected Components
    ↓
Cycle Detection
```

You've already learned:

```txt
A tree = connected + acyclic
```

The missing piece is:

```txt
How do we actually detect a cycle?
```

---

# Part 1 — What Is A Cycle?

You already know the definition:

```txt
A → B → C → A
```

or in an undirected graph:

```txt
0 -- 1
|    |
|    |
3 -- 2
```

A cycle means:

```txt
Starting somewhere
↓
Following edges
↓
Returning to a previously visited node
```

---

# Important Observation

Not every revisit is a cycle.

This is where many beginners get confused.

Consider:

```txt
0 -- 1
```

Suppose DFS starts at:

```txt
0
```

Visits:

```txt
1
```

Now from node 1:

```txt
Neighbor = 0
```

Question:

```txt
Did we find a cycle?
```

Answer:

```txt
No
```

We simply returned to the node we came from.

This introduces the most important idea of the lesson.

---

# Part 2 — Parent Tracking

Graph:

```txt
0 -- 1 -- 2
```

DFS:

```txt
0
↓
1
↓
2
```

At node 2:

```txt
Neighbor = 1
```

But:

```txt
1
```

is simply:

```txt
The parent
```

that brought us here.

That is normal.

---

Therefore cycle detection needs:

```txt
Visited
+
Parent
```

not just:

```txt
Visited
```

---

# Mental Model

When DFS moves:

```txt
0 → 1
```

we remember:

```txt
Parent of 1 = 0
```

---

When DFS moves:

```txt
1 → 2
```

we remember:

```txt
Parent of 2 = 1
```

---

Now if node 2 sees:

```txt
1
```

again:

that's expected.

---

But if node 2 sees:

```txt
0
```

then something strange happened.

We found another route back.

That means:

```txt
Cycle
```

---

# Part 3 — Back Edge

This is the graph theory term.

Suppose:

```txt
0 -- 1
|    |
|    |
3 -- 2
```

DFS:

```txt
0
↓
1
↓
2
↓
3
```

At node 3:

```txt
Neighbor = 0
```

Question:

```txt
Is 0 my parent?
```

No.

Parent is:

```txt
2
```

---

Question:

```txt
Have I already visited 0?
```

Yes.

---

This is called a:

```txt
Back Edge
```

Meaning:

```txt
Current node
    ↓
Points back to an earlier node
```

A back edge indicates a cycle.

---

# Cycle Detection Rule (Undirected Graph)

During DFS:

```txt
If neighbor is visited
AND
neighbor is not parent

=> Cycle Found
```

This is the core rule.

---

# Part 4 — Visual Example

Graph:

```txt
0 -- 1
|    |
|    |
3 -- 2
```

---

Start:

```txt
DFS(0)
```

---

Visit:

```txt
0
```

Parent:

```txt
None
```

---

Visit:

```txt
1
```

Parent:

```txt
0
```

---

Visit:

```txt
2
```

Parent:

```txt
1
```

---

Visit:

```txt
3
```

Parent:

```txt
2
```

---

Node 3 sees:

```txt
0
```

---

Check:

```txt
Visited?
YES

Parent?
NO
```

Result:

```txt
Cycle Found
```

---

# Part 5 — Recursive Cycle Detection

Run this.

```python
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
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
```

---

Before Running

Predict:

```txt
Tree?
Cycle?
Output?
```

Expected:

```txt
True
```

because the graph contains a cycle.

---

# Understanding The Critical Line

```python
elif neighbor != parent:
```

This line is the heart of undirected cycle detection.

Without it:

```txt
Every graph
would appear cyclic
```

because every child naturally sees its parent.

---

# Part 6 — Test A Valid Tree

Run:

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
```

using the same function.

Expected:

```txt
False
```

No cycle exists.

---

# Visual Comparison

## Tree

```txt
0 -- 1 -- 2 -- 3
```

DFS never encounters:

```txt
Visited node
that is not parent
```

---

## Cycle

```txt
0 -- 1
|    |
|    |
3 -- 2
```

DFS eventually encounters:

```txt
Visited node
that is NOT parent
```

Cycle detected.

---

# Part 7 — Directed Graphs (Introduction)

Directed graphs are different.

Consider:

```txt
0 → 1 → 2
↑       |
|       |
└───────┘
```

Here:

```txt
Parent tracking
is not enough
```

because edges have direction.

---

Instead we track:

```txt
Current DFS Path
```

using something often called:

```python
path = set()
```

or

```python
recursion_stack = set()
```

---

Core idea:

```txt
If DFS reaches a node
already on the current path

=> Cycle
```

---

Example:

```txt
0
↓
1
↓
2
↓
0
```

Node 0 is already active on the DFS path.

Therefore:

```txt
Cycle Found
```

---

For now, just remember:

```txt
Undirected Cycle Detection
=
Visited + Parent

Directed Cycle Detection
=
Visited + Current DFS Path
```

We'll use this later in problems like:

Course Schedule

---

# Python Lab

Run both graphs below.

## Graph A

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
```

Prediction:

```txt
Tree
No Cycle
```

---

## Graph B

```python
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}
```

Prediction:

```txt
Cycle
```

---

Observe how only one extra edge changes everything.

---

# Pattern Extraction

```txt
Need:
    Detect cycle

Pattern:
    DFS + Parent Tracking

Structure:
    Visited Set
    Parent Node

Flow:
    DFS
        If neighbor unvisited:
            Continue DFS
        Else if neighbor != parent:
            Cycle
```

---

# Challenge

Without running code:

```txt
0 -- 1 -- 2
     |
     3
```

Adjacency List:

```python
graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1]
}
```

Questions:

1. Is the graph connected?
2. Does it contain a cycle?
3. Is it a tree?
4. During DFS, will you ever encounter:

   ```txt
   visited neighbor != parent
   ```

   ?

5. Which lesson's tree definition can you use to verify your answer?

---

# Lesson 9 Completion Criteria

You should now be able to explain:

### How traversal detects cycles

By finding:

```txt
A previously visited node
that should not have been reachable again.
```

---

### Why parent tracking is needed

Because seeing your parent again is normal in an undirected graph.

---

### Undirected Cycle Detection Rule

```txt
Visited neighbor
+
Neighbor is not parent
=
Cycle
```

---

### Directed Cycle Detection Intuition

```txt
Visited node on current DFS path
=
Cycle
```

---

At this point you have completed the graph foundation layer:

```txt
Representation
✓

Traversal
✓

DFS
✓

BFS
✓

Visited
✓

Connected Components
✓

Trees as Graphs
✓

Cycle Detection
✓
```

The next step after this mini-course is **Lesson 10 — Graph Problem Readiness**, where we connect all of these patterns to actual LeetCode recognition signals and prepare for problems like:

- Number of Islands
- Clone Graph
- Graph Valid Tree
- Course Schedule
