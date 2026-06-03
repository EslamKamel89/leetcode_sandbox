# Lesson 2 — Graph Traversal Mental Model

## Lesson Goal

In Lesson 1, we learned:

```txt
How a graph is stored.
```

Now we answer a different question:

```txt
Once I have a graph,
how do I move through it?
```

This lesson is intentionally before DFS and BFS.

Many people memorize DFS/BFS code without understanding the real problem they solve.

---

# Part 1 — What Is Traversal?

Suppose we have:

```txt
0 → 1 → 2

|
v

3 → 4
```

and we start at node:

```txt
0
```

Traversal means:

```txt
Explore everything reachable from 0.
```

That's it.

Not DFS.

Not BFS.

Just:

```txt
Starting somewhere,
what can I reach?
```

---

# Mental Model

Imagine a city.

```txt
City A
|
+-- Road --> City B
|
+-- Road --> City C
```

You arrive at:

```txt
City A
```

Question:

```txt
Where can I go?
```

Then:

```txt
Where can I go from there?
```

Then:

```txt
Where can I go next?
```

Graph traversal is simply systematic exploration.

---

# Part 2 — Reachability

This is the first important graph question.

---

Consider:

```txt
0 → 1 → 2

3 → 4
```

Question:

```txt
Can I reach 2 from 0?
```

Answer:

```txt
Yes
```

Path:

```txt
0 → 1 → 2
```

---

Question:

```txt
Can I reach 4 from 0?
```

Answer:

```txt
No
```

There is no path.

---

This idea appears constantly in graph problems.

Recognition signals:

```txt
reachable
connected
path exists
can visit
can reach
```

These often mean:

```txt
Traversal problem
```

---

# Part 3 — Traversal Tree

This is a concept many beginners never learn.

---

Suppose the graph is:

```txt
      0
     / \
    1   3
    |   |
    2   4
```

When we traverse it, we create a temporary structure:

```txt
0
├── 1
│   └── 2
└── 3
    └── 4
```

This is called a traversal tree.

---

Important:

The graph already existed.

We are NOT creating new nodes.

We are recording:

```txt
How we discovered them.
```

---

Think:

```txt
Original Graph
        ↓
Exploration Path
        ↓
Traversal Tree
```

This idea becomes very important later in:

- DFS
- BFS
- Shortest Path

---

# Part 4 — Why Cycles Are Dangerous

Look at this graph:

```txt
0 → 1
↑   ↓
└── 2
```

You can travel:

```txt
0 → 1 → 2 → 0 → 1 → 2 ...
```

forever.

---

Question:

```txt
When should we stop?
```

The graph itself doesn't tell us.

Without additional logic:

```txt
Infinite traversal
```

becomes possible.

---

For now remember only:

> Traversal needs a way to remember where it has already been.

We will solve this in Lesson 4.

---

# Part 5 — Manual Traversal Exercise

No DFS.

No BFS.

Just exploration.

---

Graph:

```txt
0 → 1
0 → 3

1 → 2

3 → 4
3 → 5
```

Adjacency list:

```python
graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4, 5],
    4: [],
    5: []
}
```

Start:

```txt
0
```

---

Question 1

Which nodes are reachable from 0?

Write the complete set.

---

Question 2

Which nodes are NOT reachable from 0?

---

# Part 6 — Visual Traversal Simulator

Run this code.

Do not modify it yet.

```python
graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4, 5],
    4: [],
    5: []
}

current = 0

print(f"Currently at: {current}")
print(f"Neighbors: {graph[current]}")

for neighbor in graph[current]:
    print(f"Can move to: {neighbor}")
```

---

# Think Before Running

Try predicting the output first.

Ask yourself:

```txt
What information do I need
to continue exploring?
```

You should notice something important:

When standing on a node, the only thing you really need is:

```python
graph[current]
```

because that tells you:

```txt
Where can I go next?
```

---

# Core Insight of Lesson 2

Every graph algorithm eventually becomes:

```python
for neighbor in graph[node]:
```

Everything else:

- DFS
- BFS
- Cycle Detection
- Connected Components
- Shortest Path

is built on top of that one idea.

---

# Lesson 2 Completion Check

Before moving to Lesson 3, you should be able to answer:

### Conceptual

What does traversal mean?

---

### Reachability

For a given start node:

```txt
Which nodes can I reach?
```

---

### Traversal Tree

What information does a traversal tree represent?

---

### Prediction

Given a graph and a start node, you can manually predict:

```txt
Which nodes will eventually be visited.
```

without writing DFS or BFS.

---

Reply with:

1. Answer to Question 1 (reachable nodes).
2. Answer to Question 2 (unreachable nodes).
3. Your explanation of what a traversal tree represents.

Then we'll start **Lesson 3 — Recursive DFS**, where traversal becomes an actual algorithm.
