# Problem Classification

| Question       | Answer                                                |
| -------------- | ----------------------------------------------------- |
| Pattern        | Advanced Recursive Aggregation                        |
| Traversal Type | DFS Postorder                                         |
| Core Skill     | Return multiple states from each subtree              |
| Key Insight    | Every node has two possible states: rob it or skip it |

---

# Step 1 — Understand The Real Problem

At first glance this looks like:

```txt id="hr31"
Dynamic Programming
```

And it is.

But the deeper question is:

```txt id="hr32"
What is the state?
```

Understanding the state is the entire problem.

---

# The Rule

You cannot rob:

```txt id="hr33"
parent
and
child
```

simultaneously.

---

# Example

```txt id="hr34"
       3
      / \
     2   3
```

If you rob:

```txt id="hr35"
3
```

You cannot rob:

```txt id="hr36"
2
or
3
```

below it.

---

# The Most Important Observation

For every node there are only two choices:

---

# Choice 1

```txt id="hr37"
Rob this node
```

---

# Choice 2

```txt id="hr38"
Do NOT rob this node
```

That's it.

The entire solution comes from analyzing these two states.

---

# Visual Example

Suppose:

```txt id="hr39"
        4
       / \
      1   3
```

At node `4`:

---

Option A:

```txt id="hr40"
Rob 4
```

Then:

```txt id="hr41"
Cannot rob 1
Cannot rob 3
```

---

Option B:

```txt id="hr42"
Skip 4
```

Then:

```txt id="hr43"
Can freely choose
best option from 1 and 3
```

---

# The Core Insight

Every subtree must tell its parent:

```txt id="hr44"
How much money can I make
if you rob me?

How much money can I make
if you don't rob me?
```

This is the entire recursive state.

---

# Step 2 — Define The Recursive Meaning

This is the most important step.

---

Define:

```python
dfs(node)
```

returns:

```python
[with_node, without_node]
```

Meaning:

```txt id="hr45"
with_node
=
best profit if this node is robbed

without_node
=
best profit if this node is NOT robbed
```

This recursive meaning drives everything.

---

# Visual Meaning

Suppose:

```txt id="hr46"
       5
```

returns:

```python
[5,0]
```

Meaning:

```txt id="hr47"
Rob 5     -> earn 5
Skip 5    -> earn 0
```

---

# Why Two Values?

This is the key upgrade from previous tree problems.

---

# Maximum Depth Returned

```txt id="hr48"
one number
```

---

# Balanced Tree Returned

```txt id="hr49"
(balance,height)
```

---

# House Robber III Returns

```txt id="hr50"
(rob,skip)
```

Two states.

Because parent decisions depend on both.

---

# Step 3 — Base Case

```python
if not root:
    return [0,0]
```

Meaning:

```txt id="hr51"
Empty subtree
```

---

# Profit If Robbed?

```txt id="hr52"
0
```

---

# Profit If Skipped?

```txt id="hr53"
0
```

---

Return:

```python
[0,0]
```

---

# Step 4 — Gather Child Information

```python
left_pair = dfs(root.left)
right_pair = dfs(root.right)
```

Now each child gives:

```python
[
    rob_child,
    skip_child
]
```

---

# Example

Suppose left child returns:

```python
[4,2]
```

Meaning:

```txt id="hr54"
Rob left child  -> 4
Skip left child -> 2
```

---

Right child returns:

```python
[3,1]
```

Meaning:

```txt id="hr55"
Rob right child  -> 3
Skip right child -> 1
```

---

# Step 5 — Compute "Rob Current Node"

This is the first major formula.

---

Code:

```python
with_root = (
    root.val
    + left_pair[1]
    + right_pair[1]
)
```

---

Why?

Suppose:

```txt id="hr56"
You rob current node
```

Then rule says:

```txt id="hr57"
Cannot rob children
```

Therefore:

```txt id="hr58"
Must use children's
"skip" state
```

---

Visualization

```txt id="hr59"
        ROOT
       /    \
      A      B
```

If ROOT robbed:

```txt id="hr60"
A skipped
B skipped
```

Always.

---

Formula becomes:

```txt id="hr61"
root value
+
left skip
+
right skip
```

---

# Step 6 — Compute "Skip Current Node"

Code:

```python
without_root = (
    max(left_pair)
    +
    max(right_pair)
)
```

---

Why?

Suppose:

```txt id="hr62"
Current node skipped
```

Now:

```txt id="hr63"
Children are unrestricted
```

Each child can choose:

```txt id="hr64"
rob
or
skip
```

whichever earns more.

---

Visualization

```txt id="hr65"
        ROOT (skip)
       /          \
      A            B
```

For A:

```txt id="hr66"
choose best state
```

For B:

```txt id="hr67"
choose best state
```

---

Therefore:

```txt id="hr68"
best left
+
best right
```

---

Formula:

```python
max(left_pair)
+
max(right_pair)
```

---

# This Is The Whole Problem

These two equations are everything.

---

# State 1

```txt id="hr69"
Rob current
```

Formula:

```txt id="hr70"
root
+
left skip
+
right skip
```

---

# State 2

```txt id="hr71"
Skip current
```

Formula:

```txt id="hr72"
best left
+
best right
```

---

# Return State

```python
return [with_root, without_root]
```

Pass both possibilities upward.

---

# Visual Walkthrough

Example:

```txt id="hr73"
        3
       / \
      2   3
       \   \
        3   1
```

Expected answer:

```txt id="hr74"
7
```

---

# Process Leaves First

Node:

```txt id="hr75"
3
```

Leaf.

Children:

```python
[0,0]
```

---

Compute:

```txt id="hr76"
with = 3
without = 0
```

Return:

```python
[3,0]
```

---

Other leaf:

```txt id="hr77"
1
```

Returns:

```python
[1,0]
```

---

# Process Node 2

Child returned:

```python
[3,0]
```

---

Rob 2:

```txt id="hr78"
2 + 0
=
2
```

---

Skip 2:

```txt id="hr79"
max(3,0)
=
3
```

Return:

```python
[2,3]
```

---

# Process Node 3 (right side)

Child:

```python
[1,0]
```

---

Rob:

```txt id="hr80"
3 + 0
=
3
```

---

Skip:

```txt id="hr81"
1
```

Return:

```python
[3,1]
```

---

# Process Root

Current:

```txt id="hr82"
root = 3
```

Children:

```python
left  = [2,3]
right = [3,1]
```

---

# Rob Root

Formula:

```txt id="hr83"
3
+
3
+
1
=
7
```

---

# Skip Root

Formula:

```txt id="hr84"
max(2,3)
+
max(3,1)
=
6
```

---

Return:

```python
[7,6]
```

---

Final Answer

```python
max([7,6])
=
7
```

---

# Why This Is Postorder DFS

Notice:

```txt id="hr85"
Need child states first
```

before computing parent.

Order:

```txt id="hr86"
left
right
current
```

That is:

```txt id="hr87"
Postorder Traversal
```

---

# Deep Insight

This problem teaches a major tree-DP idea:

```txt id="hr88"
A subtree may need to return
multiple possible futures.
```

Not:

```txt id="hr89"
one answer
```

but:

```txt id="hr90"
all information parent needs
to make its decision
```

---

# Compare To Earlier Problems

### Maximum Depth

Returned:

```txt id="hr91"
height
```

---

### Diameter

Returned:

```txt id="hr92"
height
```

while updating global answer.

---

### LCA

Returned:

```txt id="hr93"
discovered target
```

---

### House Robber III

Returned:

```txt id="hr94"
rob-state
skip-state
```

This is the most DP-like recursion you've seen so far.

---

# Time Complexity

Each node visited once:

```txt id="hr95"
O(n)
```

---

# Space Complexity

Recursive stack:

```txt id="hr96"
O(h)
```

where:

```txt id="hr97"
h = tree height
```

---

# Pattern Extraction

| Component   | Meaning                                          |
| ----------- | ------------------------------------------------ |
| Trigger     | Parent decision depends on child decisions       |
| Pattern     | Tree DP / Recursive Aggregation                  |
| Structure   | Return multiple states                           |
| Core State  | [rob, skip]                                      |
| Key Formula | rob → children skip, skip → children choose best |

---

# Final Mental Model

This problem is fundamentally:

```txt id="hr98"
Every node asks:

"What is the best profit
if I rob myself?"

and

"What is the best profit
if I skip myself?"

The subtree computes both answers
and passes them upward.

The parent then uses those answers
to make its own decision.
```

This is one of the cleanest introductions to dynamic programming on trees.
