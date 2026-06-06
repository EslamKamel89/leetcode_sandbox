We're now in the **Problem Loop**.

So before discussing the solution itself, we start with:

# Step 1 — Pattern Prediction

For Number of Islands, the pattern should be:

```txt
Trigger:
"islands"
"connected land"
"count groups"

↓

Pattern:
Connected Components

↓

Traversal:
DFS (or BFS)

↓

Structure:
Visited Tracking
```

Mental translation:

```txt
The problem is NOT asking:

"How many cells contain 1?"

The problem is asking:

"How many connected groups of 1s exist?"
```

That's the key recognition skill.

---

# Step 2 — Your Attempt

Your solution is correct.

Now we do not jump directly to "accepted solution."

We reconstruct why every piece exists.

---

# What Problem Are We Actually Solving?

Consider:

```txt
1 1 0

1 1 0

0 0 1
```

Humans instantly see:

```txt
Island A

1 1
1 1

Island B

1
```

Answer:

```txt
2
```

The computer does not see islands.

The computer sees cells.

So our job is:

```txt
Find one land cell
↓
Discover every land cell connected to it
↓
Mark them as processed
↓
Repeat
```

This is exactly the Connected Components pattern.

---

# Why Do We Need DFS?

Suppose we find:

```txt
1 1
1 1
```

If we count every `'1'` individually:

```txt
4
```

which is wrong.

We need a mechanism that says:

```txt
Starting from this land cell,
show me ALL land belonging
to the same island.
```

DFS does exactly that.

---

# Reconstructing the DFS

Start with:

```python
def dfs(i, j):
```

Meaning:

```txt
Explore the island
that contains cell (i,j)
```

---

## Boundary Check

```python
if i < 0 or i >= m or j < 0 or j >= n:
    return
```

Why?

Because DFS will try:

```txt
up
down
left
right
```

Eventually it walks outside the grid.

Without this:

```txt
IndexError
```

---

## Water Check

```python
if grid[i][j] != '1':
    return
```

Why?

DFS should only continue through land.

If we reach:

```txt
0
```

the island ends.

Without this check:

```txt
water becomes part of island
```

which breaks the definition.

---

## Visited Tracking

```python
grid[i][j] = '0'
```

This is the most important line.

Mental model:

```txt
Before:

1 = unvisited land

After:

0 = already processed
```

We're using the grid itself as the visited structure.

Equivalent to:

```python
visited.add((i,j))
```

but saves memory.

Without this line:

```txt
A → B
B → A
A → B
B → A
...
```

DFS loops forever.

This is the core graph lesson:

> Traversal without visited tracking is dangerous.

---

## Explore Neighbors

```python
dfs(i, j + 1)
dfs(i, j - 1)
dfs(i + 1, j)
dfs(i - 1, j)
```

Why these four?

Problem statement says:

```txt
horizontally
vertically
```

Not diagonally.

Therefore the graph for a cell is:

```txt
up
down
left
right
```

These are the neighbors.

---

# The Outer Loops

Now let's look at:

```python
for i in range(m):
    for j in range(n):
```

Why scan everything?

Because:

```txt
The graph is disconnected.
```

We don't know where islands begin.

Maybe:

```txt
Island A at top-left

Island B at bottom-right
```

A single DFS can only discover one component.

So we must inspect every cell.

---

# The Most Important Insight

This line:

```python
if grid[i][j] == '1':
```

means:

```txt
I found land that
belongs to no previously discovered island.
```

Why?

Because every discovered island was already converted to:

```txt
0
```

during DFS.

Therefore:

```python
num_of_islands += 1
```

is not counting land.

It is counting:

```txt
new connected components
```

This is the heart of the problem.

---

# Visual Execution

Example 2:

```txt
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```

Start scan:

```txt
(0,0) = 1
```

New island:

```txt
count = 1
```

DFS floods:

```txt
1 1
1 1
```

Grid becomes:

```txt
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
```

Continue scanning.

Find:

```txt
(2,2)
```

New island:

```txt
count = 2
```

Flood it.

Grid:

```txt
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
```

Continue.

Find:

```txt
(3,3)
```

New island:

```txt
count = 3
```

Flood it.

Done.

Answer:

```txt
3
```

---

# Complexity

### Time

Every cell is visited once.

```txt
O(m × n)
```

---

### Space

Recursive call stack in worst case:

```txt
O(m × n)
```

if the whole grid is one giant island.

---

# Pattern Extraction

This is the piece you should remember after forgetting the code.

```txt
Trigger:
Count islands
Count groups
Count regions
Connected land

↓

Pattern:
Connected Components

↓

Traversal:
DFS / BFS

↓

Structure:
Visited Tracking

↓

Flow:
Find unvisited land
    ↓
Flood entire component
    ↓
Mark visited
    ↓
Count once
    ↓
Continue scanning
```

This pattern will reappear almost unchanged in:

- Max Area of Island (695)
- Number of Provinces (547)
- Surrounded Regions (130)
- Flood Fill (733)
- Number of Connected Components in Graph (323)

Before moving to the next problem, answer this:

**Why does incrementing `num_of_islands` before calling `dfs()` count islands rather than land cells?**

That's the key idea this problem is teaching.
