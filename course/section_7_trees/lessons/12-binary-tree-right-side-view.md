# Problem Classification

| Question       | Answer                                                            |
| -------------- | ----------------------------------------------------------------- |
| Pattern        | BFS Level Traversal                                               |
| Traversal Type | Breadth-First Search                                              |
| Core Skill     | Extract meaningful information from each level                    |
| Key Insight    | The last node processed in a level is the visible right-side node |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “If you stand on the RIGHT side of the tree, what nodes can you see?”

Important:

```txt id="jlxz11"
Only ONE node per level is visible
```

Specifically:

- the rightmost node of each level

---

# Visual Example

Tree:

```txt id="jlxz22"
        1
       / \
      2   3
       \    \
        5    4
```

---

# What Is Visible?

From the right side:

```txt id="jlxz33"
Level 0 → 1
Level 1 → 3
Level 2 → 4
```

Answer:

```python id="jlxz44"
[1,3,4]
```

---

# The Most Important Insight

This is fundamentally:

```txt id="jlxz55"
a level-order traversal problem
```

Why?

Because:

- visibility depends on LEVELS
- not paths
- not subtree structure

At each level we need:

- the rightmost node

That naturally suggests:

> BFS

---

# Why BFS Fits Perfectly

BFS already processes:

```txt id="jlxz66"
one level at a time
```

So after processing a level:

```txt id="jlxz77"
the LAST node encountered
=
rightmost visible node
```

That is the key observation.

---

# Compare With Binary Tree Level Order Traversal

## Level Order Traversal

Stored:

```python id="jlxz88"
entire level
```

Example:

```python id="jlxz99"
[9,20]
```

---

## Right Side View

We only care about:

```python id="jlya00"
level[-1]
```

The last node.

---

# Step 2 — Queue Mental Model

Queue stores:

```txt id="jlya11"
current BFS frontier
```

Meaning:

- nodes waiting to be processed

BFS expands:

- level-by-level

---

# Visual BFS Expansion

```txt id="jlya22"
        1
       / \
      2   3
       \    \
        5    4
```

---

# Queue Evolution

Start:

```txt id="jlya33"
[1]
```

Then:

```txt id="jlya44"
[2,3]
```

Then:

```txt id="jlya55"
[5,4]
```

Each queue state represents:

- one complete level

---

# Step 3 — Build The Solution Gradually

---

# Queue Initialization

```python id="jlya66"
queue = collections.deque()
queue.append(root)
```

---

# Important Observation

Your solution appends:

```python id="jlya77"
root
```

even if:

```python id="jlya88"
root == None
```

This still works because later:

```python id="jlya99"
if node:
```

filters invalid nodes.

---

# Alternative Cleaner Style

Many solutions do:

```python id="jlyb00"
if not root:
    return []
```

before queue initialization.

This avoids:

- storing useless `None`

---

# Result Storage

```python id="jlyb11"
result = []
```

Stores:

- visible right-side nodes

---

# Main BFS Loop

```python id="jlyb22"
while queue:
```

Meaning:

```txt id="jlyb33"
“As long as another level exists”
```

---

# Current Level Storage

```python id="jlyb44"
level = []
```

Stores:

- all node values for current level

---

# The Most Important BFS Technique

```python id="jlyb55"
for _ in range(len(queue)):
```

This freezes:

```txt id="jlyb66"
current level size
```

before processing starts.

---

# Why This Is Necessary

Suppose queue initially:

```txt id="jlyb77"
[2,3]
```

Those belong to:

- current level

But processing them adds:

```txt id="jlyb88"
5,4
```

to queue.

Without freezing length:

- levels would mix together

Huge BFS concept.

---

# Node Processing

```python id="jlyb99"
node = queue.popleft()
```

Processes:

- oldest discovered node first

FIFO behavior.

---

# Node Validation

```python id="jlyc00"
if node:
```

Prevents:

- processing `None`

---

# Add Children

```python id="jlyc11"
queue.append(node.left)
queue.append(node.right)
```

Schedules:

- next level

for future BFS processing.

---

# Record Current Level

```python id="jlyc22"
level.append(node.val)
```

Stores node values in:

- left-to-right BFS order

---

# The Key Right-Side Observation

At end of level processing:

```python id="jlyc33"
level[-1]
```

is:

```txt id="jlyc44"
the rightmost node
```

because BFS processes:

- left-to-right

inside each level.

---

# Store Rightmost Node

```python id="jlyc55"
result.append(level[-1])
```

This extracts:

- visible node from current level

---

# Visual BFS Execution

Tree:

```txt id="jlyc66"
        1
       / \
      2   3
       \    \
        5    4
```

---

# INITIAL STATE

Queue:

```txt id="jlyc77"
[1]
```

Result:

```python id="jlyc88"
[]
```

---

# LEVEL 0

Process node `1`.

Level:

```python id="jlyc99"
[1]
```

Add children:

```txt id="jlyd00"
Queue = [2,3]
```

Rightmost node:

```python id="jlyd11"
1
```

Result:

```python id="jlyd22"
[1]
```

---

# LEVEL 1

Queue:

```txt id="jlyd33"
[2,3]
```

Process:

- 2
- 3

Level:

```python id="jlyd44"
[2,3]
```

Children added:

```txt id="jlyd55"
Queue = [5,4]
```

Rightmost node:

```python id="jlyd66"
3
```

Result:

```python id="jlyd77"
[1,3]
```

---

# LEVEL 2

Queue:

```txt id="jlyd88"
[5,4]
```

Level:

```python id="jlyd99"
[5,4]
```

Rightmost node:

```python id="jlye00"
4
```

Result:

```python id="jlye11"
[1,3,4]
```

Queue becomes empty.

Done.

---

# Full BFS Visualization

```txt id="jlye22"
Level 0: [1]      → visible: 1
Level 1: [2,3]    → visible: 3
Level 2: [5,4]    → visible: 4
```

---

# Why This Problem Is Important

This problem teaches:

```txt id="jlye33"
BFS levels are meaningful structures
```

Not just traversal order.

We can extract:

- averages
- rightmost nodes
- widths
- zigzags
- visibility

from each level.

Huge BFS insight.

---

# Deep BFS Understanding

BFS naturally organizes nodes by:

```txt id="jlye44"
distance from root
```

This problem uses:

- one representative node per distance layer

Specifically:

- the rightmost representative

---

# Why DFS Is Less Natural Here

DFS explores:

- deeply first

But visibility depends on:

- horizontal grouping by level

That is BFS territory.

---

# Important Alternative Insight

Another valid solution:

```txt id="jlye55"
DFS Right-First Traversal
```

can also solve this.

If DFS visits:

- right child first

then:

- # first node seen at each depth
  visible node

But BFS is conceptually cleaner for:

- level-based thinking

---

# Time Complexity

Every node processed once:

```txt id="jlye66"
O(n)
```

---

# Space Complexity

Queue may hold entire level:

```txt id="jlye77"
O(w)
```

Where:

- `w` = maximum tree width

---

# Pattern Extraction

| Component      | Meaning                            |
| -------------- | ---------------------------------- |
| Trigger        | Need one representative per level  |
| Pattern        | BFS Level Traversal                |
| Structure      | Process complete level before next |
| Core Operation | take last node of each level       |
| Key Technique  | freeze queue size                  |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlye88"
BFS exposes the tree layer-by-layer.
The last node in each layer
is the visible right-side node.
```
