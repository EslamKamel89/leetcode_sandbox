# Lesson 7 — Connected Components

## Lesson Goal

This is the lesson where graph traversal becomes a problem-solving tool.

So far, DFS and BFS have answered:

```txt
Starting from node X,
what can I reach?
```

Now we ask a bigger question:

```txt
How many separate groups exist?
```

This pattern appears everywhere:

- Number of Islands (200)
- Number of Provinces (547)
- Connected Components in Graph (323)
- Accounts Merge (721)
- Similar String Groups (839)

These all reduce to:

```txt
Find connected components.
```

---

# Part 1 — What Is A Connected Component?

Consider:

```txt
0 -- 1 -- 2

3 -- 4

5
```

There are three separate groups:

```txt
Component #1
0,1,2

Component #2
3,4

Component #3
5
```

A connected component is:

> A maximal group of nodes where every node can reach every other node.

---

# Mental Model

Imagine islands.

```txt
Island A
  houses connected together

Island B
  houses connected together

Island C
  one lonely house
```

Question:

```txt
How many islands exist?
```

We don't care about individual houses anymore.

We care about groups.

---

# Part 2 — Why One DFS Is Not Enough

Graph:

```txt
0 -- 1 -- 2

3 -- 4

5
```

Suppose we start DFS from:

```txt
0
```

Traversal visits:

```txt
0
1
2
```

Then DFS ends.

---

Question:

```txt
Did we discover the entire graph?
```

No.

We never reached:

```txt
3
4
5
```

because they belong to different components.

---

This creates a new idea.

Instead of:

```txt
Run DFS once
```

we do:

```txt
Run DFS repeatedly
```

until every node has been visited.

---

# Part 3 — The Master Pattern

This is one of the most important graph patterns you'll learn.

```txt
For every node:

    If unvisited:

        Start DFS

        Component found
```

Notice what changed.

Previously:

```txt
Start DFS from one source
```

Now:

```txt
Every node is a potential source.
```

---

# Visual Example

Graph:

```txt
0 -- 1 -- 2

3 -- 4

5
```

Start:

```txt
visited = {}
components = 0
```

---

Node 0:

```txt
unvisited
```

Start DFS.

Visits:

```txt
0
1
2
```

Now:

```txt
visited = {0,1,2}
components = 1
```

---

Node 1:

Already visited.

Skip.

---

Node 2:

Already visited.

Skip.

---

Node 3:

Unvisited.

Start DFS.

Visits:

```txt
3
4
```

Now:

```txt
visited = {0,1,2,3,4}
components = 2
```

---

Node 4:

Already visited.

Skip.

---

Node 5:

Unvisited.

Start DFS.

Visits:

```txt
5
```

Now:

```txt
components = 3
```

Finished.

---

Answer:

```txt
3 connected components
```

---

# Core Insight

A DFS does NOT find:

```txt
The graph
```

A DFS finds:

```txt
One connected component
```

This is a major insight.

Many graph problems become easy once you realize this.

---

# Part 4 — First Connected Component Algorithm

Graph:

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}
```

---

DFS:

```python
visited = set()

def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)
```

---

Component Counting:

```python
components = 0

for node in graph:

    if node not in visited:

        dfs(node)

        components += 1

print(components)
```

---

Expected:

```txt
3
```

---

# Why Increment AFTER DFS?

This is important.

When we discover:

```txt
node 0
```

we don't just discover:

```txt
0
```

We discover:

```txt
Entire component
```

through DFS.

Therefore:

```python
dfs(node)

components += 1
```

means:

```txt
One whole component has been processed.
```

---

# Part 5 — Visual Trace

Graph:

```txt
0 -- 1

2 -- 3

4
```

---

Loop:

```txt
node = 0
```

Unvisited.

Run DFS.

Visits:

```txt
0
1
```

Component count:

```txt
1
```

---

Loop:

```txt
node = 1
```

Already visited.

Skip.

---

Loop:

```txt
node = 2
```

Unvisited.

Run DFS.

Visits:

```txt
2
3
```

Component count:

```txt
2
```

---

Loop:

```txt
node = 3
```

Skip.

---

Loop:

```txt
node = 4
```

Unvisited.

Run DFS.

Visits:

```txt
4
```

Component count:

```txt
3
```

Done.

---

# Part 6 — Why Number of Islands Is The Same Pattern

Grid:

```txt
1 1 0

0 1 0

1 0 1
```

Visual:

```txt
Island A

1 1
  1

Island B

1

Island C

1
```

Count:

```txt
3 islands
```

Exactly the same idea.

The grid is just a graph in disguise.

We'll revisit this when we solve Number of Islands.

---

# Python Lab

Run this.

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

visited = set()

def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)

components = 0

for node in graph:

    if node not in visited:

        print(f"Starting new component from {node}")

        dfs(node)

        components += 1

print("\nTotal Components:", components)
```

---

Expected Shape

```txt
Starting new component from 0

Starting new component from 3

Starting new component from 5

Total Components: 3
```

Notice:

```txt
Three DFS calls

Three components
```

---

# Pattern Extraction

This is the first true graph pattern.

```txt
Need:
    Count groups

Pattern:
    Connected Components

Structure:
    DFS/BFS + Visited

Flow:
    Iterate all nodes
        If unvisited:
            DFS
            Count += 1
```

---

# Challenge

Without running code:

```python
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: [5],
    5: [4]
}
```

Question:

1. How many connected components exist?
2. Which DFS calls start new components?
3. What is the final value of `components`?

---

# Lesson 7 Completion Criteria

You should now be able to explain:

### What a connected component is

A group of nodes that can all reach one another.

---

### What one DFS discovers

```txt
One connected component
```

not necessarily the entire graph.

---

### How to count components

```txt
For every node:

    If unvisited:

        DFS

        Count += 1
```

---

### Why Number of Islands is a graph problem

Because each island is simply a connected component.

---

When you're comfortable with this lesson, we'll move to **Lesson 8 — Trees Through Graph Theory**, where we'll connect everything you already know about trees to the graph concepts you've learned.
