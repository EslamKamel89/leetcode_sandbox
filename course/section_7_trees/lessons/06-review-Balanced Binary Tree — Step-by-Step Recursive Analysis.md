# Balanced Binary Tree — Step-by-Step Recursive Analysis

We will deeply trace:

- recursive calls
- returned values
- execution order
- information flow

because this problem is fundamentally about:

```txt id="f9d1rr"
subtree information flowing upward
```

This is one of the most important recursion patterns in Trees.

The attached analysis already explains the recursive structure and mental model.

Now we’ll make the execution fully visible.

---

# The Problem

We must determine:

```txt id="b53gkw"
Is every subtree height-balanced?
```

Balanced means:

|height(left)-height(right)|\leq1

for EVERY node.

---

# The Solution

```python id="jlwm3x"
def dfs(root):
    if not root:
        return [True, 0]

    left = dfs(root.left)
    right = dfs(root.right)

    balanced = (
        left[0]
        and right[0]
        and abs(left[1] - right[1]) <= 1
    )

    return [balanced, 1 + max(left[1], right[1])]
```

---

# The Most Important Concept

The recursive function returns:

```python id="jlwm4y"
[isBalanced, height]
```

NOT just one value.

This is the major recursion upgrade.

---

# What Does `dfs(node)` Mean?

This definition is EVERYTHING.

```txt id="jlwm5z"
dfs(node)
=
“Tell me whether this subtree is balanced,
and also tell me its height.”
```

Every recursive call obeys this contract.

---

# Visual Tree

We’ll trace this example:

```txt id="jlwm6a"
        3
       / \
      9   20
         /  \
        15   7
```

---

# Important Observation

The algorithm works:

```txt id="jlwm7b"
BOTTOM-UP
```

NOT top-down.

The parent cannot decide anything until:

- left subtree finished
- right subtree finished

This is:

> postorder DFS

---

# Full Recursive Execution

---

# STEP 1 — Start At Root

Initial call:

```python id="jlwm8c"
dfs(3)
```

Can node `3` determine balance immediately?

No.

Why?

Because balance depends on:

```txt id="jlwm9d"
left subtree height
right subtree height
```

So recursion descends first.

---

# STEP 2 — Go Left

```python id="jlwmae"
dfs(9)
```

Again:

- must inspect children first

Go left:

```python id="jlwmbf"
dfs(None)
```

---

# STEP 3 — Base Case Hit

```python id="jlwmcg"
return [True, 0]
```

Meaning:

```txt id="jlwmdh"
empty tree:
- balanced
- height 0
```

---

# STEP 4 — Right Child Of 9

```python id="jlwmei"
dfs(None)
```

Again:

```python id="jlwmfj"
[True, 0]
```

---

# STEP 5 — Compute Node 9

Now node `9` finally has child information.

---

# Left Result

```python id="jlwmgk"
[True, 0]
```

---

# Right Result

```python id="jlwmhl"
[True, 0]
```

---

# Balance Check

|0-0|=0\leq1

Balanced.

---

# Height Calculation

1+\max(0,0)=1

---

# Return Value From Node 9

```python id="jlwmim"
[True, 1]
```

Meaning:

```txt id="jlwmjn"
Subtree rooted at 9:
- balanced
- height 1
```

---

# STEP 6 — Return To Root 3

Root now has:

```python id="jlwmko"
left = [True, 1]
```

But still missing:

- right subtree information

So recurse right.

---

# STEP 7 — Process Node 20

```python id="jlwmlp"
dfs(20)
```

Again:

- recurse left first

---

# STEP 8 — Process Node 15

Children:

- None
- None

Both return:

```python id="jlwmmq"
[True, 0]
```

---

# Compute Node 15

Balance:

|0-0|=0

Height:

1+\max(0,0)=1

Return:

```python id="jlwmnr"
[True, 1]
```

---

# STEP 9 — Process Node 7

Exactly same logic.

Returns:

```python id="jlwmos"
[True, 1]
```

---

# STEP 10 — Compute Node 20

Now node `20` receives:

```python id="jlwmpt"
left  = [True, 1]
right = [True, 1]
```

---

# Balance Check

|1-1|=0\leq1

Balanced.

---

# Height

1+\max(1,1)=2

---

# Return From Node 20

```python id="jlwmqu"
[True, 2]
```

Meaning:

```txt id="jlwmrv"
Subtree rooted at 20:
- balanced
- height 2
```

---

# STEP 11 — Final Computation At Root 3

Now root finally has BOTH child results.

---

# Left Subtree

```python id="jlwmsw"
[True, 1]
```

---

# Right Subtree

```python id="jlwmtx"
[True, 2]
```

---

# Root Balance Check

|1-2|=1\leq1

Balanced.

---

# Root Height

1+\max(1,2)=3

---

# Final Return

```python id="jlwmuy"
[True, 3]
```

Main function returns:

```python id="jlwmvz"
True
```

---

# Complete Information Flow Visualization

```txt id="jlwmw0"
Leaves return upward first

15 -> [True,1]
7  -> [True,1]

20 combines children:
-> [True,2]

9 -> [True,1]

3 combines:
left  = [True,1]
right = [True,2]

-> [True,3]
```

This is recursive aggregation.

---

# Why This Is Postorder DFS

Notice the order:

```txt id="jlwmx1"
1. solve left subtree
2. solve right subtree
3. compute current node
```

Current node depends on child information.

That is exactly:

> postorder traversal

---

# What Makes This Problem Difficult

The major challenge is:

```txt id="jlwmy2"
One recursive call returns MULTIPLE pieces of information
```

That is the key progression from:

- Maximum Depth
- Same Tree

---

# Important Mental Shift

Old recursion problems:

```txt id="jlwmz3"
“Visit children”
```

This problem:

```txt id="jlwn04"
“Ask children for structured information”
```

Huge difference.

---

# Why Returning Height Is Necessary

Suppose node:

```txt id="jlwn15"
        A
       / \
      B   C
```

To determine if `A` is balanced:

```txt id="jlwn26"
Need:
height(B)
height(C)
```

So recursion MUST return:

- subtree heights

---

# Why Returning Balance Is Necessary

Suppose:

- left subtree already unbalanced

Then current node automatically becomes:

- unbalanced

So balance information must also propagate upward.

---

# Core Recursive Formula

Node balance depends on:

```txt id="jlwn37"
left balanced
AND
right balanced
AND
height difference <= 1
```

---

# The Deepest Insight

This problem teaches:

```txt id="jlwn48"
Recursive calls are information providers
```

Each subtree computes:

- its own validity
- its own metrics

then passes them upward.

That idea becomes foundational for:

- Diameter of Binary Tree
- Maximum Path Sum
- House Robber III
- Tree Dynamic Programming

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlwn59"
Each node asks:

“Are my children balanced?
And how tall are they?”
```

Then:

- combines their answers
- computes its own state
- returns it upward recursively.
