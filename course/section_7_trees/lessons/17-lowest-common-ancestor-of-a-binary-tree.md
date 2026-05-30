# Problem Classification

| Question       | Answer                                                        |
| -------------- | ------------------------------------------------------------- |
| Pattern        | Advanced Recursive Aggregation                                |
| Traversal Type | DFS Postorder                                                 |
| Core Skill     | Propagate discoveries upward from subtrees                    |
| Key Insight    | Each subtree reports whether it contains `p`, `q`, or neither |

---

# Step 1 — Understand The Real Problem

This looks very similar to:

```txt
235. Lowest Common Ancestor of a BST
```

But this problem is fundamentally different.

---

# Why The BST Version Was Easy

In the BST problem:

```txt
left subtree < node
right subtree > node
```

We used value ordering to navigate.

Example:

```txt
        6
       / \
      2   8
```

If:

```txt
p = 2
q = 4
```

Both values were:

```txt
< 6
```

So we immediately knew:

```txt
go left
```

---

# Why That Doesn't Work Here

Consider:

```txt
          3
        /   \
       5     1
      / \
     6   2
```

There is NO ordering rule.

Node values mean nothing structurally.

You cannot decide:

```txt
go left
or
go right
```

using values.

---

# Therefore

We lose the BST shortcut.

Now we must actually search.

---

# The Most Important Question

Before reading the code, ask:

```txt
How can a node know
whether it is the LCA?
```

This question leads directly to the solution.

---

# Visual Example

```txt
              3
            /   \
           5     1
          / \
         6   2
            / \
           7   4
```

Suppose:

```txt
p = 7
q = 4
```

Answer:

```txt
2
```

Why?

Because:

```txt
7 is below 2
4 is below 2
```

and:

```txt
2 is the lowest node
containing both.
```

---

# What Information Does Node 2 Need?

Node `2` needs to know:

```txt
Did my left subtree find p or q?
Did my right subtree find p or q?
```

Interesting.

That sounds like:

```txt
information flowing upward
```

This is exactly the Advanced Recursive Aggregation pattern.

---

# The Core Insight

Each subtree reports:

```txt
I found p
or
I found q
or
I found nothing
```

Then the parent combines those reports.

---

# Step 2 — Define The Recursive Meaning

This is the most important step.

---

Define:

```python
lowestCommonAncestor(node, p, q)
```

returns:

```txt
The node that represents
a discovered target or LCA
inside this subtree.
```

Notice:

```txt
The recursion does NOT return
True/False.
```

It returns:

```txt
TreeNode
```

This is the key idea.

---

# What Can A Recursive Call Return?

Only three meaningful possibilities.

---

# Case 1

```txt
Found nothing
```

Return:

```python
None
```

---

# Case 2

```txt
Found p
```

Return:

```python
p
```

---

# Case 3

```txt
Found q
```

Return:

```python
q
```

---

# Case 4

```txt
Found LCA
```

Return:

```python
LCA node
```

---

# Everything Flows Upward

Think of recursion as sending messages upward.

Each subtree tells its parent:

```txt
"I found something important."
```

or

```txt
"I found nothing."
```

---

# Step 3 — Understand The Base Cases

---

# Empty Tree

```python
if not root:
    return None
```

Meaning:

```txt
No p
No q
No LCA
```

Nothing useful found.

---

# Found Target

```python
if root == p or root == q:
    return root
```

This is extremely important.

---

# Why Return The Node?

Suppose:

```txt
       5
      /
     7
```

and:

```txt
p = 7
```

When recursion reaches:

```txt
7
```

we discovered one target.

So we send upward:

```txt
"I found p."
```

represented by:

```python
return p
```

---

# Step 4 — Recursive Exploration

Now we search both sides.

```python
left = LCA(root.left, p, q)
right = LCA(root.right, p, q)
```

---

# Meaning

Ask left subtree:

```txt
Did you find anything?
```

---

Ask right subtree:

```txt
Did you find anything?
```

---

Now current node combines the answers.

This is recursive aggregation.

---

# Step 5 — The Most Important Case

```python
if left and right:
    return root
```

This is the heart of the problem.

---

# Visualize It

```txt
              3
            /   \
           5     1
          / \
         6   2
            / \
           7   4
```

Suppose:

```txt
p = 7
q = 4
```

---

At node `2`

Left recursion returns:

```txt
7
```

Right recursion returns:

```txt
4
```

Visualization:

```txt
           2
          / \
         7   4

left  = 7
right = 4
```

---

Now node `2` knows:

```txt
One target exists on left.
One target exists on right.
```

Therefore:

```txt
I am exactly where they split.
```

So:

```python
return root
```

returns node `2`.

---

# Why Is This The LCA?

Because:

```txt
both targets exist
in different branches
```

of this node.

That's precisely the definition of LCA.

---

# Step 6 — One Side Found Something

Suppose:

```python
return left or right
```

---

Why?

Because maybe only one subtree found something.

Example:

```txt
        5
       /
      2
     /
    7
```

Suppose:

```txt
p = 7
q = 4
```

Currently at node `2`.

---

Results:

```python
left = 7
right = None
```

Meaning:

```txt
The left subtree found something.
```

We must pass that information upward.

So:

```python
return left
```

which happens automatically through:

```python
left or right
```

---

# Visual Full Execution

Example:

```txt
              3
            /   \
           5     1
          / \
         6   2
            / \
           7   4
```

Find:

```txt
p = 7
q = 4
```

---

# Start At 3

Need both subtrees.

---

# Explore Left

Go to 5.

---

# Explore Left

Go to 6.

Returns:

```python
None
```

---

# Explore Right

Go to 2.

---

# Explore Left

Go to 7.

Target found.

Returns:

```python
7
```

---

# Explore Right

Go to 4.

Target found.

Returns:

```python
4
```

---

# Back To Node 2

Now:

```python
left = 7
right = 4
```

Both exist.

Therefore:

```python
return 2
```

---

# Back To Node 5

Now:

```python
left = None
right = 2
```

Return:

```python
2
```

---

# Back To Node 3

Now:

```python
left = 2
right = None
```

Return:

```python
2
```

Final answer:

```txt
2
```

---

# Why This Is Postorder DFS

Notice the execution order:

```txt
1. Explore left subtree
2. Explore right subtree
3. Combine results
```

Current node cannot decide anything until:

```txt
both children finish
```

That is:

```txt
Postorder Traversal
```

---

# Deep Insight

This problem is almost identical in spirit to:

```txt
Balanced Binary Tree
Diameter of Binary Tree
```

Why?

Because the parent waits for:

```txt
information from children
```

before making a decision.

---

# What Information Flows Up?

Balanced Tree:

```txt
height
```

---

Diameter:

```txt
subtree height
```

---

LCA:

```txt
found target / found LCA
```

---

Same recursive pattern.

Different information.

---

# Time Complexity

Every node visited once.

```txt
O(n)
```

---

# Space Complexity

Recursive stack:

```txt
O(h)
```

where:

```txt
h = tree height
```

Worst case:

```txt
O(n)
```

Balanced tree:

```txt
O(log n)
```

---

# Pattern Extraction

| Component        | Meaning                                              |
| ---------------- | ---------------------------------------------------- |
| Trigger          | Need ancestor determined from subtree discoveries    |
| Pattern          | Recursive Aggregation                                |
| Structure        | Search left + search right + combine                 |
| Information Flow | Upward                                               |
| Key Rule         | If both sides return something → current node is LCA |

---

# Final Mental Model

This problem is fundamentally:

```txt
Each subtree reports upward:

"I found p."
"I found q."
"I found nothing."

The first node that receives
a discovery from BOTH sides
is exactly where the two paths meet.

That node is the Lowest Common Ancestor.
```

This is one of the purest examples of recursive aggregation in tree problems.
