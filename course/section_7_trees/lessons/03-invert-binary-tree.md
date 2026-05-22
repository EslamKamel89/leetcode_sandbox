# Problem Classification

| Question       | Answer                        |
| -------------- | ----------------------------- |
| Pattern        | Basic DFS Traversal           |
| Traversal Type | DFS Recursive                 |
| Core Skill     | Recursive tree transformation |
| Key Insight    | Swap children at every node   |

---

# Step 1 — Understand The Real Problem

At first glance, this looks like:

> “Reverse a tree.”

But conceptually, the real operation is:

> “For every node, swap its left and right children.”

That is the ENTIRE problem.

---

# Visual Meaning of Inversion

Original:

```txt id="56u7x2"
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

After inversion:

```txt id="xk2lqq"
        4
      /   \
     7     2
    / \   / \
   9   6 3   1
```

Notice:

```txt id="m4z9gd"
Every node swaps:
left ↔ right
```

This is a recursive structural transformation.

---

# Step 2 — Pattern Recognition

This problem has strong DFS recursive signals.

---

## Signal 1 — Entire tree must be modified

We must visit:

- every node

That implies traversal.

---

## Signal 2 — Same operation repeated everywhere

At every node we do:

```txt id="4k0k1x"
swap children
```

Repeated recursive operations are classic DFS recursion.

---

## Signal 3 — Subtree independence

The inversion of:

- left subtree
- right subtree

are independent operations.

Huge recursive indicator.

---

# Step 3 — Define The Recursive Meaning

This is the most important step.

Define:

```python id="m4h6bi"
invertTree(node)
```

means:

> “Invert the entire subtree rooted at node.”

This definition drives the whole solution.

---

# Step 4 — Build The Solution Gradually

---

# Base Case — Empty Node

```python id="u4qms9"
if not root:
    return None
```

---

## What This Means

An empty subtree:

```txt id="8l9oqj"
None
```

is already inverted.

Nothing to process.

---

## Why This Is Necessary

Without it:

- recursion never stops
- accessing children crashes

This is recursion termination.

---

# Core Operation — Swap Children

```python id="nux0xr"
root.right, root.left = root.left, root.right
```

This is the heart of the algorithm.

---

# What This Actually Does

Before:

```txt id="l59o0m"
    4
   / \
  2   7
```

After swap:

```txt id="zdz9g8"
    4
   / \
  7   2
```

Only the immediate children are swapped.

---

# Important Insight

This line does NOT invert the whole tree.

It only fixes:

> the current node

We still must recursively fix:

- left subtree
- right subtree

---

# Recursive Processing

```python id="h5jn7o"
self.invertTree(root.right)
self.invertTree(root.left)
```

Now we recursively apply the SAME operation to:

- both subtrees

This is the recursive decomposition.

---

# Important Subtle Point

Notice:

```python id="trm9gw"
swap first
then recurse
```

Why?

Because after swapping:

- the old left subtree becomes right
- the old right subtree becomes left

So recursion naturally continues on the swapped structure.

---

# What Happens If We Remove Recursion?

Suppose we only do:

```python id="r0mpc2"
root.right, root.left = root.left, root.right
```

Then only ONE node gets inverted.

Example:

Before:

```txt id="k0h80r"
        4
      /   \
     2     7
    / \
   1   3
```

After swapping root only:

```txt id="5v5u7n"
        4
      /   \
     7     2
        / \
       1   3
```

Notice:

- subtree under `2` is NOT inverted yet.

That is why recursion is necessary.

---

# Return Statement

```python id="xjxwdn"
return root
```

---

# Why Return Root?

Because:

- LeetCode expects the modified tree root
- inversion happens in-place

The structure itself changes.

---

# Visual Execution Walkthrough

Input:

```txt id="z8pl5l"
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

---

# Step 1 — Process Node 4

Swap:

```txt id="23h8zc"
        4
      /   \
     7     2
```

Now recurse into:

- subtree 7
- subtree 2

---

# Step 2 — Process Node 7

Before:

```txt id="z94c4w"
    7
   / \
  6   9
```

After swap:

```txt id="6m3f5r"
    7
   / \
  9   6
```

---

# Step 3 — Process Node 2

Before:

```txt id="0qq35k"
    2
   / \
  1   3
```

After swap:

```txt id="uh0y4v"
    2
   / \
  3   1
```

Final result:

```txt id="tykntc"
        4
      /   \
     7     2
    / \   / \
   9   6 3   1
```

---

# Why This Problem Is Important

This problem upgrades your tree understanding significantly.

---

# Same Tree vs Invert Tree

## Same Tree

Recursive comparison:

- observational recursion

```txt id="z2m86z"
“Do these subtrees match?”
```

---

## Invert Tree

Recursive transformation:

- mutating recursion

```txt id="7jlwmk"
“Modify these subtrees.”
```

This is a major conceptual progression.

---

# Core Mental Shift

You now learn:

> DFS is not only for reading trees.

It is also for:

- transforming
- rebuilding
- mutating structures

Very important.

---

# Traversal Order Insight

This solution is effectively:

```txt id="i8wzbo"
process current node
then recurse
```

That resembles:

- preorder DFS

because work happens BEFORE recursive descent.

---

# Time Complexity

Every node visited once:

```txt id="g17izt"
O(n)
```

---

# Space Complexity

Recursive stack depth:

```txt id="w2fw33"
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
| Trigger           | Same operation on every subtree  |
| Pattern           | DFS Recursive Traversal          |
| Structure         | Recursive subtree transformation |
| Core Operation    | Swap children                    |
| Recursive Meaning | “Invert subtree rooted at node”  |

---

# Final Mental Model

This problem is fundamentally:

```txt id="75q2q1"
Invert tree =
swap current children
+
recursively invert subtrees
```

That is recursive structural transformation.
