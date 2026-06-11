# Study Guide — Grid DP & Unique Paths

## Dynamic Programming Pattern: Grid Problems (2D DP)

---

# 1. Section Overview

## What Is Being Taught?

Until now, every DP problem lived on a line:

```txt
0 → 1 → 2 → 3 → 4 → ...
```

Examples:

```txt
Climbing Stairs
Tribonacci
Min Cost Climbing Stairs
House Robber
```

All of them used:

```txt
dp[i]
```

because there was only one dimension.

---

Now the problem changes.

Instead of moving along a line:

```txt
1D
```

we move inside a grid:

```txt
2D
```

Visual:

```txt
□ □ □
□ □ □
□ □ □
```

This introduces the next major DP family:

```txt
Grid DP
```

---

## Why This Matters

Many interview problems are naturally grids:

```txt
Unique Paths
Minimum Path Sum
Dungeon Game
Cherry Pickup
```

The key realization:

```txt
The pattern did NOT change.

Only the state shape changed.
```

---

Previously:

```txt
dp[i]
```

Now:

```txt
dp[row][col]
```

Everything else remains familiar:

```txt
State
Transition
Base Cases
Computation Order
```

---

# The Core Insight

Climbing Stairs asked:

```txt
How many ways to reach stair n?
```

Unique Paths asks:

```txt
How many ways to reach cell (r,c)?
```

These are almost identical questions.

---

# 2. Core Concepts

---

# Concept 1 — State Definition

As always:

```txt
State first.
Formula second.
```

---

State:

```txt
dp[r][c]
```

Meaning:

```txt
Number of unique paths
that reach cell

(r,c)
```

---

Example:

```txt
dp[2][1]
```

means:

```txt
How many ways exist
to arrive at row 2,
column 1
```

---

Notice:

```txt
NOT

Number of paths
starting from this cell
```

It means:

```txt
Paths reaching this cell
```

---

# Concept 2 — Transition

Ask:

```txt
How can I arrive
at cell (r,c)?
```

Rules:

```txt
Only move right
Only move down
```

---

Therefore:

```txt
You can arrive from:

Top
or
Left
```

Only.

---

Visual:

```txt
      ↑
      |
      |
←  (r,c)
```

---

No other possibilities exist.

Therefore:

```txt
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

---

# Why This Works

Suppose:

```txt
3 paths
```

reach from above.

and

```txt
2 paths
```

reach from left.

Every one of those paths can continue into:

```txt
(r,c)
```

---

Therefore:

```txt
3 + 2
=
5
```

total paths.

---

This is exactly the same logic as:

```txt
Ways(n)
=
Ways(n-1)
+
Ways(n-2)
```

from Climbing Stairs.

---

# Concept 3 — Base Cases

The borders behave differently.

---

# First Row

Example:

```txt
S → □ → □ → □
```

How many ways to reach each cell?

Only:

```txt
1
```

Why?

Because:

```txt
Cannot come from above.
```

---

Only move:

```txt
Right
```

---

Result:

```txt
1 1 1 1
```

---

# First Column

Example:

```txt
S
↓
□
↓
□
↓
□
```

Only one route.

---

Result:

```txt
1
1
1
1
```

---

These become our base cases.

---

# Concept 4 — Computation Order

DP requires:

```txt
Dependencies first
```

---

Since:

```txt
dp[r][c]
```

needs:

```txt
Top
Left
```

those must already exist.

---

Therefore:

Valid:

```txt
Row by row
```

or

```txt
Column by column
```

---

Invalid:

```txt
Random order
```

because needed states may not exist.

---

# 3. Mental Models

---

# Mental Model 1 — Water Flow

Imagine water flowing through the grid.

Every path reaching a cell contributes flow.

---

Visual:

```txt
1 → 1 → 1

↓   ↓   ↓

1 → 2 → 3

↓   ↓   ↓

1 → 3 → 6
```

---

Each cell accumulates water from:

```txt
Top
+
Left
```

---

# Mental Model 2 — Path Counter

Every cell contains:

```txt
Number of routes
that can reach me.
```

---

Not:

```txt
Where should I go?
```

---

Instead:

```txt
How many ways
have arrived here?
```

---

# Mental Model 3 — Expanding Frontier

Imagine filling the grid.

Known cells create future cells.

```txt
Known
↓
Generate neighbors
↓
Generate neighbors
```

Eventually:

```txt
Bottom Right
```

contains the answer.

---

# 4. Pattern Recognition

---

# Recognition Signals

Words like:

```txt
Grid
Matrix
Board
Rows
Columns
```

---

Movement restrictions:

```txt
Right
Down
```

or

```txt
Up
Left
Right
Down
```

---

Questions like:

```txt
Number of paths
Minimum path
Maximum path
```

---

# Recognition Checklist

```txt
□ Is there a grid?

□ Do states correspond
  to cells?

□ Can I define
  dp[row][col]?

□ Does each cell depend
  on neighboring cells?

□ Is there a natural
  traversal order?
```

If yes:

```txt
Grid DP
```

---

# Distinguishing from 1D DP

1D:

```txt
dp[i]
```

depends on:

```txt
dp[i-1]
dp[i-2]
```

---

Grid:

```txt
dp[r][c]
```

depends on:

```txt
Neighbor cells
```

---

State shape changes:

```txt
1D → 2D
```

Pattern remains DP.

---

# 5. Step-by-Step Walkthrough

Example:

```txt
3 × 3 Grid
```

---

Start:

```txt
S □ □
□ □ □
□ □ E
```

---

Initialize first row:

```txt
1 1 1
```

---

Initialize first column:

```txt
1
1
1
```

---

Table:

```txt
1 1 1
1 ? ?
1 ? ?
```

---

Cell (1,1)

```txt
Top = 1
Left = 1
```

---

Result:

```txt
1+1=2
```

---

Table:

```txt
1 1 1
1 2 ?
1 ? ?
```

---

Cell (1,2)

```txt
Top = 1
Left = 2
```

---

Result:

```txt
3
```

---

Table:

```txt
1 1 1
1 2 3
1 ? ?
```

---

Cell (2,1)

```txt
Top = 2
Left = 1
```

---

Result:

```txt
3
```

---

Table:

```txt
1 1 1
1 2 3
1 3 ?
```

---

Cell (2,2)

```txt
Top = 3
Left = 3
```

---

Result:

```txt
6
```

---

Final:

```txt
1 1 1
1 2 3
1 3 6
```

Answer:

```txt
6
```

---

# 6. Visual Execution

---

# Table Construction

Start:

```txt
1 1 1
1 ? ?
1 ? ?
```

---

Fill:

```txt
1 1 1
1 2 3
1 3 6
```

---

Visualization

```txt
      1
      ↓

1 → (2)

Top + Left

1 + 1

=
2
```

---

Another Cell

```txt
      2
      ↓

1 → (3)

2 + 1

=
3
```

---

General Rule

```txt
      Top
       ↓

Left → Cell

Cell
=
Top + Left
```

---

# 7. Python Lab

---

# Lab 1 — Build the Full DP Table

## Part A — Minimal Example

```python
def unique_paths(m, n):

    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        dp[r][0] = 1

    for c in range(n):
        dp[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):

            dp[r][c] = (
                dp[r-1][c]
                +
                dp[r][c-1]
            )

    return dp[m-1][n-1]


print(unique_paths(3,3))
```

---

## Part B — Guided Experiment

```python
def unique_paths(m, n):

    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        dp[r][0] = 1

    for c in range(n):
        dp[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):

            dp[r][c] = (
                dp[r-1][c]
                +
                dp[r][c-1]
            )

            print()

            for row in dp:
                print(row)

    return dp[m-1][n-1]


print(unique_paths(3,3))
```

---

## Part C — Observation Questions

```txt
Why are border cells all 1?

Which two cells create dp[2][2]?

What happens if movement upward
becomes allowed?
```

---

# Lab 2 — Space Optimization

The transcript introduces a major optimization.

Observation:

```txt
To compute row r

We only need:

Current row
Previous row
```

Actually:

The implementation goes further.

It uses:

```txt
One row only.
```

---

Runnable Example

```python
def unique_paths(m, n):

    row = [1] * n

    for _ in range(1, m):

        for c in range(1, n):

            row[c] = (
                row[c]
                +
                row[c - 1]
            )

        print(row)

    return row[-1]


print(unique_paths(3,3))
```

---

# Why This Works

Before update:

```txt
row[c]
```

contains:

```txt
Top value
```

---

After updating:

```txt
row[c-1]
```

contains:

```txt
Left value
```

---

Therefore:

```txt
Top + Left
```

is still available.

---

This is the key insight of the optimization.

---

# 8. Full Runnable Code

## Optimal Solution

```python
def unique_paths(m, n):

    row = [1] * n

    for _ in range(1, m):

        for c in range(1, n):

            row[c] = (
                row[c]
                +
                row[c - 1]
            )

    return row[-1]


print(
    unique_paths(
        3,
        3
    )
)
```

---

# 9. Complexity Analysis

## Full Grid

Time:

```txt
O(m*n)
```

Every cell computed once.

---

Space:

```txt
O(m*n)
```

Entire table stored.

---

## Optimized Version

Time:

```txt
O(m*n)
```

Unchanged.

---

Space:

```txt
O(n)
```

Only one row stored.

---

Generalized:

```txt
O(min(m,n))
```

if we store the smaller dimension.

---

# 10. Common Mistakes

---

## Mistake 1

Wrong State Meaning

Incorrect:

```txt
dp[r][c]
=
paths leaving cell
```

Correct:

```txt
dp[r][c]
=
paths reaching cell
```

---

## Mistake 2

Forgetting Border Initialization

Without:

```txt
First Row = 1

First Column = 1
```

everything collapses.

---

## Mistake 3

Filling in Wrong Order

Remember:

```txt
Top
and
Left

must already exist.
```

---

## Mistake 4

Thinking Grid DP Is New

Conceptually:

```txt
Climbing Stairs

↓

Unique Paths
```

is simply:

```txt
1D DP

↓

2D DP
```

The reasoning is identical.

---

# 11. Knowledge Compression

## Key Takeaways

```txt
Grid
    ↓

State

dp[r][c]

    ↓

Meaning

Paths reaching cell

    ↓

Transition

Top + Left

    ↓

dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]

    ↓

Grid DP
```

---

## Interview Recognition Signals

```txt
Grid / Matrix
        ↓

Movement Rules
        ↓

State Per Cell
        ↓

dp[row][col]
        ↓

Neighbor Dependencies
        ↓

Grid DP
```

---

## One-Page Summary

```txt
Unique Paths

State

dp[r][c]
=
number of paths
to reach cell

(r,c)

--------------------------------

Base Cases

First Row = 1

First Column = 1

--------------------------------

Transition

dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]

--------------------------------

Answer

Bottom Right Cell

--------------------------------

Pattern

Grid DP

--------------------------------

Optimization

Full Grid

O(m*n)

↓

One Row

O(n)

--------------------------------

Recognition

Grid

Rows

Columns

Move Right

Move Down

↓

Grid DP
```

The most important lesson of this section is:

```txt
Climbing Stairs

dp[i]

↓

Unique Paths

dp[row][col]
```

The DP mindset remains exactly the same. Only the shape of the state changes.
