# Problem Classification

| Question       | Answer                                  |
| -------------- | --------------------------------------- |
| Pattern        | Minimum Distance BFS                    |
| Traversal Type | Breadth-First Search                    |
| Core Skill     | Find nearest valid node                 |
| Key Insight    | BFS discovers the shallowest leaf FIRST |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Find the SHORTEST root-to-leaf path.”

Important:

```txt id="jlzf11"
nearest leaf
```

NOT:

- maximum depth
- all paths
- longest branch

This single word changes the optimal pattern completely:

```txt id="jlzf22"
MINIMUM
```

---

# The Most Important Insight

This problem is fundamentally:

```txt id="jlzf33"
nearest-node discovery
```

And BFS is PERFECT for that.

---

# Why BFS Is The Correct Pattern

BFS explores nodes in this order:

```txt id="jlzf44"
distance 0
distance 1
distance 2
distance 3
```

So:

```txt id="jlzf55"
The FIRST leaf BFS finds
=
the nearest leaf
```

This is the key realization.

---

# Visual Intuition

Tree:

```txt id="jlzf66"
        3
       / \
      9   20
         /  \
        15   7
```

---

# BFS Expansion

Level 1:

```txt id="jlzf77"
3
```

Level 2:

```txt id="jlzf88"
9   20
```

Immediately we discover:

```txt id="jlzf99"
9 is a leaf
```

So minimum depth is:

```python id="jlzg00"
2
```

We NEVER need to explore deeper levels.

That is the power of BFS.

---

# Compare With Maximum Depth

This comparison is extremely important.

---

# Maximum Depth Asked

```txt id="jlzg11"
deepest path
```

That required:

- exploring ALL paths
- recursive aggregation

So DFS fit naturally.

---

# Minimum Depth Asks

```txt id="jlzg22"
nearest leaf
```

That is fundamentally:

- shortest distance
- closest valid node

So BFS becomes ideal.

---

# Deep Pattern Recognition

Whenever you see:

```txt id="jlzg33"
minimum
nearest
shortest
fewest moves
closest
```

Think:

> BFS

Because BFS expands:

- level-by-level
- shortest-distance first

---

# Step 2 — Why DFS Is Awkward Here

DFS explores:

```txt id="jlzg44"
one branch deeply first
```

Example:

```txt id="jlzg55"
3 → 20 → 15
```

before even checking:

- node `9`

But node `9` was already:

- a closer leaf

DFS does NOT naturally prioritize:

- shallow answers

BFS does.

---

# BFS Mental Model

Imagine ripples spreading outward:

```txt id="jlzg66"
distance 0
distance 1
distance 2
```

BFS explores:

- all nearby nodes first

Exactly what minimum-depth needs.

---

# Step 3 — Build The BFS Solution Gradually

---

# Empty Tree Check

```python id="jlzg77"
if not root:
    return 0
```

---

# Why Return 0?

No nodes exist:

- no depth exists

---

# Queue Initialization

```python id="jlzg88"
queue = deque([(root, 1)])
```

This is extremely important.

---

# What Does Queue Store?

Each queue item stores:

```python id="jlzg99"
(node, depth)
```

Meaning:

```txt id="jlzh00"
“This node is currently at this depth.”
```

---

# Why Store Depth Explicitly?

BFS naturally tracks:

- traversal order

But NOT depth automatically.

So we store:

- current node depth

inside queue.

---

# Visual Queue State

Start:

```txt id="jlzh11"
[(3,1)]
```

Meaning:

```txt id="jlzh22"
root node at depth 1
```

---

# Main BFS Loop

```python id="jlzh33"
while queue:
```

Meaning:

```txt id="jlzh44"
“As long as unexplored nodes exist”
```

---

# Process Current Node

```python id="jlzh55"
node, depth = queue.popleft()
```

This removes:

- oldest discovered node

FIFO behavior.

---

# The MOST Important Check

```python id="jlzh66"
if not node.left and not node.right:
    return depth
```

This is the heart of the algorithm.

---

# Why Can We Return IMMEDIATELY?

Because BFS guarantees:

```txt id="jlzh77"
first discovered leaf
=
shallowest leaf
```

This is the deepest BFS insight.

---

# Important Mental Model

BFS explores:

- by increasing distance

So if BFS found a leaf at depth 2:

```txt id="jlzh88"
No leaf at depth 1 existed
```

Otherwise BFS would already have found it.

That is why early return is safe.

---

# Add Children To Queue

```python id="jlzh99"
if node.left:
    queue.append((node.left, depth + 1))
```

Meaning:

```txt id="jlzi00"
child is one level deeper
```

Same for right child.

---

# Complete BFS Solution

```python id="jlzi11"
from collections import deque

class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:

            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
```

---

# Step-by-Step BFS Visualization

Tree:

```txt id="jlzi22"
        3
       / \
      9   20
         /  \
        15   7
```

---

# INITIAL STATE

Queue:

```txt id="jlzi33"
[(3,1)]
```

---

# STEP 1 — Process Root

Pop:

```txt id="jlzi44"
(3,1)
```

Is `3` leaf?

```txt id="jlzi55"
No
```

Add children:

```txt id="jlzi66"
(9,2)
(20,2)
```

Queue:

```txt id="jlzi77"
[(9,2),(20,2)]
```

---

# STEP 2 — Process Node 9

Pop:

```txt id="jlzi88"
(9,2)
```

Check:

```txt id="jlzi99"
9 has no children
```

Leaf found.

Return:

```python id="jlzj00"
2
```

DONE.

---

# Important Observation

We NEVER explored:

```txt id="jlzj11"
15
7
```

Because BFS already found:

- nearest leaf

This is the efficiency advantage.

---

# Why BFS Is Beautiful Here

BFS naturally solves:

```txt id="jlzj22"
nearest-answer problems
```

without needing:

- global minimum tracking
- full traversal
- recursive comparisons

---

# Common Beginner Mistake (VERY IMPORTANT)

Many beginners incorrectly write:

```python id="jlzj33"
1 + min(leftDepth, rightDepth)
```

This is WRONG.

---

# Why It Fails

Consider:

```txt id="jlzj44"
    1
     \
      2
       \
        3
```

Left depth:

```txt id="jlzj55"
0
```

Right depth:

```txt id="jlzj66"
3
```

Then:

1+\min(0,3)=1

WRONG.

Actual minimum depth:

```txt id="jlzj77"
3
```

---

# Why This Happens

A missing subtree:

```txt id="jlzj88"
None
```

is NOT:

- a valid leaf path

This is a subtle but extremely important tree concept.

---

# DFS Solution Exists Too

A correct DFS solution must carefully handle:

- missing children

Example:

```python id="jlzj99"
if not root.left:
    return 1 + minDepth(root.right)

if not root.right:
    return 1 + minDepth(root.left)
```

More complicated.

---

# Why BFS Is Better Conceptually

BFS directly matches the problem:

```txt id="jlzk00"
find nearest leaf
```

No tricky edge handling needed.

That makes BFS:

- cleaner
- safer
- more intuitive

---

# Time Complexity

Every node visited at most once:

```txt id="jlzk11"
O(n)
```

---

# Space Complexity

Queue may store entire level:

```txt id="jlzk22"
O(w)
```

Where:

- `w` = maximum width

---

# Pattern Extraction

| Component      | Meaning                          |
| -------------- | -------------------------------- |
| Trigger        | Need nearest / minimum answer    |
| Pattern        | BFS                              |
| Structure      | Expand outward level-by-level    |
| Core Operation | first leaf found wins            |
| Key Insight    | BFS guarantees shortest distance |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlzk33"
Search outward from root level-by-level.
The FIRST leaf encountered
must be the closest leaf.
```

That is exactly why BFS is the ideal pattern here.
