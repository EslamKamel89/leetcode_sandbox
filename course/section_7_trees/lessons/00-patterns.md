Excellent.
SECTION 7 — Trees is where algorithmic thinking changes significantly.

Up to this point:

- Arrays → linear memory
- Linked Lists → sequential pointer movement
- Sliding Window / Two Pointers → interval control
- Stack → controlled history/state

But Trees introduce something fundamentally different:

> hierarchical branching structure

You are no longer moving through data in a straight line.

You are navigating:

- parent ↔ child relationships
- recursive structure
- multiple paths simultaneously

This section is the foundation for:

- recursion mastery
- divide-and-conquer thinking
- graph traversal later
- recursive DFS in dynamic programming

Your curriculum structure for Trees from the study system is:

- DFS (Recursion)
- BFS (Queue)

We’ll now build the mental model first.

---

# PHASE 0 — PATTERN FOUNDATION

# PART 1 — What Makes Trees Different?

A tree is hierarchical.

Instead of:

```txt
1 → 2 → 3 → 4
```

You now have branching:

```txt
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

Each node may lead to:

- left subtree
- right subtree

This changes traversal completely.

---

# Core Difficulty of Trees

The challenge is NOT the data structure itself.

The challenge is:

> “How do I systematically visit nodes?”

That leads to the two master patterns:

1. DFS — go deep first
2. BFS — go level by level

Everything in Trees mostly derives from these two ideas.

---

# PART 2 — DFS (Depth-First Search)

## Mental Model

DFS means:

> Follow one branch completely before exploring siblings.

Like exploring a maze by:

- choosing a path
- going as deep as possible
- backtracking later

Example:

```txt
        A
      /   \
     B     C
    / \
   D   E
```

DFS order might be:

```txt
A → B → D → E → C
```

Notice:

- We fully explored B’s subtree before touching C.

---

# Why DFS Exists

DFS is ideal when:

- structure is recursive
- answers depend on subtrees
- you need path-based reasoning
- you need post-processing after children

This is why recursion becomes natural.

---

# The Key Insight Behind DFS

A tree is recursively defined.

A subtree is itself another tree.

Example:

```txt
        1
      /   \
     2     3
```

Node `2` is itself the root of another tree.

So instead of solving:

> “the whole tree”

You solve:

> “the current node + smaller subtrees”

This is the foundation of recursive decomposition.

---

# Recognition Signals for DFS

Use DFS when:

### Signal 1 — The problem asks about a path

Examples:

- root-to-leaf paths
- path sums
- longest path

Because DFS naturally follows paths deeply.

---

### Signal 2 — The answer depends on children

Examples:

- tree height
- balanced tree
- subtree properties

Because DFS computes subtree information recursively.

---

### Signal 3 — You must process every node

Examples:

- invert tree
- same tree
- validate BST

DFS systematically touches all nodes.

---

### Signal 4 — The problem language mentions “subtree”

Huge DFS indicator.

Because recursion mirrors subtree structure directly.

---

# Why Recursion Fits Trees So Well

This is the most important conceptual point in the section.

Suppose you want:

> maximum depth

For node `1`:

```txt
depth(1) =
1 + max(depth(left), depth(right))
```

Notice something important:

To solve the whole problem,
you ask the SAME problem on smaller trees.

That is recursion.

---

# DFS Traversal Types

These matter later.

---

## 1. Preorder

```txt
Node → Left → Right
```

Mental model:

> “Process node BEFORE children”

Useful for:

- copying trees
- serialization
- path construction

---

## 2. Inorder

```txt
Left → Node → Right
```

Special property in BSTs:

- outputs sorted order

Critical later.

---

## 3. Postorder

```txt
Left → Right → Node
```

Mental model:

> “Process node AFTER children”

Useful when:

- parent depends on child results

Examples:

- height
- balanced tree
- diameter

---

# Important DFS Mental Model

DFS is usually:

```txt
Divide → Solve children → Combine
```

Example:

- divide into left/right subtree
- recursively solve them
- combine answers

This pattern repeats constantly.

---

# PART 3 — BFS (Breadth-First Search)

Now the second master traversal.

---

# Mental Model

BFS explores:

> level by level

Instead of going deep.

Example:

```txt
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

BFS order:

```txt
1 → 2 → 3 → 4 → 5 → 6 → 7
```

We process all nodes at depth 1 before depth 2.

---

# Why BFS Exists

DFS is depth-oriented.

BFS is distance-oriented.

That distinction matters enormously.

---

# The Queue Mental Model

BFS uses a queue because:

```txt
First discovered
→ first processed
```

This preserves level order.

---

# Recognition Signals for BFS

Use BFS when:

---

### Signal 1 — “Level order”

Immediate BFS.

Examples:

- level traversal
- zigzag traversal
- average of levels

---

### Signal 2 — “Shortest path” in unweighted structures

Because BFS expands outward evenly.

Critical later in Graphs.

---

### Signal 3 — You need nearest/closest answers

Examples:

- nearest leaf
- minimum depth

BFS naturally discovers shallowest answers first.

---

### Signal 4 — Problems explicitly mention levels

Example:

- “nodes at each depth”

Direct BFS indicator.

---

# Core BFS Insight

DFS explores structure deeply.

BFS explores structure by distance from source.

That is the real conceptual difference.

---

# DFS vs BFS — Deep Comparison

| Aspect         | DFS                     | BFS              |
| -------------- | ----------------------- | ---------------- |
| Exploration    | Deep first              | Level first      |
| Main DS        | Recursion / Stack       | Queue            |
| Natural for    | Recursive structure     | Distance/levels  |
| Memory         | Usually smaller         | Can become large |
| Best for       | Subtree computation     | Shortest path    |
| Thinking style | Recursive decomposition | Wave expansion   |

---

# Visual Difference

## DFS

```txt
1 → 2 → 4 → backtrack → 5 → backtrack → 3
```

Like:

> diving deep into one tunnel

---

## BFS

```txt
1
2 3
4 5 6 7
```

Like:

> expanding circles outward

---

# PART 4 — The Most Important Skill in Trees

The biggest skill is NOT syntax.

It is:

> defining what each recursive call means

Example:

```python
def dfs(node):
```

You must mentally define:

> “What does dfs(node) return?”

Examples:

- height of subtree
- whether subtree is balanced
- max path from subtree

This definition drives the entire solution.

---

# Common Beginner Mistake

Beginners write recursion mechanically.

Strong problem solvers first define:

```txt
dfs(node) means ______
```

Then everything becomes easier.

---

# PART 5 — Pattern Map for SECTION 7

Here’s the mental system you’re building.

| Problem Type         | Pattern       |
| -------------------- | ------------- |
| Height/depth         | DFS postorder |
| Path problems        | DFS           |
| Tree comparison      | DFS           |
| Subtree aggregation  | DFS           |
| Level traversal      | BFS           |
| Minimum depth        | BFS           |
| Closest node         | BFS           |
| BST sorted traversal | Inorder DFS   |

---

# PART 6 — How Trees Connect to Future Sections

Trees are foundational for:

- Graph DFS/BFS
- Backtracking
- Dynamic Programming on Trees
- Trie structures
- Segment Trees
- Heap reasoning

This section changes how you think about recursion permanently.

---

# PHASE 1 — PROBLEM SELECTION

## Step 1 — Exact LeetCode Tags / Topics

These are the tags you should filter for.

---

# Core Tags

## Primary

- Binary Tree
- Binary Search Tree
- Tree
- Breadth-First Search
- Depth-First Search
- Recursion
- Queue

---

# Secondary (later in section)

- Backtracking
- Divide and Conquer

---

# Pattern-to-Tag Mapping

| Pattern           | Useful Tags          |
| ----------------- | -------------------- |
| DFS Recursive     | Tree, DFS, Recursion |
| BFS Level Order   | Tree, BFS, Queue     |
| BST Traversal     | BST, DFS             |
| Path Problems     | DFS, Backtracking    |
| Tree Construction | Divide and Conquer   |

---

# Initial Pattern Sequence (Recommended)

This is the learning order I recommend.

| Stage | Pattern                        |
| ----- | ------------------------------ |
| 1     | Basic DFS Traversal            |
| 2     | Tree Height / Depth            |
| 3     | Tree Comparison                |
| 4     | Path-Based DFS                 |
| 5     | BFS Level Traversal            |
| 6     | BST Properties                 |
| 7     | Advanced Recursive Aggregation |

---

# What You Should Do Next

Now follow your PHASE 1 process:

## Your Step

Go collect candidate problems using:

- Binary Tree
- DFS
- BFS
- Recursion
- Queue

Prefer:

- Easy + Medium initially
- Classic interview problems
- High acceptance first

Then send me:

- the candidate list

And I will curate:

- final ordered curriculum
- progression path
- exact pattern coverage
- difficulty ladder
- redundancy removal

This matches the mastery-based system defined in your study framework.
