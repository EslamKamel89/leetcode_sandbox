# Problem Classification

| Question       | Answer                                           |
| -------------- | ------------------------------------------------ |
| Pattern        | BFS Level Traversal                              |
| Traversal Type | Breadth-First Search                             |
| Core Skill     | Process tree level-by-level                      |
| Key Insight    | Queue stores the current frontier of exploration |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Return nodes grouped by levels.”

Example:

```txt id="jlws11"
Level 0 → [3]
Level 1 → [9,20]
Level 2 → [15,7]
```

Final output:

```python id="jlws22"
[[3],[9,20],[15,7]]
```

---

# The Most Important Insight

This problem is fundamentally about:

```txt id="jlws33"
distance from root
```

Every tree level corresponds to:

- nodes with same distance from root

That is EXACTLY what BFS is designed for.

---

# Why DFS Is NOT Natural Here

DFS explores:

```txt id="jlws44"
one complete branch deeply
```

Example:

```txt id="jlws55"
3 → 9
```

before even seeing:

- node `20`

But level-order traversal requires:

```txt id="jlws66"
process ALL nearby nodes first
```

That is BFS behavior.

---

# BFS Mental Model

Imagine water spreading outward:

```txt id="jlws77"
distance 0
distance 1
distance 2
```

BFS expands:

- evenly outward

Level-by-level.

---

# Visual Tree

```txt id="jlws88"
        3
       / \
      9   20
         /  \
        15   7
```

---

# Desired Traversal Order

```txt id="jlws99"
3
9 20
15 7
```

Grouped by depth.

---

# Step 2 — Why Queue Is Perfect For BFS

BFS needs:

```txt id="jlwt00"
First discovered
→ first processed
```

That is exactly:

```txt id="jlwt11"
FIFO
(First In First Out)
```

Queue behavior.

---

# Queue Visualization

Start:

```txt id="jlwt22"
Queue = [3]
```

Process `3`.

Add children:

```txt id="jlwt33"
Queue = [9,20]
```

Now process:

- `9`
- then `20`

exactly preserving level order.

---

# Step 3 — Build The Solution Gradually

---

# Empty Tree Check

```python id="jlwt44"
if not root:
    return []
```

---

# Why Return Empty List?

No nodes exist.

Therefore:

- no levels exist

---

# Initialize Queue

```python id="jlwt55"
queue = collections.deque()
queue.append(root)
```

---

# Why Use `deque`?

Because BFS repeatedly:

- removes from front
- adds to back

`deque` supports:

```txt id="jlwt66"
O(1)
```

operations for both.

Very important.

---

# Queue Meaning

The queue stores:

```txt id="jlwt77"
nodes waiting to be processed
```

More specifically:

```txt id="jlwt88"
current BFS frontier
```

---

# Result Storage

```python id="jlwt99"
result = []
```

Stores:

- all processed levels

---

# Main BFS Loop

```python id="jlwu00"
while queue:
```

Meaning:

```txt id="jlwu11"
“As long as unexplored nodes exist”
```

---

# Important BFS Insight

Each iteration of the while-loop processes:

```txt id="jlwu22"
ONE COMPLETE LEVEL
```

This is the key BFS pattern.

---

# Current Level Storage

```python id="jlwu33"
level = []
```

Stores:

- values of current level only

---

# The MOST Important BFS Technique

```python id="jlwu44"
for _ in range(len(queue)):
```

This line is EVERYTHING.

---

# Why This Is Necessary

Suppose queue initially contains:

```txt id="jlwu55"
[9,20]
```

Those are:

- current level nodes

But while processing them,
we add:

```txt id="jlwu66"
15,7
```

to the queue.

Without freezing queue length first:

```txt id="jlwu77"
current level
+
next level
```

would mix together.

Huge bug.

---

# This Line Freezes The Level

```python id="jlwu88"
len(queue)
```

captures:

```txt id="jlwu99"
“How many nodes belong to THIS level?”
```

before processing starts.

This is the core BFS level-order technique.

---

# Node Processing

```python id="jlwv00"
node = queue.popleft()
```

Removes:

- oldest discovered node

FIFO behavior.

---

# Add Node Value

```python id="jlwv11"
level.append(node.val)
```

Store current node in:

- current level group

---

# Add Children To Queue

```python id="jlwv22"
queue.append(node.left)
queue.append(node.right)
```

This schedules:

- next level for future processing

---

# Important Observation

Children are NOT processed immediately.

They wait in queue until:

- current level fully finishes

That is exactly what creates:

- level-order traversal

---

# Why The `if node:` Check Exists

Your solution enqueues:

- actual nodes
- None values

Example:

```python id="jlwv33"
queue.append(node.left)
```

Even if:

```python id="jlwv44"
node.left == None
```

So:

```python id="jlwv55"
if node:
```

filters invalid nodes before processing.

---

# Alternative Cleaner Style

Many BFS solutions avoid storing `None` entirely:

```python id="jlwv66"
if node.left:
    queue.append(node.left)
```

This avoids:

- useless queue entries

More efficient.

But your version still works correctly.

---

# Store Finished Level

```python id="jlwv77"
if level:
    result.append(level)
```

Once current level fully processed:

- save it into final result

---

# Visual BFS Execution

Tree:

```txt id="jlwv88"
        3
       / \
      9   20
         /  \
        15   7
```

---

# INITIAL STATE

Queue:

```txt id="jlwv99"
[3]
```

Result:

```python id="jlww00"
[]
```

---

# LEVEL 0

Queue size:

```txt id="jlww11"
1
```

Process node `3`.

Level becomes:

```python id="jlww22"
[3]
```

Add children:

```txt id="jlww33"
Queue = [9,20]
```

Store level:

```python id="jlww44"
[[3]]
```

---

# LEVEL 1

Queue size:

```txt id="jlww55"
2
```

Process `9`:

```python id="jlww66"
[9]
```

Process `20`:

```python id="jlww77"
[9,20]
```

Add children:

```txt id="jlww88"
Queue = [15,7]
```

Store level:

```python id="jlww99"
[[3],[9,20]]
```

---

# LEVEL 2

Queue size:

```txt id="jlwx00"
2
```

Process `15`, `7`.

Level:

```python id="jlwx11"
[15,7]
```

No children added.

Queue becomes empty.

Store level:

```python id="jlwx22"
[[3],[9,20],[15,7]]
```

---

# BFS Expansion Visualization

```txt id="jlwx33"
Step 1:
    3

Step 2:
    9   20

Step 3:
   15    7
```

BFS expands outward level-by-level.

---

# Why This Problem Is Important

This problem teaches:

- queue-based traversal
- BFS frontier expansion
- level processing
- distance-layer thinking

This is foundational for:

- shortest path
- graph BFS
- grid traversal
- minimum moves problems

---

# Compare DFS vs BFS Here

---

# DFS Behavior

```txt id="jlwx44"
3 → 9
```

goes deep immediately.

Not suitable for:

- grouped levels

---

# BFS Behavior

```txt id="jlwx55"
3
then
9,20
then
15,7
```

Perfectly matches:

- level structure

---

# The Deep BFS Insight

BFS naturally organizes nodes by:

```txt id="jlwx66"
distance from source
```

In trees:

```txt id="jlwx77"
source = root
```

So:

- # same distance
- same level

That is why BFS fits perfectly.

---

# Time Complexity

Every node processed once:

```txt id="jlwx88"
O(n)
```

---

# Space Complexity

Queue may hold entire level:

```txt id="jlwx99"
O(w)
```

Where:

- `w` = maximum tree width

---

# Pattern Extraction

| Component      | Meaning                          |
| -------------- | -------------------------------- |
| Trigger        | Need level-by-level processing   |
| Pattern        | BFS                              |
| Structure      | Queue-based frontier expansion   |
| Core Operation | process one full level at a time |
| Key Technique  | freeze queue length              |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlwy00"
Process all nodes at distance d
before processing distance d+1.
```

That is exactly what BFS guarantees.
