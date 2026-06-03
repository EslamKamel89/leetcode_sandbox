# Lesson 3 — DFS (Recursive)

## Lesson Goal

In Lesson 2, we learned:

```txt
Traversal = exploring reachable nodes.
```

But we never answered:

```txt
How do we systematically explore them?
```

DFS is the first real traversal algorithm.

---

# Part 1 — The Core Idea

DFS stands for:

```txt
Depth First Search
```

The name tells you exactly what it does:

```txt
Go deep first.
Explore later.
```

---

Consider:

```txt
0
|
1
|
2
|
3
```

Starting at:

```txt
0
```

DFS thinks:

```txt
0
↓
1
↓
2
↓
3
```

It keeps going deeper.

It does NOT stop at:

```txt
0
```

and ask:

```txt
What are all my options?
```

That's BFS thinking.

DFS says:

```txt
Pick a path.
Follow it.
```

---

# Part 2 — Why Recursion Fits Naturally

Imagine this graph:

```txt
0
├── 1
│   └── 2
└── 3
```

Suppose we're currently at:

```txt
0
```

We discover:

```txt
1
```

Question:

```txt
How do we explore 1?
```

The answer is surprisingly simple:

```txt
Do exactly what we did for 0.
```

---

At node 1:

```txt
How do we explore 1?
```

Same answer:

```txt
Explore its neighbors.
```

---

At node 2:

```txt
How do we explore 2?
```

Same answer.

This is the hallmark of recursion:

> The problem contains smaller versions of itself.

---

# Part 3 — The Smallest DFS Possible

Forget graphs for a moment.

Imagine a function:

```python
def visit(node):
    print(node)
```

If we call:

```python
visit(0)
```

Output:

```txt
0
```

Nothing special.

Now let's add neighbors.

---

Graph:

```python
graph = {
    0: [1],
    1: [2],
    2: []
}
```

Suppose we're at:

```txt
0
```

We print:

```txt
0
```

Then we discover:

```txt
1
```

How do we explore it?

We call:

```python
visit(1)
```

This is the key idea.

---

# Part 4 — The Recursive Mental Model

Don't think:

```txt
Function calls function
```

Think:

```txt
Explorer hires another explorer
```

---

Example:

```txt
visit(0)

prints 0

finds neighbor 1

asks visit(1) to continue
```

---

Then:

```txt
visit(1)

prints 1

finds neighbor 2

asks visit(2) to continue
```

---

Then:

```txt
visit(2)

prints 2

no neighbors
```

Now something important happens.

---

# Part 5 — Backtracking

At:

```txt
2
```

there is nowhere else to go.

DFS says:

```txt
Return.
```

We go back to:

```txt
1
```

---

Question:

```txt
Did node 1 have more neighbors?
```

If yes:

```txt
Explore them.
```

If no:

```txt
Return again.
```

---

This process is called:

```txt
Backtracking
```

Mental model:

```txt
Go deeper
Hit dead end
Return
```

---

# Part 6 — Visual Call Stack

Graph:

```txt
0
|
1
|
2
```

Execution:

```txt
visit(0)
```

Stack:

```txt
visit(0)
```

---

Then:

```txt
visit(1)
```

Stack:

```txt
visit(1)
visit(0)
```

---

Then:

```txt
visit(2)
```

Stack:

```txt
visit(2)
visit(1)
visit(0)
```

---

Node 2 finishes.

Stack becomes:

```txt
visit(1)
visit(0)
```

---

Node 1 finishes.

Stack becomes:

```txt
visit(0)
```

---

Node 0 finishes.

Stack becomes:

```txt
(empty)
```

---

This stack is what makes DFS naturally go deep.

No extra work is needed.

The recursion stack remembers the path for us.

---

# Part 7 — First Recursive DFS

Run this exactly as written.

```python
graph = {
    0: [1],
    1: [2],
    2: []
}

def dfs(node):
    print(f"Visiting {node}")

    for neighbor in graph[node]:
        dfs(neighbor)

dfs(0)
```

---

## Predict Before Running

Question:

```txt
What order will be printed?
```

Try predicting first.

---

Expected:

```txt
Visiting 0
Visiting 1
Visiting 2
```

---

# Part 8 — Watching Backtracking

Now run this.

```python
graph = {
    0: [1],
    1: [2],
    2: []
}

def dfs(node):
    print(f"ENTER {node}")

    for neighbor in graph[node]:
        dfs(neighbor)

    print(f"EXIT {node}")

dfs(0)
```

---

Predict first.

---

Expected:

```txt
ENTER 0
ENTER 1
ENTER 2
EXIT 2
EXIT 1
EXIT 0
```

---

This output is incredibly important.

It reveals the hidden behavior of DFS:

```txt
Go down
Go down
Go down

Return
Return
Return
```

---

# Part 9 — Why DFS Goes Deep First

This is the lesson's main idea.

Suppose we are at:

```txt
0
```

and discover:

```txt
1
```

DFS immediately does:

```python
dfs(1)
```

before looking at anything else.

That function call interrupts the current work.

Now we are fully focused on:

```txt
1
```

Then:

```txt
2
```

Then:

```txt
3
```

Only after reaching a dead end do we return.

Because recursive calls suspend the current execution, DFS naturally follows a single path as far as possible.

That is why it is called:

```txt
Depth First Search
```

---

# Python Lab Challenge

Without running it, predict the order.

```python
graph = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4],
    4: []
}

def dfs(node):
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs(0)
```

---

# Lesson 3 Completion Criteria

You should now be able to explain:

### Why recursion works for graph traversal

Because:

```txt
Exploring a neighbor
is the same problem
as exploring the current node.
```

---

### What backtracking means

```txt
Go deeper
Hit dead end
Return
```

---

### Why DFS goes deep first

Because recursive calls immediately transfer control to the neighbor.

---

### Predict DFS execution

Given a graph and neighbor order, you can manually determine:

```txt
Visit order
Call stack growth
Backtracking sequence
```

---

Before moving to Lesson 4, answer:

**What is the output of the challenge DFS at the end of this lesson, and why?**
