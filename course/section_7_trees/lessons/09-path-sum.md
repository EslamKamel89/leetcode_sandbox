# Problem Classification

| Question       | Answer                             |
| -------------- | ---------------------------------- |
| Pattern        | Path-Based DFS                     |
| Traversal Type | DFS Recursive                      |
| Core Skill     | Carry state along recursive path   |
| Key Insight    | Pass accumulated path sum downward |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Does ANY root-to-leaf path sum equal targetSum?”

Important:

```txt id="jlwma1"
ROOT → LEAF
```

NOT:

- any arbitrary path
- any subtree
- any two nodes

The path must:

- start at root
- end at a leaf

---

# Visual Example

Tree:

```txt id="jlwmb2"
           5
         /   \
        4     8
       /     / \
      11    13  4
     /  \         \
    7    2         1
```

Target:

```txt id="jlwmc3"
22
```

Valid path:

```txt id="jlwmd4"
5 → 4 → 11 → 2
```

Sum:

5+4+11+2=22

So answer:

```python id="jlwme5"
True
```

---

# The Most Important Insight

This problem is NOT about:

- subtree aggregation
- combining child answers numerically

Instead, this is:

```txt id="jlwmf6"
state propagation along a path
```

That is a major pattern shift.

---

# Compare With Previous Problems

## Maximum Depth

Children RETURN information upward.

```txt id="jlwmg7"
bottom-up recursion
```

---

## Path Sum

Parent SENDS information downward.

```txt id="jlwmh8"
top-down recursion
```

Huge conceptual difference.

---

# Step 2 — Pattern Recognition

This problem has strong path-based DFS signals.

---

# Signal 1 — “Root-to-leaf path”

Immediate DFS indicator.

DFS naturally explores:

- full paths deeply

---

# Signal 2 — “Path sum”

We must accumulate information while moving downward.

That suggests:

- state carried through recursion

---

# Signal 3 — “Any valid path”

This suggests:

- branching search

DFS explores:

- one path at a time

Perfect fit.

---

# Step 3 — Define The Recursive Meaning

Define:

```python id="jlwmi9"
dfs(node, curr_sum)
```

means:

```txt id="jlwmja"
“We are currently standing at this node,
and curr_sum is the sum accumulated so far.”
```

This recursive meaning is EVERYTHING.

---

# Important Mental Model

The recursion carries:

- path state

downward through the tree.

---

# Visualize State Flow

Example:

```txt id="jlwmkb"
5 → 4 → 11
```

State evolves:

| Node | curr_sum |
| ---- | -------- |
| 5    | 5        |
| 4    | 9        |
| 11   | 20       |

The recursive calls transport:

- path information

---

# Step 4 — Build The Solution Gradually

---

# Base Case — Empty Node

```python id="jlwmlc"
if not root:
    return False
```

---

# Why Return False?

An empty path:

- cannot satisfy root-to-leaf requirement

No valid path exists here.

---

# Important Difference From Other Problems

In:

- Maximum Depth
- Balanced Tree

`None` contributed useful structural information.

Here:

```txt id="jlwmmd"
None does NOT represent a valid path
```

So return:

```python id="jlwmne"
False
```

---

# Update Running Sum

```python id="jlwmof"
curr_sum += root.val
```

---

# What This Means

We are extending the current path.

Suppose:

```txt id="jlwmpg"
Current path:
5 → 4
```

Current sum:

5+4=9

Moving to node `11`:

9+11=20

The state evolves as recursion descends.

---

# Leaf Node Check

```python id="jlwmqh"
if not root.left and not root.right:
```

This identifies:

- leaf node

---

# Why Leaf Check Is Critical

The problem specifically requires:

```txt id="jlwmri"
ROOT → LEAF
```

Suppose we stop early:

```txt id="jlwmsj"
5 → 4 → 11
```

Even if sum matched:

- not valid yet

Because `11` is not leaf.

Huge detail.

---

# Final Leaf Validation

```python id="jlwmtk"
return curr_sum == targetSum
```

At leaf:

- check if full path sum matches target

---

# Recursive Exploration

```python id="jlwmul"
return (
    dfs(root.left, curr_sum)
    or
    dfs(root.right, curr_sum)
)
```

---

# What This Means

We explore:

- left path
- right path

If EITHER succeeds:

- valid solution exists

---

# Why `or` Is Correct

We only need:

```txt id="jlwmvm"
ONE valid path
```

NOT all paths.

So:

- any successful branch returns True

---

# Visual Recursive Walkthrough

Tree:

```txt id="jlwmwn"
           5
         /   \
        4     8
       /     / \
      11    13  4
     /  \         \
    7    2         1
```

Target:

```txt id="jlwmxo"
22
```

---

# STEP 1 — Start At Root

```python id="jlwmyp"
dfs(5, 0)
```

Update sum:

0+5=5

---

# STEP 2 — Go Left

```python id="jlwmzq"
dfs(4, 5)
```

Update:

5+4=9

---

# STEP 3 — Go Left Again

```python id="jlwn0r"
dfs(11, 9)
```

Update:

9+11=20

---

# STEP 4 — Explore Left Child

```python id="jlwn1s"
dfs(7, 20)
```

Update:

20+7=27

Leaf reached.

Check:

```txt id="jlwn2t"
27 == 22 ?
```

False.

Backtrack.

---

# STEP 5 — Explore Right Child

```python id="jlwn3u"
dfs(2, 20)
```

Update:

20+2=22

Leaf reached.

Check:

```txt id="jlwn4v"
22 == 22
```

True.

---

# Recursive Collapse

Now:

```python id="jlwn5w"
True OR anything
```

becomes:

```python id="jlwn6x"
True
```

The success propagates upward.

---

# Full Path Visualization

```txt id="jlwn7y"
5
↓
4   sum=9
↓
11  sum=20
↓
2   sum=22 ✓
```

---

# Why This Problem Is Important

This problem introduces:

```txt id="jlwn8z"
top-down recursive state propagation
```

That is foundational for:

- backtracking
- path problems
- recursive search
- graph DFS

---

# Compare With Bottom-Up Recursion

## Bottom-Up Problems

Examples:

- Maximum Depth
- Balanced Tree
- Diameter

Children return information upward.

---

## Top-Down Problems

Example:

- Path Sum

Parent sends state downward.

---

# Deep Recursive Insight

This problem teaches:

```txt id="jlwn90"
Recursive calls can CARRY state,
not only COMPUTE state.
```

Huge distinction.

---

# Why This Is DFS

DFS naturally:

- follows complete paths deeply
- backtracks after dead ends

Exactly what this problem needs.

---

# Time Complexity

Every node visited at most once:

```txt id="jlwna1"
O(n)
```

---

# Space Complexity

Recursive stack depth:

```txt id="jlwnb2"
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

| Component         | Meaning                          |
| ----------------- | -------------------------------- |
| Trigger           | Root-to-leaf path search         |
| Pattern           | Path-Based DFS                   |
| Structure         | Carry accumulated state downward |
| Core Operation    | running path sum                 |
| Recursive Meaning | “Current path sum so far”        |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlwnc3"
Walk down every root-to-leaf path,
while carrying the running sum.
```

If ANY leaf finishes with:

- sum == target

then the tree contains a valid path.
