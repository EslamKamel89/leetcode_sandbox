# Problem Classification

| Question       | Answer                             |
| -------------- | ---------------------------------- |
| Pattern        | Tree Comparison / Validation       |
| Traversal Type | DFS Recursive                      |
| Core Skill     | Mirror-structure comparison        |
| Key Insight    | Compare opposite sides recursively |

---

# Step 1 — Understand The Real Problem

The problem asks:

> “Is the tree a mirror of itself?”

This is NOT normal tree equality.

This is:

> mirrored equality

That distinction is everything.

---

# Visual Meaning of Symmetry

Symmetric tree:

```txt id="qyzfrw"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

Notice:

```txt id="jlwmx4"
Left side mirrors right side
```

---

# Important Observation

These pairs must match:

| Left Side  | Right Side  |
| ---------- | ----------- |
| left.left  | right.right |
| left.right | right.left  |

NOT:

- left.left ↔ right.left

That is the critical insight.

---

# Non-Symmetric Example

```txt id="4glfcw"
          1
        /   \
       2     2
        \     \
         3     3
```

Looks similar at first.

But mirror structure fails.

Why?

Left subtree:

```txt id="jlwmv6"
3 is on RIGHT
```

Right subtree:

```txt id="jlwmu7"
3 is ALSO on RIGHT
```

A mirror would require:

- opposite positions

So answer:

```python id="jlwmt8"
False
```

---

# Step 2 — Pattern Recognition

This problem has strong synchronized DFS signals.

---

# Signal 1 — Compare Two Sides Simultaneously

We are traversing:

- left subtree
- right subtree

at the same time.

Exactly like Same Tree.

---

# Signal 2 — Structural Validation

We must verify:

- structure
- node positions
- values

---

# Signal 3 — Recursive Mirror Relationship

The mirror condition naturally decomposes recursively.

Huge DFS indicator.

---

# Step 3 — The Most Important Insight

This problem is NOT:

```txt id="jlsms9"
“Compare same positions.”
```

It IS:

```txt id="jlsmt0"
“Compare mirrored positions.”
```

That is the entire conceptual difference from Same Tree.

---

# Compare With Same Tree

## Same Tree

Compare:

```txt id="jlsmu1"
left ↔ left
right ↔ right
```

---

## Symmetric Tree

Compare:

```txt id="jlsmv2"
left ↔ right
right ↔ left
```

Mirror traversal.

---

# Step 4 — Define The Recursive Meaning

Define:

```python id="jlsmw3"
dfs(left, right)
```

means:

> “Are these two subtrees mirror images of each other?”

This recursive meaning drives the entire solution.

---

# Step 5 — Build The Logic Gradually

---

# Base Case 1 — Both Nodes Missing

```python id="jlsmx4"
if not left and not right:
    return True
```

---

# What This Means

Example:

```txt id="jlsmy5"
None ↔ None
```

Perfect mirror.

Both sides end simultaneously.

---

# Why This Matters

Mirror structure requires:

- both sides exist together
  OR
- both sides missing together

---

# Base Case 2 — One Missing

```python id="jlsmz6"
if not left or not right:
    return False
```

---

# What This Means

Example:

```txt id="jlsm07"
left exists
right missing
```

Mirror broken.

---

# Why This Must Happen Before Value Comparison

Because:

```python id="jlsm18"
left.val
```

would crash if:

- `left == None`

So structural validation happens first.

---

# Core Recursive Logic

```python id="jlsm29"
left.val == right.val
```

Current mirrored nodes must:

- contain same value

---

# Mirror Recursive Calls

```python id="jlsm3a"
dfs(left.left, right.right)
```

This checks:

```txt id="jlsm4b"
outer mirror
```

---

# Second Recursive Call

```python id="jlsm5c"
dfs(left.right, right.left)
```

This checks:

```txt id="jlsm6d"
inner mirror
```

---

# This Is The Heart Of The Problem

The recursion crosses directions:

```txt id="jlsm7e"
left subtree goes inward
right subtree goes inward oppositely
```

That creates mirror comparison.

---

# Visual Mirror Mapping

Tree:

```txt id="jlsm8f"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

Recursive comparisons:

| Comparison |
| ---------- |
| 2 ↔ 2      |
| 3 ↔ 3      |
| 4 ↔ 4      |

But structurally:

```txt id="jlsm9g"
left.left ↔ right.right
left.right ↔ right.left
```

---

# Full Recursive Expression

```python id="jlsmah"
return (
    left.val == right.val
    and dfs(left.left, right.right)
    and dfs(left.right, right.left)
)
```

---

# Why `and` Is Necessary

Mirror symmetry requires:

- ALL mirror relationships valid

If even one fails:

- tree is not symmetric

---

# Visual Recursive Walkthrough

Input:

```txt id="jlsmbi"
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

---

# Initial Call

```python id="jlsmcj"
dfs(root.left, root.right)
```

Meaning:

```txt id="jlsmdk"
dfs(2, 2)
```

Values match.

---

# Outer Mirror Check

```python id="jlsmel"
dfs(3, 3)
```

Leaf nodes match.

Children:

- None ↔ None

Return:

```python id="jlsmfm"
True
```

---

# Inner Mirror Check

```python id="jlsmgn"
dfs(4, 4)
```

Also valid.

---

# Final Result

All recursive checks:

```txt id="jlsmho"
True
```

Final answer:

```python id="jlsmip"
True
```

---

# Why This Problem Is Important

This problem upgrades recursive comparison thinking.

---

# Same Tree Taught:

```txt id="jlsmjq"
Compare matching positions
```

---

# Symmetric Tree Teaches:

```txt id="jlsmkr"
Compare mirrored positions
```

This is a more advanced structural relationship.

---

# Deep Conceptual Insight

The recursion pattern itself encodes:

- geometric symmetry

The recursion structure mirrors:

- the visual tree symmetry

That is elegant and important.

---

# Why This Is DFS

The recursion:

- fully explores mirrored branches deeply
- backtracks after subtree validation

Classic DFS traversal.

---

# Time Complexity

Every node visited once:

```txt id="jlsmls"
O(n)
```

---

# Space Complexity

Recursive stack depth:

```txt id="jlsmmt"
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

| Component         | Meaning                       |
| ----------------- | ----------------------------- |
| Trigger           | Compare mirrored structure    |
| Pattern           | Synchronized DFS              |
| Structure         | Cross-recursive comparison    |
| Core Operation    | left.left ↔ right.right       |
| Recursive Meaning | “Are these subtrees mirrors?” |

---

# Final Mental Model

This problem is fundamentally:

```txt id="jlsmnu"
Mirror symmetry =
current nodes equal
+
outer subtrees mirror
+
inner subtrees mirror
```

Where recursion itself follows the mirror geometry of the tree.
