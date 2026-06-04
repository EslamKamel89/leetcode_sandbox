# Lesson 10 — Graph Problem Readiness

## Lesson Goal

You've now learned:

```txt
Graph Representation
DFS
BFS
Visited
Connected Components
Trees
Cycle Detection
```

The final step is learning how to recognize graph problems quickly.

Most interview failures happen **before coding**.

The candidate knows DFS and BFS.

But they fail to recognize:

```txt
This is actually a graph problem.
```

This lesson builds the recognition system:

```txt
Problem
    ↓
Pattern
    ↓
Traversal
    ↓
Implementation
```

---

# Part 1 — The Real Interview Workflow

Beginners often think:

```txt
Read Problem
    ↓
Write Code
```

Strong candidates think:

```txt
Read Problem
    ↓
Recognize Pattern
    ↓
Choose Traversal
    ↓
Implement
```

---

# The Goal

When reading a problem, your brain should automatically ask:

```txt
Can I model this as nodes and connections?
```

If yes:

```txt
Graph Problem
```

---

# Part 2 — Common Graph Signals

These words should immediately trigger graph thinking.

---

## Signal 1 — Connected

Example:

```txt
Determine whether all computers are connected.
```

Translation:

```txt
Connected Components
```

---

## Signal 2 — Reachable

Example:

```txt
Can city A reach city B?
```

Translation:

```txt
Traversal
```

Usually:

```txt
DFS
or
BFS
```

---

## Signal 3 — Island

Example:

```txt
Count islands.
```

Translation:

```txt
Connected Components
```

Grid problems are often graphs in disguise.

---

## Signal 4 — Region

Example:

```txt
Count connected regions.
```

Translation:

```txt
Connected Components
```

---

## Signal 5 — Neighbor

Example:

```txt
Each node has neighbors.
```

Translation:

```txt
Graph Representation
+
Traversal
```

This is a huge clue.

---

## Signal 6 — Path

Example:

```txt
Find a path.
```

Ask:

```txt
Any path?
or
Shortest path?
```

---

If:

```txt
Any path
```

Often:

```txt
DFS
```

---

If:

```txt
Shortest path
```

Often:

```txt
BFS
```

---

# Part 3 — Pattern Recognition Table

This is the first version of your graph recognition system.

| Problem Signal             | Pattern                        | Tool    |
| -------------------------- | ------------------------------ | ------- |
| Reachability               | Traversal                      | DFS/BFS |
| Connected Groups           | Connected Components           | DFS/BFS |
| Islands                    | Connected Components           | DFS/BFS |
| Regions                    | Connected Components           | DFS/BFS |
| Tree Validation            | Connectivity + Cycle Detection | DFS     |
| Cycle Exists               | Cycle Detection                | DFS     |
| Shortest Path (Unweighted) | Layer Expansion                | BFS     |
| Clone Structure            | Graph Traversal                | DFS/BFS |

---

Memorize the pattern, not the problem.

---

# Part 4 — The Universal Solution Framework

Almost every graph problem follows:

```txt
1. Build Graph
2. Choose Traversal
3. Track Visited
4. Process Nodes
```

---

## Step 1 — Build Graph

Input often looks like:

```python
edges = [
    [0,1],
    [1,2]
]
```

Convert:

```python
graph = {
    0:[1],
    1:[2]
}
```

---

## Step 2 — Choose Traversal

Ask:

```txt
Need shortest path?
```

Yes:

```txt
BFS
```

No:

```txt
DFS
```

---

## Step 3 — Track Visited

Almost always:

```python
visited = set()
```

---

## Step 4 — Process Nodes

The problem-specific logic.

Examples:

```txt
Count
Clone
Measure Area
Detect Cycle
Collect Nodes
```

Everything unique happens here.

---

# Part 5 — Mini Recognition Exercises

Don't think about implementation yet.

Only identify the pattern.

---

## Exercise A

Problem:

```txt
Given a graph,
determine whether node A can reach node B.
```

Question:

```txt
Pattern?
Traversal?
```

---

Expected:

```txt
Reachability

DFS or BFS
```

---

## Exercise B

Problem:

```txt
Count the number of disconnected groups.
```

Expected:

```txt
Connected Components

DFS or BFS
```

---

## Exercise C

Problem:

```txt
Find the minimum number of moves to reach the target.
```

Expected:

```txt
Shortest Path

BFS
```

---

## Exercise D

Problem:

```txt
Determine whether the graph contains a cycle.
```

Expected:

```txt
Cycle Detection

DFS
```

---

## Exercise E

Problem:

```txt
Copy every node and connection into a new graph.
```

Expected:

```txt
Graph Traversal

DFS or BFS
```

This is exactly the pattern behind:

Clone Graph

---

# Part 6 — Mapping To Your First Graph Problems

## Problem 1

Number of Islands

Recognition:

```txt
Island
Connected Region
Count Groups
```

Pattern:

```txt
Connected Components
```

Tool:

```txt
DFS
or
BFS
```

---

## Problem 2

Clone Graph

Recognition:

```txt
Node
Neighbor
Copy Structure
```

Pattern:

```txt
Graph Traversal
```

Tool:

```txt
DFS
or
BFS
```

Plus:

```txt
Visited Map
```

instead of a visited set.

---

# Part 7 — The Fast Recognition Checklist

When reading a graph problem:

### Question 1

```txt
What are the nodes?
```

---

### Question 2

```txt
What are the connections?
```

---

### Question 3

```txt
Need:
Reachability?
Groups?
Cycle?
Shortest Path?
Copy?
```

---

### Question 4

```txt
DFS
or
BFS?
```

---

### Question 5

```txt
What does visited mean here?
```

---

# Python Lab

Run this tiny framework.

```python
problems = [
    "Can A reach B?",
    "Count islands",
    "Find shortest path",
    "Detect cycle",
    "Clone graph"
]

for p in problems:

    print("\nProblem:", p)

    if "reach" in p.lower():
        print("Pattern: Traversal")

    elif "island" in p.lower():
        print("Pattern: Connected Components")

    elif "shortest" in p.lower():
        print("Pattern: BFS")

    elif "cycle" in p.lower():
        print("Pattern: Cycle Detection")

    elif "clone" in p.lower():
        print("Pattern: Graph Traversal")
```

The code itself isn't important.

The mental mapping is.

---

# Final Graph Foundation Map

You should now have this mental system:

```txt
Graph
│
├── Representation
│   ├── Edge List
│   └── Adjacency List
│
├── Traversal
│   ├── DFS
│   └── BFS
│
├── Visited
│
├── Connected Components
│
├── Trees
│
└── Cycle Detection
```

---

# Graduation Test

Without thinking about implementation, identify the pattern.

### Case 1

```txt
Count the number of islands.
```

Pattern?

---

### Case 2

```txt
Can city A reach city B?
```

Pattern?

---

### Case 3

```txt
Find the minimum number of moves.
```

Pattern?

Traversal?

---

### Case 4

```txt
Determine whether all computers form a valid tree.
```

Pattern?

---

### Case 5

```txt
Copy a graph.
```

Pattern?

---

# Course Completion

You have completed the graph foundation curriculum:

```txt
Lesson 1  Representation
Lesson 2  Traversal Mental Model
Lesson 3  Recursive DFS
Lesson 4  Visited Tracking
Lesson 5  Iterative DFS
Lesson 6  BFS
Lesson 7  Connected Components
Lesson 8  Trees Through Graph Theory
Lesson 9  Cycle Detection
Lesson 10 Problem Readiness
```

At this point you're ready to start your first graph problems. Based on the problem sequence we discussed earlier, the best next step is:

1. Number of Islands
2. Clone Graph
3. Graph Valid Tree
4. Course Schedule

These four problems map almost perfectly onto the patterns you've just learned.
