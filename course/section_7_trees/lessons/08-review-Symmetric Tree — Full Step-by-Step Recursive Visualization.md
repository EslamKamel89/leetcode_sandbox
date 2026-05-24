# Symmetric Tree — Full Step-by-Step Recursive Visualization

This problem is one of the most important upgrades in recursive tree thinking.

Why?

Because this is the first major problem where recursion becomes:

```txt id="m91l1f"
GEOMETRIC
```

You are no longer comparing:

- same positions

You are comparing:

- mirrored positions

The attached explanation already establishes the recursive mirror logic and conceptual structure.

Now we’ll make the execution completely visible step-by-step.

---

# The Core Problem

We must determine:

```txt id="2fc9rm"
Is the tree mirrored around its center?
```

---

# Important Mental Shift

This is NOT:

```txt id="0v2tgi"
“Are the left and right subtrees equal?”
```

This IS:

```txt id="npjlwm"
“Are the left and right subtrees MIRRORS?”
```

Huge difference.

---

# Visualize Mirror Symmetry

Symmetric tree:

```txt id="jlwmv9"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

Mirror pairs:

| Left Side | Right Side |
| --------- | ---------- |
| 2         | 2          |
| 3         | 3          |
| 4         | 4          |

But structurally:

```txt id="jlwmu8"
left.left  ↔ right.right
left.right ↔ right.left
```

NOT:

- left.left ↔ right.left

This is the heart of the problem.

---

# The Solution

```python id="jlwmt7"
def dfs(left, right):

    if not left and not right:
        return True

    if not left or not right:
        return False

    return (
        left.val == right.val
        and dfs(left.left, right.right)
        and dfs(left.right, right.left)
    )
```

---

# The Most Important Recursive Definition

Define:

```python id="jlwms6"
dfs(left, right)
```

means:

```txt id="jlwmr5"
“Are these two subtrees mirror images?”
```

This recursive meaning drives everything.

---

# Visual Execution Walkthrough

We’ll trace:

```txt id="jlwmq4"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

---

# STEP 1 — Initial Call

```python id="jlwmp3"
dfs(root.left, root.right)
```

Meaning:

```python id="jlwmo2"
dfs(2, 2)
```

---

# Why We Start Here

The root itself does not need comparison.

A tree is symmetric if:

- left subtree mirrors right subtree

So we compare:

- root.left
- root.right

---

# STEP 2 — Compare Current Nodes

Current nodes:

```txt id="jlwmn1"
2 ↔ 2
```

Values match.

Good so far.

But symmetry also requires:

- mirrored children

So recursion continues.

---

# The Two Mirror Checks

This is the MOST important part.

---

# Outer Mirror

```python id="jlwmm0"
dfs(left.left, right.right)
```

Meaning:

```python id="jlwml9"
dfs(3, 3)
```

---

# Why Outer?

Visualize:

```txt id="jlwmk8"
          1
        /   \
       2     2
      /       \
     3         3
```

These are outer mirror positions.

---

# Inner Mirror

```python id="jlwmj7"
dfs(left.right, right.left)
```

Meaning:

```python id="jlwmi6"
dfs(4, 4)
```

---

# Why Inner?

Visualize:

```txt id="jlwmh5"
          1
        /   \
       2     2
        \   /
         4 4
```

These are inner mirror positions.

---

# This Is The Entire Mirror Geometry

At every node:

```txt id="jlwmg4"
outside ↔ outside
inside ↔ inside
```

That is exactly what recursion encodes.

---

# STEP 3 — Process Outer Pair (3,3)

Call:

```python id="jlwmf3"
dfs(3, 3)
```

Values match.

Now recurse again.

---

# Outer Children

```python id="jlwme2"
dfs(None, None)
```

Returns:

```python id="jlwmd1"
True
```

---

# Why?

Both sides ended simultaneously.

Perfect mirror.

---

# Inner Children

```python id="jlwmc0"
dfs(None, None)
```

Again:

```python id="jlwmb9"
True
```

---

# Result For Node Pair (3,3)

All conditions succeeded.

So:

```python id="jlwma8"
True
```

returns upward.

---

# STEP 4 — Process Inner Pair (4,4)

Exactly same logic.

---

# Compare Values

```txt id="jlwm97"
4 ↔ 4
```

Good.

---

# Children

All are:

```txt id="jlwm86"
None ↔ None
```

So recursion succeeds.

Returns:

```python id="jlwm75"
True
```

---

# STEP 5 — Final Combination At (2,2)

Now original call receives:

```txt id="jlwm64"
outer mirror = True
inner mirror = True
```

And current values matched.

So:

```python id="jlwm53"
True
```

returns upward.

---

# FINAL ANSWER

Tree is symmetric:

```python id="jlwm42"
True
```

---

# Complete Recursive Flow Visualization

```txt id="jlwm31"
dfs(2,2)
│
├── dfs(3,3)
│     ├── dfs(None,None) → True
│     └── dfs(None,None) → True
│
└── dfs(4,4)
      ├── dfs(None,None) → True
      └── dfs(None,None) → True
```

Everything mirrors correctly.

---

# Now Let’s Visualize Failure

Non-symmetric tree:

```txt id="jlwm20"
          1
        /   \
       2     2
        \     \
         3     3
```

---

# Initial Call

```python id="jlwm19"
dfs(2,2)
```

Values match.

---

# Outer Mirror Check

```python id="jlwm08"
dfs(None, 3)
```

Now:

```txt id="jlvmyz"
left missing
right exists
```

Mirror broken immediately.

Returns:

```python id="jlvmxy"
False
```

Whole recursion collapses to:

```python id="jlvmwx"
False
```

---

# Why This Problem Is Deeply Important

This problem teaches:

```txt id="jlvmvw"
recursive geometry
```

The recursion itself follows:

- the mirror structure of the tree

This is a major recursive thinking upgrade.

---

# Compare With Same Tree

# Same Tree

Recursive structure:

```txt id="jlvmuv"
left ↔ left
right ↔ right
```

---

# Symmetric Tree

Recursive structure:

```txt id="jlvmtu"
left ↔ right
right ↔ left
```

Cross-recursion.

That is the conceptual leap.

---

# Why This Is DFS

The recursion:

- explores mirrored branches deeply
- backtracks after subtree validation

Classic DFS traversal.

---

# Important Execution Order

At every recursive step:

```txt id="jlvmst"
1. Compare current mirrored nodes
2. Explore outer mirror
3. Explore inner mirror
```

This repeats recursively.

---

# Common Beginner Mistake

Beginners often write:

```python id="jlvmrs"
dfs(left.left, right.left)
```

This is WRONG.

Why?

Because that compares:

- same-side positions

NOT:

- mirrored positions

Mirror comparison must CROSS directions.

---

# Deep Mental Compression

This problem fundamentally says:

```txt id="jlvmqr"
A tree is symmetric if:
the left subtree is a mirror reflection
of the right subtree.
```

And recursion recursively validates that mirror relationship.

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlvmpq"
Mirror(nodeA, nodeB) =
same value
+
outer children mirror
+
inner children mirror
```

Where recursion itself follows the visual symmetry of the tree.
