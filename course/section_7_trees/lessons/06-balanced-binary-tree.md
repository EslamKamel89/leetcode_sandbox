# Problem Classification

| Question       | Answer                                                  |
| -------------- | ------------------------------------------------------- |
| Pattern        | Tree Height / Depth                                     |
| Traversal Type | DFS Recursive (Postorder)                               |
| Core Skill     | Multi-value recursive aggregation                       |
| Key Insight    | Each subtree must return BOTH balance status and height |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Is the tree height-balanced?”

But what does balanced actually mean?

---

# Balanced Tree Definition

A tree is balanced if:

```txt id="02u29w"
For EVERY node:
|left height - right height| <= 1
```

Meaning:

- left subtree height
- right subtree height

must not differ by more than 1.

---

# Visual Example — Balanced

```txt id="gg0r33"
        3
       / \
      9   20
         /  \
        15   7
```

Heights stay close.

Every node satisfies:

|h*{left} - h*{right}| \leq 1

So result:

```python id="n6e01v"
True
```

---

# Visual Example — Unbalanced

```txt id="xjlwmf"
        1
       /
      2
     /
    3
   /
  4
```

At root:

```txt id="6jlwmz"
left height = 3
right height = 0
```

Difference:

|3 - 0| = 3

Too large.

So:

```python id="jlwmx9"
False
```

---

# Step 2 — The Most Important Insight

This is NOT just a traversal problem anymore.

This is:

> recursive information aggregation

The node needs information from children before it can decide anything.

---

# What Information Does A Node Need?

Suppose we're at this node:

```txt id="g75v10"
        A
       / \
      B   C
```

To know if `A` is balanced,
we must know:

---

## Information Needed From Left Subtree

```txt id="jlwmc8"
1. Is left subtree balanced?
2. What is left subtree height?
```

---

## Information Needed From Right Subtree

```txt id="jlwmk2"
1. Is right subtree balanced?
2. What is right subtree height?
```

---

# This Is The Core Difficulty

One recursive call must return:

- multiple pieces of information

That is the major progression from Maximum Depth.

---

# Compare With Maximum Depth

## Maximum Depth Returned:

```txt id="jlwmh5"
ONLY height
```

---

## Balanced Tree Returns:

```txt id="jlwmtp"
balance status + height
```

This is a major recursion upgrade.

---

# Step 3 — Define The Recursive Meaning

This is the most important step.

Define:

```python id="jlwmq7"
dfs(node)
```

means:

> “Return whether this subtree is balanced AND its height.”

That is why we return:

```python id="jlwmn6"
[balanced, height]
```

---

# Step 4 — Build The Solution Gradually

---

# Base Case

```python id="jlwma4"
if not root:
    return [True, 0]
```

---

# What This Means

An empty tree is:

- balanced
- height 0

So:

```python id="jlwmw2"
[True, 0]
```

---

# Why Returning `True` Matters

Suppose leaf node:

```txt id="jlwmv3"
    7
```

Its children are:

- None
- None

Each child returns:

```python id="jlwmu9"
[True, 0]
```

Then leaf node can correctly compute:

- balanced
- height

Without this base case recursion breaks.

---

# Recursive Calls

```python id="jlwmt8"
left, right = dfs(root.left), dfs(root.right)
```

This recursively gathers information from children.

---

# Important Mental Model

This is NOT:

```txt id="jlsm1r"
“Go visit children.”
```

This IS:

```txt id="jlwms1"
“Ask children for subtree information.”
```

Huge conceptual difference.

---

# What Does `left` Contain?

Example:

```python id="jlwmr2"
left = [True, 3]
```

Meaning:

```txt id="jlwmp0"
Left subtree:
- IS balanced
- height = 3
```

---

# Computing Balance

```python id="jlwmo9"
balanced = (
    left[0]
    and
    right[0]
    and
    abs(left[1] - right[1]) <= 1
)
```

This is the heart of the algorithm.

---

# Break It Into Pieces

---

# Condition 1

```python id="jlsm2k"
left[0]
```

Left subtree itself must already be balanced.

---

# Condition 2

```python id="jlsm3v"
right[0]
```

Right subtree itself must already be balanced.

---

# Condition 3

```python id="jlsm4f"
abs(left[1] - right[1]) <= 1
```

Current node height difference must also be valid.

---

# This Is Extremely Important

Balance is NOT only local.

A node is balanced ONLY IF:

```txt id="jlsm5d"
children balanced
+
current height difference valid
```

---

# Computing Height

```python id="jlsm6s"
1 + max(left[1], right[1])
```

Same recursive equation from Maximum Depth.

height = 1 + \max(h*{left}, h*{right})

---

# Return Statement

```python id="jlsm7q"
return [balanced, height]
```

This sends subtree information upward to parent.

---

# Visual Recursive Walkthrough

Tree:

```txt id="jlsm8y"
        3
       / \
      9   20
         /  \
        15   7
```

---

# Step 1 — Leaf Nodes

Leaves:

- 9
- 15
- 7

Each computes:

height = 1 + \max(0,0)=1

Each returns:

```python id="jlsm9n"
[True, 1]
```

---

# Step 2 — Node 20

Receives:

```python id="jlsma1"
left  = [True, 1]
right = [True, 1]
```

Check:

|1-1|=0 \leq 1

Balanced.

Height:

1 + \max(1,1)=2

Returns:

```python id="jlsmb2"
[True, 2]
```

---

# Step 3 — Root Node 3

Receives:

```python id="jlsmc3"
left  = [True, 1]
right = [True, 2]
```

Check:

|1-2|=1 \leq 1

Balanced.

Height:

1 + \max(1,2)=3

Returns:

```python id="jlsmd4"
[True, 3]
```

Final answer:

```python id="jlsme5"
True
```

---

# Why This Is Postorder DFS

Execution order:

```txt id="jlsmf6"
1. Solve left subtree
2. Solve right subtree
3. Compute current node
```

The current node depends on child information first.

That is:

> postorder recursion

---

# The Deep Recursion Insight

This problem teaches a HUGE concept:

> recursive calls can return structured information

Not just:

- single numbers
- booleans

But:

- tuples
- multiple states
- aggregated subtree data

This is foundational for:

- diameter
- max path sum
- tree DP
- advanced recursion

---

# Why This Problem Is A Major Milestone

This is where tree recursion becomes:

> real recursive problem solving

You now understand:

- recursive information flow
- subtree aggregation
- local + global conditions

This is much more advanced than:

- Same Tree
- Invert Tree
- Maximum Depth

---

# Time Complexity

Every node visited once:

```txt id="jlsmg7"
O(n)
```

---

# Space Complexity

Recursive stack depth:

```txt id="jlsmh8"
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

| Component         | Meaning                                    |
| ----------------- | ------------------------------------------ |
| Trigger           | Parent depends on subtree information      |
| Pattern           | Postorder DFS Aggregation                  |
| Structure         | Return multiple subtree states             |
| Core Operation    | combine child balance + heights            |
| Recursive Meaning | “Return balance status and subtree height” |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlsmi9"
Balanced subtree =
left balanced
AND
right balanced
AND
heights differ by at most 1
```

Where subtree heights are recursively computed bottom-up.
