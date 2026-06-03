# Lesson 1 — Building Graphs

## Lesson Goal

Before we can traverse a graph, we need to understand how a graph is represented in memory.

A graph algorithm never operates on a drawing like this:

```txt
0 --> 1 --> 2

|
v

3 --> 4
```

The computer only sees data structures.

This lesson is about building the mental bridge:

```txt
Drawing
    ↓
Edge List
    ↓
Adjacency List
```

This is arguably the most important preparation step for graph problems.

---

# Part 1 — Core Concepts

## Concept 1: Node

A node (vertex) is simply an object/location/value in the graph.

Example:

```txt
0
1
2
3
```

Each number is a node.

---

## Concept 2: Edge

An edge is a connection.

```txt
0 --> 1
```

means:

```txt
0 is connected to 1
```

The connection itself is the edge.

---

## Concept 3: Neighbor

If:

```txt
0 --> 1
0 --> 3
```

then:

```txt
1 and 3
```

are neighbors of node 0.

Graph algorithms spend most of their time answering:

> Given a node, who are its neighbors?

Keep that question in mind throughout the lesson.

---

# Part 2 — Edge List

Suppose we have this graph:

```txt
0 --> 1
0 --> 3

1 --> 2

3 --> 4
3 --> 6
3 --> 7
```

One way to store it:

```python
edges = [
    [0, 1],
    [0, 3],
    [1, 2],
    [3, 4],
    [3, 6],
    [3, 7]
]
```

---

## Mental Model

Each row means:

```python
[start, end]
```

Example:

```python
[0, 3]
```

means:

```txt
0 --> 3
```

Nothing more.

Nothing less.

---

## Problem With Edge Lists

Imagine I ask:

> What are node 3's neighbors?

You must scan:

```python
[
    [0,1],
    [0,3],
    [1,2],
    [3,4],
    [3,6],
    [3,7]
]
```

and find all rows starting with:

```python
3
```

That's inefficient.

---

# Part 3 — Adjacency List

Instead we transform the graph into:

```python
graph = {
    0: [1, 3],
    1: [2],
    3: [4, 6, 7]
}
```

Now if I ask:

> What are node 3's neighbors?

The answer is immediate:

```python
graph[3]
```

returns:

```python
[4, 6, 7]
```

This is why almost every graph problem starts by building an adjacency list.

---

# Part 4 — Build One Yourself

Don't run anything yet.

First predict.

---

Given:

```python
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 4]
]
```

Question:

What should the adjacency list become?

Try to write it yourself before reading further.

---

Expected answer:

```python
{
    0: [1, 2],
    1: [3],
    2: [4]
}
```

---

# Part 5 — Python Lab

Now run this.

```python
from collections import defaultdict

edges = [
    [0, 1],
    [0, 3],
    [1, 2],
    [3, 4],
    [3, 6],
    [3, 7]
]

graph = defaultdict(list)

for start, end in edges:
    graph[start].append(end)

print("Adjacency List:")

for node in sorted(graph):
    print(node, "->", graph[node])
```

---

# Before Running

Predict the output.

Especially:

```python
graph[3]
```

What do you expect to see?

---

# After Running

Verify:

```txt
Which node became a key?
Why?

Which nodes became values?
Why?

Why is node 3 mapped to [4, 6, 7]?
```

If you cannot explain those three questions, rerun the code and trace it manually.

---

# Lesson 1 Exercise

Without running code, convert this edge list into an adjacency list.

```python
edges = [
    [0, 1],
    [0, 4],
    [1, 2],
    [1, 3],
    [4, 5]
]
```

Write your answer in this form:

```python
{
    ...
}
```

---

# Lesson 1 Completion Criteria

Before moving to Lesson 2, you should be able to answer:

### Recognition

When you see:

```python
n
edges
```

you immediately think:

```txt
Build adjacency list
```

---

### Understanding

Explain:

```txt
Node
Edge
Neighbor
```

in your own words.

---

### Execution

Convert an edge list into an adjacency list manually.

---

Reply with:

1. Your adjacency list for the exercise.
2. Any questions from the lesson.

Then I'll verify your understanding and either refine the concept or promote you to Lesson 2.
