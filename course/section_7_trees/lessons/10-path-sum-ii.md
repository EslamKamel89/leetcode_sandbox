# Problem Classification

| Question       | Answer                                           |
| -------------- | ------------------------------------------------ |
| Pattern        | Path-Based DFS                                   |
| Traversal Type | DFS + Backtracking                               |
| Core Skill     | Carry and record path state                      |
| Key Insight    | We must preserve the FULL path, not just the sum |

---

# Step 1 — Understand The Real Problem

This problem is a direct evolution of:

- Path Sum I

But now the difficulty increases significantly.

---

# Path Sum I Asked

```txt id="jlwm11"
“Does a valid path exist?”
```

Answer type:

```python id="jlwm22"
True / False
```

---

# Path Sum II Asks

```txt id="jlwm33"
“Return ALL valid paths.”
```

Answer type:

```python id="jlwm44"
[[path1], [path2], ...]
```

Huge conceptual upgrade.

---

# The Most Important Difference

In Path Sum I:

```txt id="jlwm55"
Only needed current sum
```

---

# In Path Sum II:

```txt id="jlwm66"
Need the ENTIRE path history
```

This transforms the problem into:

> path-state management

---

# Visual Example

Tree:

```txt id="jlwm77"
           5
         /   \
        4     8
       /     / \
      11    13  4
     /  \        / \
    7    2      5   1
```

Target:

```txt id="’wini88"
22
```

Valid paths:

```txt id="’wini99"
5 → 4 → 11 → 2
5 → 8 → 4 → 5
```

Return:

```python id="jlvn00"
[
  [5,4,11,2],
  [5,8,4,5]
]
```

---

# Step 2 — Pattern Recognition

This problem has strong:

- path DFS
- backtracking
- recursive state management

signals.

---

# Signal 1 — “All root-to-leaf paths”

We must:

- explore ALL complete paths

DFS naturally does this.

---

# Signal 2 — “Return the actual paths”

Now recursion must carry:

- full path information

not just sums.

---

# Signal 3 — “Multiple solutions”

This means:

- cannot stop after first valid path

Must continue exploring.

---

# Step 3 — Define The Recursive Meaning

Define:

```python id="jlvn11"
dfs(node, nodes)
```

means:

```txt id="jlvn22"
“We are currently standing at this node,
and nodes contains the path so far.”
```

This recursive meaning is everything.

---

# Important Mental Model

The recursion carries:

- the CURRENT PATH STATE

downward through the tree.

---

# Visualize Path State

Suppose traversal:

```txt id="jlvn33"
5 → 4 → 11
```

Then:

```python id="jlvn44"
nodes = [5,4,11]
```

The recursive calls transport:

- path history

through recursion.

---

# Step 4 — Build The Solution Gradually

---

# Result Storage

```python id="jlvn55"
self.res = []
```

This stores:

- all valid paths found

---

# Why Global Result Is Useful

Recursive calls explore:

- independent branches

Whenever a valid leaf is found:

- append path immediately

---

# Base Case — Empty Node

```python id="jlvn66"
if not root:
    return nodes
```

---

# What This Means

No node exists:

- path ends here

Nothing further to explore.

---

# Important Observation

This return value is actually not necessary here.

The algorithm works because:

- result stored globally

This line could simply be:

```python id="jlvn77"
return
```

The important logic is:

- path exploration
- result collection

---

# Extend Current Path

```python id="jlvn88"
nodes = [*nodes, root.val]
```

This is extremely important.

---

# What This Does

Suppose:

```python id="jlvn99"
nodes = [5,4]
```

Current node:

```txt id="jlvo00"
11
```

New path becomes:

```python id="jlvo11"
[5,4,11]
```

---

# Why Create A NEW List?

This is critical.

---

# Problem With Shared Mutable Lists

Suppose we did:

```python id="jlvo22"
nodes.append(root.val)
```

Then:

- all recursive branches share same list

That causes path corruption.

---

# Example Of Corruption

Suppose:

```txt id="jlvo33"
Left branch adds:
11
```

Then right branch accidentally also sees:

- 11

even though it belongs only to left path.

Very dangerous bug.

---

# Why This Copying Works

```python id="jlvo44"
nodes = [*nodes, root.val]
```

creates:

- completely new path list

Each recursive branch gets:

- isolated path state

This avoids manual backtracking cleanup.

---

# Leaf Node Check

```python id="jlvo55"
if not root.left and not root.right
```

Meaning:

- complete root-to-leaf path finished

---

# Sum Validation

```python id="jlvo66"
sum(nodes) == targetSum
```

Check whether current path satisfies target.

---

# Important Observation About Efficiency

This works,
but it recalculates:

```python id="jlvo77"
sum(nodes)
```

every time.

That costs:

```txt id="jlvo88"
O(path length)
```

More optimized solutions carry:

- running sum

like Path Sum I.

But conceptually this version is excellent for learning.

---

# Save Valid Path

```python id="jlvo99"
self.res.append(nodes)
```

Very important.

---

# Why Append COPY-SAFE Path?

Because:

- `nodes` already isolated
- safe to store directly

No future mutation problems.

---

# Recursive Exploration

```python id="jlvp00"
dfs(root.left, nodes)
dfs(root.right, nodes)
```

This explores:

- all possible root-to-leaf paths

DFS naturally explores:

- one complete path at a time

---

# Visual Recursive Walkthrough

Tree:

```txt id="jlvp11"
           5
         /   \
        4     8
       /     / \
      11    13  4
     /  \        / \
    7    2      5   1
```

Target:

```txt id="jlvp22"
22
```

---

# STEP 1 — Root

```python id="jlvp33"
dfs(5, [])
```

New path:

```python id="jlvp44"
[5]
```

---

# STEP 2 — Left Branch

```python id="jlvp55"
dfs(4, [5])
```

New path:

```python id="jlvp66"
[5,4]
```

---

# STEP 3 — Node 11

```python id="jlvp77"
[5,4,11]
```

---

# STEP 4 — Explore 7

```python id="jlvp88"
[5,4,11,7]
```

Sum:

5+4+11+7=27

Not valid.

Backtrack naturally.

---

# STEP 5 — Explore 2

```python id="jlvp99"
[5,4,11,2]
```

Sum:

5+4+11+2=22

Valid.

Append:

```python id="jlvq00"
[[5,4,11,2]]
```

---

# STEP 6 — Explore Right Subtree

Eventually:

```python id="jlvq11"
[5,8,4,5]
```

Sum:

5+8+4+5=22

Append.

Final result:

```python id="jlvq22"
[
  [5,4,11,2],
  [5,8,4,5]
]
```

---

# Full DFS Exploration Visualization

```txt id="jlvq33"
5
├── 4
│   └── 11
│       ├── 7   ❌
│       └── 2   ✅
│
└── 8
    ├── 13  ❌
    └── 4
         ├── 5 ✅
         └── 1 ❌
```

DFS explores:

- one complete path at a time

---

# Why This Is Backtracking

Even though explicit:

```python id="jlvq44"
nodes.pop()
```

does not exist,
the algorithm STILL behaves like backtracking.

Why?

Because each recursive call creates:

- isolated path state

So recursion naturally discards old paths when returning.

---

# Compare With Explicit Backtracking

Alternative style:

```python id="jlvq55"
nodes.append(root.val)

dfs(...)

nodes.pop()
```

This mutates:

- one shared list

then manually undoes changes.

Your solution instead uses:

- immutable-style copying

Much easier conceptually.

---

# Why This Problem Is Important

This problem introduces:

```txt id="jlvq66"
path reconstruction
```

not just:

- path validation

This is foundational for:

- backtracking
- graph DFS
- combinatorial search

---

# Major Conceptual Upgrade From Path Sum I

## Path Sum I

Carry:

- current sum

---

## Path Sum II

Carry:

- full path history

Huge recursive state-management progression.

---

# Time Complexity

Every node visited once.

But:

- `sum(nodes)` costs extra

Worst-case:

```txt id="jlvq77"
O(n²)
```

in skewed tree.

---

# Optimized Version

Better approach:

- carry running sum separately

Then complexity becomes:

```txt id="jlvq88"
O(n)
```

---

# Space Complexity

Recursive depth + stored paths:

```txt id="jlvq99"
O(h)
```

recursive stack

plus:

- result storage

---

# Pattern Extraction

| Component         | Meaning                     |
| ----------------- | --------------------------- |
| Trigger           | Need all root-to-leaf paths |
| Pattern           | DFS + Backtracking          |
| Structure         | Carry path state downward   |
| Core Operation    | extend current path         |
| Recursive Meaning | “Current path so far”       |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlvr00"
Walk down every root-to-leaf path,
while carrying the FULL path history.
```

Whenever:

- a leaf
- has target sum

store that complete path.
