Excellent. We'll treat **SECTION 8 — Graphs** as a pattern system, not as a collection of isolated problems.

Your curriculum currently defines:

> Lesson 1 — DFS / BFS
> Lesson 2 — Cycle Detection

I would expand that into the actual graph-recognition system used in interviews and LeetCode.

---

# SECTION 8 — Graphs

## First Mental Shift

Before learning graph algorithms, you need a different mental model.

A tree is actually a special graph.

In Trees:

```txt
A → B
A → C
B → D
```

You always know:

- one root
- no cycles
- exactly one path to each node

Graphs remove those guarantees.

```txt
A -- B
|    |
D -- C
```

Now:

- multiple paths may exist
- cycles may exist
- there may be no root
- graph may be disconnected

So the biggest new problem becomes:

> How do I avoid processing the same node forever?

This is why **visited tracking** becomes the central idea of graph problems.

---

# GRAPH PATTERN 1 — Traversal

The foundation of everything.

---

## Problem It Solves

You have:

```txt
node -> neighbors
```

and need to:

- visit everything
- search for something
- count components
- explore a region

---

## Recognition Signals

Look for phrases like:

```txt
connected
reachable
path exists
visit all
explore
neighbor
adjacent
connected component
island
region
```

These almost always indicate:

> Traversal problem

---

# Pattern 1A — DFS

Depth First Search

---

## Mental Model

Imagine entering a cave.

You always go as deep as possible.

```txt
A
|
B
|
C
|
D
```

You keep moving forward before returning.

---

## Why It Works

DFS naturally explores an entire branch before moving elsewhere.

Useful when:

- exploring a component
- marking visited nodes
- recursive reasoning
- backtracking

---

## Structure

```txt
Visit node

for neighbor:
    visit neighbor
```

with:

```txt
visited set
```

to avoid loops.

---

## Typical Problems

- Number of Islands
- Clone Graph
- Max Area of Island
- Surrounded Regions

---

# Pattern 1B — BFS

Breadth First Search

---

## Mental Model

Imagine a wave expanding.

```txt
Start

Distance 0
Distance 1
Distance 2
Distance 3
```

Layer by layer.

---

## Why It Works

BFS visits nodes in order of distance.

That gives a powerful guarantee:

> First time you reach a node = shortest path in an unweighted graph.

---

## Structure

```txt
queue

push start

while queue:
    pop front
    push neighbors
```

---

## Recognition Signals

Words like:

```txt
minimum steps
shortest path
fewest moves
nearest
distance
levels
```

usually mean:

> BFS first

---

## Typical Problems

- Binary Tree Level Order Traversal
- Rotting Oranges
- Word Ladder
- Open the Lock

---

# DFS vs BFS

## DFS

Think:

```txt
Explore
Mark
Search
Component
```

Questions:

```txt
How many?
Can I reach?
What belongs together?
```

---

## BFS

Think:

```txt
Distance
Layers
Minimum moves
Shortest path
```

Questions:

```txt
How far?
How many steps?
What's closest?
```

---

# GRAPH PATTERN 2 — Connected Components

This is usually the first real graph pattern.

---

## Problem It Solves

Graph may be disconnected.

Example:

```txt
A - B

C - D

E
```

There are:

```txt
3 components
```

---

## Recognition Signals

Words like:

```txt
groups
clusters
islands
provinces
regions
connected components
```

---

## Mental Model

Start DFS/BFS.

Everything reachable belongs to the same component.

Then find another unvisited node.

Repeat.

---

## Typical Problems

- Number of Islands
- Number of Provinces
- Max Area of Island

---

# GRAPH PATTERN 3 — Cycle Detection

This is your curriculum's second lesson.

---

## Problem It Solves

Determine whether traversal loops back.

Example:

```txt
A -> B -> C -> A
```

---

## Recognition Signals

Words like:

```txt
cycle
loop
circular dependency
valid tree
can finish courses
dependency graph
```

---

## Why It Matters

Many problems are really asking:

> Does this graph contain a cycle?

Examples:

- Course Schedule
- Graph Valid Tree
- Redundant Connection

---

## Mental Model

While exploring:

```txt
Have I reached a node that is already on my current path?
```

If yes:

```txt
cycle exists
```

---

# GRAPH PATTERN 4 — Topological Sort

One of the highest ROI graph patterns.

---

## Problem It Solves

You have dependencies.

Example:

```txt
Study Math
    ↓
Study Physics
```

Physics cannot come first.

---

## Recognition Signals

Words like:

```txt
prerequisite
dependency
before
after
order
schedule
build order
```

---

## Typical Problems

- Course Schedule
- Course Schedule II
- Alien Dictionary

---

## Mental Model

Find a valid ordering that respects all arrows.

---

# GRAPH PATTERN 5 — Shortest Path

Advanced BFS family.

---

## Problem It Solves

Find cheapest route.

---

## Recognition Signals

```txt
shortest path
minimum cost
least distance
fastest route
```

---

## Variations

### Unweighted

Use BFS.

### Weighted

Use algorithms like:

- Dijkstra
- Bellman-Ford
- Floyd-Warshall

For LeetCode interview preparation:

Dijkstra is the important one.

---

# Graph Pattern Hierarchy

Think of graphs as:

```txt
Traversal
│
├── DFS
├── BFS
│
├── Connected Components
├── Cycle Detection
├── Topological Sort
└── Shortest Path
```

Everything is built on DFS/BFS.

---

# Phase 1 — Problem Selection

For this section, I recommend mapping problems to patterns as follows:

| Pattern              | LeetCode Tags           |
| -------------------- | ----------------------- |
| DFS Traversal        | Graph, DFS              |
| BFS Traversal        | Graph, BFS              |
| Connected Components | Graph, DFS, BFS         |
| Cycle Detection      | Graph, DFS, Union Find  |
| Topological Sort     | Graph, Topological Sort |
| Shortest Path        | Graph, BFS, Dijkstra    |

---

# Candidate Problem Collection

Collect candidate problems from these tags:

### DFS / Components

- Number of Islands
- Max Area of Island
- Number of Provinces
- Surrounded Regions
- Clone Graph

### BFS

- Rotting Oranges
- Open the Lock
- Word Ladder

### Cycle Detection

- Graph Valid Tree
- Redundant Connection
- Course Schedule

### Topological Sort

- Course Schedule II
- Alien Dictionary

### Shortest Path

- Network Delay Time
- Path With Minimum Effort

---

After you gather your candidate list, I'll curate a final progression that maximizes:

1. Pattern isolation
2. Difficulty progression
3. Pattern reuse
4. Interview ROI

and then we'll begin the problem loop:

> Problem → Pattern Prediction → Attempt → Guided Reconstruction → Visual Execution → Pattern Extraction

which matches your mastery-based learning system.
