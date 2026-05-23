# Problem Classification

| Question       | Answer                                  |
| -------------- | --------------------------------------- |
| Pattern        | Tree Height / Depth                     |
| Traversal Type | DFS Recursive                           |
| Core Skill     | Recursive subtree aggregation           |
| Key Insight    | Depth of a node depends on child depths |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “What is the longest path from root to leaf?”

Important:

```txt id="h5bl7m"
Depth = number of nodes
```

NOT edges.

---

# Visual Meaning of Depth

Example:

```txt id="nhx4i7"
        3
       / \
      9   20
         /  \
        15   7
```

Longest root-to-leaf path:

```txt id="1u6t35"
3 → 20 → 15
```

Depth:

```txt id="n2vgcm"
3 nodes
```

So answer:

```python id="r0c5ew"
3
```

---

# Why This Problem Is Extremely Important

This is arguably:

> the foundational recursion problem for trees

Because it teaches the core recursive equation:

\text{depth(node)} = 1 + \max(\text{depth(left)},\text{depth(right)})

This equation becomes the foundation for:

- balanced tree
- diameter
- tree DP
- recursive aggregation problems

---

# Step 2 — Pattern Recognition

This problem has strong recursive aggregation signals.

---

## Signal 1 — “Maximum”

Usually implies:

- combine results
- aggregation

---

## Signal 2 — “Depth of subtree”

Huge recursive indicator.

Because:

- subtree depth depends on child subtree depths

---

## Signal 3 — Current answer depends on children

This is classic:

> postorder DFS reasoning

We must know:

- left depth
- right depth

BEFORE computing current node depth.

---

# Step 3 — Define The Recursive Meaning

This is the most important step.

Define:

```python id="r9ov2u"
maxDepth(node)
```

means:

> “Return the maximum depth of the subtree rooted at node.”

Everything follows naturally from this definition.

---

# Step 4 — Build The Recursive Logic

---

# Base Case — Empty Node

```python id="d2u0ng"
if not root:
    return 0
```

---

# What This Means

An empty tree:

```txt id="jlwm5t"
None
```

has depth:

```txt id="6qvbg5"
0
```

Because:

- there are no nodes

---

# Why Returning 0 Is Correct

Suppose leaf node:

```txt id="4mh6gs"
    7
```

Its children are:

```txt id="rglxiw"
None
None
```

Each returns:

```txt id="13uy3l"
0
```

Then leaf depth becomes:

1 + \max(0,0)=1

Correct.

---

# Recursive Relation

```python id="f0jlwm"
return 1 + max(
    self.maxDepth(root.left),
    self.maxDepth(root.right)
)
```

This is the heart of the algorithm.

---

# What This Means Conceptually

We are saying:

```txt id="luwq5n"
Current depth =
1 (current node)
+
deepest child subtree
```

---

# Why `max()` Is Correct

Because the problem asks for:

```txt id="0ih7gl"
LONGEST path
```

So we choose:

- deeper subtree

NOT both.

---

# Why `+1` Exists

The recursive calls compute:

```txt id="tmx2pz"
child subtree depth
```

But current node itself must also count.

So:

```txt id="1p0k0t"
+1 for current node
```

---

# The Most Important Mental Model

This problem teaches:

```txt id="u1g71o"
A node asks its children for information,
then combines their answers.
```

That is recursive aggregation.

This is fundamentally different from:

- Same Tree
- Invert Tree

Those problems were:

- traversal-oriented

This problem is:

- information-return-oriented

Huge conceptual shift.

---

# Visual Recursive Execution

Tree:

```txt id="cb7qmi"
        3
       / \
      9   20
         /  \
        15   7
```

---

# Step 1 — Start at Root

```python id="uhk8x7"
maxDepth(3)
```

Cannot compute immediately.

Needs:

- left depth
- right depth

So recurse.

---

# Step 2 — Left Subtree

```python id="9j8wsf"
maxDepth(9)
```

Node `9` is leaf.

Children:

```python id="bh9lzy"
maxDepth(None) → 0
maxDepth(None) → 0
```

So:

1 + \max(0,0)=1

Return:

```python id="3k29md"
1
```

---

# Step 3 — Right Subtree

```python id="49f8ux"
maxDepth(20)
```

Needs:

- depth(15)
- depth(7)

Each leaf returns:

```txt id="1bgvc5"
1
```

So node `20` computes:

1 + \max(1,1)=2

Return:

```python id="8wkxj5"
2
```

---

# Step 4 — Root Combines Results

Root receives:

```txt id="4przff"
left = 1
right = 2
```

So:

1 + \max(1,2)=3

Final answer:

```python id="9zv4n4"
3
```

---

# Why This Is Postorder DFS

Notice execution order:

```txt id="1srr40"
1. solve left subtree
2. solve right subtree
3. compute current node
```

Current node depends on children first.

That is:

> postorder reasoning

Very important tree pattern.

---

# Understanding Your BFS Solution (`maxDepth2`)

Now let’s analyze the BFS version conceptually.

---

# Core BFS Idea

Instead of asking:

```txt id="nghnpt"
“What is subtree depth?”
```

BFS asks:

```txt id="n2bplc"
“How many levels exist?”
```

---

# Important Mental Difference

## DFS Version

Recursive aggregation:

```txt id="m5e1rm"
depth(node)
```

---

## BFS Version

Level-by-level traversal:

```txt id="mjlwm3"
count levels visited
```

Completely different thinking model.

---

# BFS Flow

```python id="s8w8gi"
level = 0
stack = [root]
```

This queue/list stores:

- current frontier (current level)

---

# Core BFS Loop

```python id="mdrku4"
while stack:
```

Means:

```txt id="yq2mfw"
“As long as another level exists”
```

---

# Why `for range(len(stack))` Exists

Critical BFS pattern.

```python id="r0ue49"
for i in range(len(stack)):
```

This freezes:

- current level size

Without this:

- newly added children would mix into same level

This is the most important BFS level-order technique.

---

# DFS Iterative Version (`maxDepth`)

Now your third solution.

---

# Core Idea

Simulate recursion manually using a stack.

---

# Important Insight

Recursive DFS internally uses:

- call stack

This solution makes it explicit.

---

# Stack Contents

```python id="hn0g9n"
[node, depth]
```

Each stack item stores:

- current node
- current depth

Because iterative DFS does not naturally remember recursion depth.

---

# Key Difference vs Recursive DFS

Recursive DFS:

```txt id="64l50n"
Python call stack stores depth implicitly
```

Iterative DFS:

```txt id="y5pzn0"
YOU must store depth manually
```

Very important understanding.

---

# Comparing The Three Solutions

| Solution      | Mental Model                | Main DS        |
| ------------- | --------------------------- | -------------- |
| Recursive DFS | subtree aggregation         | call stack     |
| BFS           | level counting              | queue          |
| Iterative DFS | manual recursion simulation | explicit stack |

---

# Which One Matters Most Here?

For learning Trees:

> the recursive DFS solution is the MOST important

Because it teaches:

- recursive decomposition
- subtree aggregation
- postorder reasoning

Core tree fundamentals.

---

# Time Complexity

All solutions visit every node once:

```txt id="ejvb2s"
O(n)
```

---

# Space Complexity

## Recursive DFS

```txt id="3gkmfu"
O(h)
```

Where:

- `h` = tree height

---

## BFS

Worst case:

```txt id="jlwm9m"
O(w)
```

Where:

- `w` = maximum tree width

---

# Pattern Extraction

| Component         | Meaning                                 |
| ----------------- | --------------------------------------- |
| Trigger           | Current answer depends on child answers |
| Pattern           | Recursive DFS Aggregation               |
| Structure         | Postorder traversal                     |
| Core Operation    | combine child depths                    |
| Recursive Meaning | “Return subtree depth”                  |

---

# Final Mental Model

This problem is fundamentally:

```txt id="7q4mk4"
Tree depth =
1 +
deepest subtree depth
```

That recursive equation is one of the most important ideas in tree algorithms.
