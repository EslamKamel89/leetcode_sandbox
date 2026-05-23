# Problem Classification

| Question       | Answer                                               |
| -------------- | ---------------------------------------------------- |
| Pattern        | Tree Height / Depth                                  |
| Traversal Type | DFS Recursive (Postorder)                            |
| Core Skill     | Global answer from local subtree information         |
| Key Insight    | Diameter through a node = left height + right height |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Find the longest path between ANY two nodes.”

Important:

```txt id="d1r6g0"
NOT necessarily through the root
```

This is the first major conceptual twist.

---

# What Is Diameter?

Diameter means:

```txt id="yqzq8v"
Longest path between two nodes
```

Measured in:

- EDGES
- not nodes

---

# Visual Example

```txt id="y0q8hz"
        1
       / \
      2   3
     / \
    4   5
```

Longest path:

```txt id="4pljrv"
4 → 2 → 1 → 3
```

Edge count:

```txt id="njlwm0"
4-2
2-1
1-3
```

Total:

```python id="q6e0r4"
3
```

---

# The Most Important Insight

At first glance, this looks difficult because:

```txt id="jlwmv2"
Path can start and end anywhere
```

But the key insight is:

> Every possible diameter passes THROUGH some node.

That changes everything.

---

# Visualize Diameter Passing Through A Node

Suppose we focus on node `2`:

```txt id="jlwmt6"
       2
      / \
     4   5
```

The longest path through node `2` is:

```txt id="jlwms8"
4 → 2 → 5
```

How long is it?

```txt id="jlwmr9"
left height + right height
```

This becomes the core formula.

---

# Core Diameter Formula

At any node:

diameter\_{through\ node}=height(left)+height(right)

This is the heart of the entire problem.

---

# Step 2 — Pattern Recognition

This problem has strong recursive aggregation signals.

---

## Signal 1 — “Longest”

Usually means:

- aggregation
- combining subtree information

---

## Signal 2 — Parent depends on subtree heights

To compute diameter at node:

```txt id="jlwmq5"
Need left height
Need right height
```

Huge DFS indicator.

---

## Signal 3 — Global answer built from local computations

Very important pattern.

Each node computes:

- local candidate diameter

Then updates:

- global maximum

---

# Step 3 — Define The Recursive Meaning

This is the most important step.

Define:

```python id="jlwmp7"
dfs(node)
```

means:

> “Return the height of this subtree.”

Important:

```txt id="jlwmo3"
dfs DOES NOT return diameter
```

This is critical.

---

# Why DFS Returns Height Instead Of Diameter

Because height is the information parents need.

Suppose node:

```txt id="jlwmn2"
        A
       / \
      B   C
```

To compute:

- diameter through A

we need:

- height(B)
- height(C)

So recursion naturally returns:

> subtree height

---

# Step 4 — Build The Solution Gradually

---

# Global Result Variable

```python id="jlwmm4"
self.res = 0
```

This stores:

- best diameter seen so far

---

# Why Global State Is Necessary

Because:

- the largest diameter may occur anywhere
- not necessarily at root

So every node may update:

- global maximum

---

# Base Case

```python id="jlwml1"
if not root:
    return 0
```

Empty subtree height:

```txt id="jlwmk0"
0
```

---

# Recursive Height Computation

```python id="jlwmj9"
left, right = dfs(root.left), dfs(root.right)
```

This recursively computes:

- left subtree height
- right subtree height

---

# Important Mental Model

Each child returns:

```txt id="jlwmi6"
“How tall is my subtree?”
```

---

# Diameter Computation

```python id="jlwmh4"
self.res = max(self.res, left + right)
```

This is the heart of the algorithm.

---

# Why `left + right` Works

Suppose:

```txt id="jlwmg2"
left height = 2
right height = 3
```

Then longest path THROUGH current node:

```txt id="jlwmf8"
2 edges down left
+
3 edges down right
```

Total:

2+3=5

---

# Extremely Important Insight

The current node acts like:

```txt id="jlwme3"
a bridge connecting two deep paths
```

That is the core geometric intuition.

---

# Height Return

```python id="jlwmd7"
return 1 + max(left, right)
```

Same height equation from Maximum Depth.

height(node)=1+\max(height(left),height(right))

---

# Why Only `max()` Here?

Because height means:

```txt id="jlwmc1"
longest downward path
```

A parent can only continue through:

- ONE subtree

not both.

---

# Why Diameter Uses `left + right`

Diameter THROUGH node uses:

- both directions simultaneously

That is the key distinction.

---

# The Most Important Conceptual Difference

| Quantity              | Meaning                    |
| --------------------- | -------------------------- |
| Height                | Longest downward branch    |
| Diameter Through Node | Left branch + right branch |

This distinction is essential.

---

# Visual Recursive Walkthrough

Tree:

```txt id="jlwmb5"
        1
       / \
      2   3
     / \
    4   5
```

---

# Step 1 — Leaves

Leaves:

- 4
- 5
- 3

Each returns height:

```python id="jlwma8"
1
```

Diameter contribution:

0+0=0

---

# Step 2 — Node 2

Receives:

```txt id="jlwm98"
left = 1
right = 1
```

Diameter through node 2:

1+1=2

Update:

```python id="jlwm87"
self.res = 2
```

Height returned:

1+\max(1,1)=2

---

# Step 3 — Root Node 1

Receives:

```txt id="jlwm76"
left = 2
right = 1
```

Diameter through root:

2+1=3

Update:

```python id="jlwm65"
self.res = 3
```

Height returned:

1+\max(2,1)=3

Final answer:

```python id="jlwm54"
3
```

---

# Why This Is Postorder DFS

Execution order:

```txt id="jlwm43"
1. Solve left subtree
2. Solve right subtree
3. Compute current node
```

Current node depends on child information.

That is:

> postorder recursion

---

# This Problem Introduces A Huge New Idea

This is the first problem where:

```txt id="jlwm32"
recursive return value
≠
final answer
```

Very important.

---

# Recursive Return

```txt id="jlwm21"
height
```

---

# Global Answer

```txt id="jlwm10"
diameter
```

Different quantities.

This pattern appears constantly in advanced recursion.

---

# Why This Problem Is A Major Milestone

This problem teaches:

- recursive aggregation
- local vs global state
- subtree information flow
- path geometry in trees

This is significantly more advanced than:

- Maximum Depth
- Balanced Tree

---

# Common Beginner Confusion

Beginners often try:

```txt id="jlwlz9"
dfs() returns diameter
```

But parent nodes do NOT need child diameters.

Parents need:

- child heights

That distinction is crucial.

---

# Time Complexity

Every node visited once:

```txt id="jlwly8"
O(n)
```

---

# Space Complexity

Recursive stack depth:

```txt id="jlwlx7"
O(h)
```

Where:

- `h` = tree height

Worst case:

- skewed tree → `O(n)`

Balanced tree:

- `O(log n)`

---

# Pattern Extraction

| Component         | Meaning                                       |
| ----------------- | --------------------------------------------- |
| Trigger           | Longest path depends on subtree heights       |
| Pattern           | Postorder DFS Aggregation                     |
| Structure         | Compute local candidate, update global answer |
| Core Operation    | left height + right height                    |
| Recursive Meaning | “Return subtree height”                       |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlwlw6"
Every node asks:
“If the longest path passes through ME,
how long would it be?”
```

Then:

- compare all such paths globally
- return the maximum diameter found.
