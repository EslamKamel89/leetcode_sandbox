# Problem Classification

| Question       | Answer                                                                |
| -------------- | --------------------------------------------------------------------- |
| Pattern        | BST Properties                                                        |
| Traversal Type | DFS Recursive                                                         |
| Core Skill     | Propagating valid value ranges                                        |
| Key Insight    | Every node must satisfy ALL ancestor constraints, not just its parent |

---

# Step 1 — Understand The Real Problem

At first glance, the BST rule seems simple:

```txt id="bst11"
left < node
right > node
```

Many beginners stop here.

That is the biggest trap in this problem.

---

# Why The Obvious Solution Fails

Consider:

```txt id="bst22"
        5
       / \
      1   4
         / \
        3   6
```

This is the famous invalid example.

---

# Let's Check Parent Relationships

Node `4`:

```txt id="bst33"
4 < 5
```

Good.

---

Node `3`:

```txt id="bst44"
3 < 4
```

Good.

---

Node `6`:

```txt id="bst55"
6 > 4
```

Good.

---

Everything seems correct.

Yet the answer is:

```python id="bst66"
False
```

Why?

---

# The Hidden Rule

Node `3` is inside the RIGHT subtree of `5`.

Therefore:

```txt id="bst77"
3 must be > 5
```

But:

```txt id="bst88"
3 < 5
```

Violation.

---

# The Most Important Insight

BST validation is NOT about:

```txt id="bst99"
parent-child relationships
```

It is about:

```txt id="bsta00"
ancestor constraints
```

This is the entire problem.

---

# Visualizing The Real Rule

Suppose:

```txt id="bsta11"
        10
       /
      5
```

The node `5` inherits a rule:

```txt id="bsta22"
must be < 10
```

---

Now go deeper:

```txt id="bsta33"
        10
       /
      5
       \
        8
```

Node `8` must satisfy:

```txt id="bsta44"
8 > 5
AND
8 < 10
```

Notice:

```txt id="bsta55"
Constraints accumulate
```

as we move down the tree.

This observation leads directly to the solution.

---

# Step 2 — Discover The Correct Mental Model

Instead of asking:

```txt id="bsta66"
“Is this node valid relative to its parent?”
```

Ask:

```txt id="bsta77"
“What values is this node allowed to have?”
```

This is the key mental shift.

---

# Range-Based Thinking

Every node has:

```txt id="bsta88"
minimum allowed value
maximum allowed value
```

---

# Root

Initially:

```txt id="bsta99"
(-∞ , +∞)
```

Anything is allowed.

---

# Left Child

Suppose root is:

```txt id="bstb00"
10
```

Then left child must be:

```txt id="bstb11"
(-∞ , 10)
```

---

# Right Child

Must be:

```txt id="bstb22"
(10 , +∞)
```

---

# Visual Example

```txt id="bstb33"
           10
          /  \
         5    15
```

Ranges:

```txt id="bstb44"
10  => (-∞,+∞)

5   => (-∞,10)

15  => (10,+∞)
```

---

# Go One Level Deeper

Node:

```txt id="bstb55"
           10
          /
         5
          \
           8
```

Node `8` inherits:

```txt id="bstb66"
must be > 5
must be < 10
```

Range:

```txt id="bstb77"
(5,10)
```

---

# This Is The Entire Solution

The recursion propagates:

```txt id="bstb88"
valid ranges
```

downward.

---

# Step 3 — Define The Recursive Meaning

Define:

```python id="bstb99"
dfs(node, left, right)
```

means:

```txt id="bstc00"
“Validate this subtree assuming
node must stay inside (left,right).”
```

This recursive meaning drives everything.

---

# Visual Meaning

Example:

```python id="bstc11"
dfs(node, 5, 10)
```

means:

```txt id="bstc22"
Every node here must satisfy:

5 < value < 10
```

---

# Step 4 — Build The Solution Gradually

---

# Base Case

```python id="bstc33"
if not node:
    return True
```

---

# Why Return True?

An empty tree cannot violate BST rules.

Think of it as:

```txt id="bstc44"
“Nothing invalid exists here.”
```

---

# Validate Current Node

```python id="bstc55"
if not (node.val > left and node.val < right):
    return False
```

This is the heart of the solution.

---

# What Does This Mean?

Suppose:

```python id="bstc66"
dfs(node, 5, 10)
```

Current node:

```txt id="bstc77"
node.val = 8
```

Check:

```txt id="bstc88"
5 < 8 < 10
```

Valid.

---

Suppose:

```txt id="bstc99"
node.val = 12
```

Check:

```txt id="bstd00"
5 < 12 < 10
```

False.

Immediate violation.

---

# Recursive Left Subtree

```python id="bstd11"
dfs(node.left, left, node.val)
```

Why?

Because everything in the left subtree must satisfy:

```txt id="bstd22"
< current node
```

So:

```txt id="bstd33"
new upper bound = node.val
```

---

# Recursive Right Subtree

```python id="bstd44"
dfs(node.right, node.val, right)
```

Everything in right subtree must satisfy:

```txt id="bstd55"
> current node
```

So:

```txt id="bstd66"
new lower bound = node.val
```

---

# This Is Constraint Propagation

Every recursive call passes:

```txt id="bstd77"
ancestor rules
```

to descendants.

---

# Visual Walkthrough

Valid BST:

```txt id="bstd88"
          8
         / \
        4   12
       / \   \
      2   6   15
```

---

# Root

Call:

```python id="bstd99"
dfs(8, -∞, +∞)
```

Check:

```txt id="bste00"
-∞ < 8 < +∞
```

Valid.

---

# Left Child

Call:

```python id="bste11"
dfs(4, -∞, 8)
```

Check:

```txt id="bste22"
-∞ < 4 < 8
```

Valid.

---

# Node 6

Call:

```python id="bste33"
dfs(6, 4, 8)
```

Notice:

```txt id="bste44"
6 inherited BOTH constraints
```

Check:

```txt id="bste55"
4 < 6 < 8
```

Valid.

---

# Right Child

Call:

```python id="bste66"
dfs(12, 8, +∞)
```

Check:

```txt id="bste77"
8 < 12 < +∞
```

Valid.

Everything succeeds.

Answer:

```python id="bste88"
True
```

---

# Visual Walkthrough Of Invalid Example

```txt id="bste99"
        5
       / \
      1   4
         / \
        3   6
```

---

# Root

```python id="bstf00"
dfs(5,-∞,+∞)
```

Valid.

---

# Right Child

```python id="bstf11"
dfs(4,5,+∞)
```

Check:

```txt id="bstf22"
5 < 4 < +∞
```

Immediately fails.

Return:

```python id="bstf33"
False
```

Done.

---

# Why This Problem Is Important

This problem teaches one of the most important BST ideas:

```txt id="bstf44"
ancestor constraints matter
```

Not just:

- parent relationships

This concept appears repeatedly in:

- BST validation
- BST insertion
- BST deletion
- interval trees

---

# Alternative BST Insight (Inorder Traversal)

There is another solution based on:

```txt id="bstf55"
inorder traversal
```

Because inorder traversal of a BST produces:

```txt id="bstf66"
sorted order
```

Example:

```txt id="bstf77"
2,4,6,8,12,15
```

If traversal is not strictly increasing:

```txt id="bstf88"
not a BST
```

But the range-propagation solution teaches the BST property more directly.

---

# Time Complexity

Every node visited once:

```txt id="bstf99"
O(n)
```

---

# Space Complexity

Recursive stack:

```txt id="bstg00"
O(h)
```

Where:

- `h` = tree height

Worst case:

```txt id="bstg11"
O(n)
```

Balanced BST:

```txt id="bstg22"
O(log n)
```

---

# Pattern Extraction

| Component         | Meaning                                  |
| ----------------- | ---------------------------------------- |
| Trigger           | Need to validate BST ordering            |
| Pattern           | DFS + Range Propagation                  |
| Structure         | Pass allowed value range downward        |
| Core Operation    | validate current value inside bounds     |
| Recursive Meaning | “This subtree must satisfy these limits” |

---

# Final Mental Model

This problem is fundamentally:

```txt id="bstg33"
Every node inherits constraints
from all of its ancestors.
```

The recursive DFS simply propagates those constraints downward and verifies that every node stays inside its allowed range.
