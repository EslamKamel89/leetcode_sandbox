# Problem Classification

| Question       | Answer                                                                  |
| -------------- | ----------------------------------------------------------------------- |
| Pattern        | BST Properties                                                          |
| Traversal Type | BST Guided Traversal                                                    |
| Core Skill     | Using BST ordering to eliminate half the tree                           |
| Key Insight    | The LCA is the first node where p and q split into different directions |

---

# Step 1 — Understand The Real Problem

Before thinking about BSTs, we need to understand:

```txt
What is a Lowest Common Ancestor (LCA)?
```

---

# Visual Example

```txt
            6
          /   \
         2     8
        / \
       0   4
          / \
         3   5
```

Suppose:

```txt
p = 2
q = 8
```

---

# Ancestors Of 2

```txt
2
6
```

---

# Ancestors Of 8

```txt
8
6
```

---

# Common Ancestors

```txt
6
```

Answer:

```txt
6
```

---

# Why "Lowest"?

Imagine:

```txt
            6
          /   \
         2     8
        / \
       0   4
          / \
         3   5
```

Suppose:

```txt
p = 3
q = 5
```

Common ancestors:

```txt
4
2
6
```

Lowest means:

```txt
closest to the nodes
```

So answer:

```txt
4
```

not:

```txt
6
```

---

# The Most Important Observation

Forget BST for a moment.

Look at:

```txt
            6
          /   \
         2     8
        / \
       0   4
          / \
         3   5
```

Suppose:

```txt
p = 2
q = 8
```

At node `6`:

```txt
p is on left side
q is on right side
```

Interesting.

---

# Why Is That Important?

Because:

```txt
6 is exactly where the paths split
```

---

Visualize:

```txt
            6
          /   \
         2     8
```

To reach:

- 2 → go left
- 8 → go right

So:

```txt
6 is the first divergence point
```

That is the LCA.

---

# The Core Insight

The LCA is:

```txt
The first node where
p and q stop going in the same direction.
```

This single idea solves the whole problem.

---

# Step 2 — Now Use The BST Property

Remember:

```txt
left subtree  < node
right subtree > node
```

This allows us to know:

```txt
which direction p and q must be
```

without searching the entire tree.

---

# Example

Current node:

```txt
6
```

Suppose:

```txt
p = 2
q = 4
```

---

Check:

```txt
2 < 6
4 < 6
```

Both are smaller.

Therefore:

```txt
Both nodes MUST be in left subtree
```

So we can safely ignore:

```txt
entire right subtree
```

Huge optimization.

---

# Visual

```txt
            6
          /   \
         2     8
```

Both targets:

```txt
2
4
```

are left of 6.

Therefore:

```txt
move left
```

---

# This Is The Whole Strategy

At each node ask:

```txt
Where are p and q relative to me?
```

There are only three possibilities.

---

# Case 1 — Both On Left

```python
p.val < curr.val
q.val < curr.val
```

Visualization:

```txt
            curr
           /
         p,q
```

Meaning:

```txt
LCA cannot be current node
```

because both nodes are deeper on left side.

Move:

```python
curr = curr.left
```

---

# Case 2 — Both On Right

```python
p.val > curr.val
q.val > curr.val
```

Visualization:

```txt
            curr
                 \
                 p,q
```

Again:

```txt
LCA must be deeper
```

Move:

```python
curr = curr.right
```

---

# Case 3 — Split Happens

Example:

```txt
p < curr
q > curr
```

Visualization:

```txt
              curr
             /    \
            p      q
```

This means:

```txt
current node is exactly where paths diverge
```

Therefore:

```txt
current node is LCA
```

Return it immediately.

---

# Special Case

Suppose:

```txt
curr = 2
p = 2
q = 4
```

At node 2:

```txt
p == curr
```

One target is current node itself.

Remember the definition:

```txt
A node can be a descendant of itself.
```

So:

```txt
2 is LCA
```

This is why the solution's final `else` works perfectly.

---

# Step 3 — Walk Through Example 1

Tree:

```txt
            6
          /   \
         2     8
        / \
       0   4
```

Find:

```txt
p = 2
q = 8
```

---

# Iteration 1

Current:

```txt
curr = 6
```

Check:

```txt
2 < 6
8 > 6
```

They split.

Visualization:

```txt
            6
          /   \
         2     8
```

Return:

```txt
6
```

Done.

---

# Step 4 — Walk Through Example 2

Tree:

```txt
            6
          /   \
         2     8
        / \
       0   4
```

Find:

```txt
p = 2
q = 4
```

---

# Iteration 1

Current:

```txt
6
```

Check:

```txt
2 < 6
4 < 6
```

Both left.

Move:

```python
curr = curr.left
```

---

# Iteration 2

Current:

```txt
2
```

Check:

```txt
p = 2
q = 4
```

Neither:

```txt
both left
```

nor

```txt
both right
```

is true.

Therefore:

```txt
split condition reached
```

Return:

```txt
2
```

Done.

---

# Why This Problem Is Different From Previous BST Problems

Let's compare.

---

# Validate BST

Used BST property to verify:

```txt
ordering constraints
```

---

# Kth Smallest

Used BST property:

```txt
inorder traversal is sorted
```

---

# LCA In BST

Uses BST property for:

```txt
navigation
```

You don't need:

- recursion
- full traversal
- visiting every node

You simply follow the correct direction.

---

# Why Iterative Solution Works So Well

Notice:

```python
while curr:
```

We never revisit nodes.

At each step:

```txt
discard half of the search space
```

Exactly like Binary Search.

This is why BSTs are powerful.

---

# Visual Mental Model

Think of each node asking:

```txt
Are both targets left of me?
→ go left

Are both targets right of me?
→ go right

Otherwise:
→ I'm the split point
→ I'm the LCA
```

---

# Time Complexity

Let:

```txt
h = tree height
```

We only move downward.

Time:

```txt
O(h)
```

---

Balanced BST:

```txt
O(log n)
```

---

Worst-case skewed BST:

```txt
O(n)
```

---

# Space Complexity

Iterative solution:

```txt
O(1)
```

No recursion stack.

---

# Pattern Extraction

| Component        | Meaning                              |
| ---------------- | ------------------------------------ |
| Trigger          | BST + ancestor/relationship problem  |
| Pattern          | BST Guided Traversal                 |
| Structure        | Use BST ordering to choose direction |
| Core Observation | LCA is first split point             |
| Decision Rule    | Both left, both right, or split      |

---

# Final Mental Model

This problem is fundamentally:

```txt
Walk downward from the root.

As long as both nodes lie on the same side,
keep moving toward them.

The first node where they no longer lie on
the same side is exactly where their paths
separate.

That split point is the Lowest Common Ancestor.
```

This is one of the cleanest examples of exploiting BST structure instead of performing a full tree traversal.
