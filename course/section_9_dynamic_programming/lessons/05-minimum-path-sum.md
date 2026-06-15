Excellent. This is a very important moment in DP learning.

At first glance, this looks like **Unique Paths**.

Same grid.

Same movement rules.

Same destination.

But the objective changed.

```txt
Unique Paths
→ Count paths
```

```txt
Minimum Path Sum
→ Optimize path cost
```

This is the first time you're seeing:

```txt
Same state space
Different state meaning
Different transition
```

This is one of the biggest DP lessons.

---

# Step 1 — Pattern Prediction

Before coding:

### Recognition Signals

We see:

```txt
Grid
Right / Down movement
Minimum
```

The word:

```txt
minimum
```

is the strongest signal.

We're no longer counting.

We're optimizing.

---

## Pattern

```txt
2D Dynamic Programming
(Grid Optimization DP)
```

---

# Step 2 — State Definition

The most important question:

What does:

```txt
dp[r][c]
```

mean?

For Unique Paths:

```txt
dp[r][c]
=
number of ways to reach (r,c)
```

Not anymore.

Now:

```txt
dp[r][c]
=
minimum path sum needed
to reach (r,c)
```

Notice:

```txt
Same coordinates
Different information
```

---

# Step 3 — Deriving the Transition

Suppose we're at:

```txt
(r,c)
```

How can we arrive here?

Only from:

```txt
(r-1,c)
```

or

```txt
(r,c-1)
```

Same as Unique Paths.

---

But now we don't want:

```txt
all paths
```

We want:

```txt
best path
```

So instead of:

```txt
+
```

we use:

```txt
min(...)
```

---

Suppose:

```txt
Top path cost = 12
Left path cost = 9

Current cell value = 5
```

Then:

```txt
best path to current
=
5 + min(12, 9)
=
14
```

Therefore:

```txt
dp[r][c]
=
grid[r][c]
+
min(
    dp[r-1][c],
    dp[r][c-1]
)
```

This is the recurrence.

---

# Understanding Your In-Place DP

Most textbook solutions create:

```python
dp = [[0] * n for _ in range(m)]
```

You didn't.

You reused:

```python
grid
```

This is a nice optimization.

---

## Mental Model

Initially:

```txt
grid[r][c]
```

contains:

```txt
cell cost
```

After processing:

```txt
grid[r][c]
```

contains:

```txt
minimum cost to reach this cell
```

The meaning changes.

This is a common DP trick.

---

# Why The First Row Is Special

Consider:

```txt
1 3 1
```

Top row.

You cannot arrive from above.

Only from left.

Therefore:

```txt
1
1+3 = 4
4+1 = 5
```

Which is exactly:

```python
grid[r][c] += grid[r][c - 1]
```

---

# Why The First Column Is Special

Similarly:

```txt
1
1
4
```

You cannot arrive from left.

Only from above.

So:

```txt
1
2
6
```

Which is:

```python
grid[r][c] += grid[r - 1][c]
```

---

# Why Interior Cells Use min()

For any non-border cell:

```python
grid[r][c] += min(
    grid[r - 1][c],
    grid[r][c - 1]
)
```

Because both directions are available.

We choose the cheaper one.

---

# Visual Execution

Input:

```txt
1 3 1
1 5 1
4 2 1
```

---

## Start

```txt
1 3 1
1 5 1
4 2 1
```

---

## Process First Row

```txt
1 4 5
1 5 1
4 2 1
```

---

## Process First Column

```txt
1 4 5
2 5 1
6 2 1
```

---

## Cell (1,1)

```txt
5 + min(4,2)
=
7
```

Grid:

```txt
1 4 5
2 7 1
6 2 1
```

---

## Cell (1,2)

```txt
1 + min(5,7)
=
6
```

Grid:

```txt
1 4 5
2 7 6
6 2 1
```

---

## Cell (2,1)

```txt
2 + min(7,6)
=
8
```

Grid:

```txt
1 4 5
2 7 6
6 8 1
```

---

## Cell (2,2)

```txt
1 + min(6,8)
=
7
```

Grid:

```txt
1 4 5
2 7 6
6 8 7
```

Answer:

```txt
7
```

---

# Reviewing Your Solution

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):

                if r == 0 and c != 0:
                    grid[r][c] += grid[r][c - 1]

                elif c == 0 and r != 0:
                    grid[r][c] += grid[r - 1][c]

                elif r != 0 and c != 0:
                    grid[r][c] += min(
                        grid[r - 1][c],
                        grid[r][c - 1]
                    )

        return grid[r][c]
```

Correct.

Time:

```txt
O(m × n)
```

Space:

```txt
O(1)
```

(extra space)

because the input grid is reused.

---

# Connection to Previous DP Problems

### Climbing Stairs

```txt
State:
    stair

Goal:
    count ways

Transition:
    +
```

---

### Unique Paths

```txt
State:
    cell

Goal:
    count ways

Transition:
    +
```

---

### Minimum Path Sum

```txt
State:
    cell

Goal:
    minimum cost

Transition:
    min()
```

---

Notice something important:

```txt
State stayed the same.

Objective changed.

Transition changed.
```

That is a major DP pattern-recognition skill.

---

# Pattern Extraction

### Trigger

```txt
Grid
Movement restrictions
Minimum / Maximum optimization
```

### Pattern

```txt
2D Grid DP
(Optimization)
```

### State

```txt
dp[r][c]
=
minimum cost to reach (r,c)
```

### Transition

```txt
dp[r][c]
=
grid[r][c]
+
min(
    dp[r-1][c],
    dp[r][c-1]
)
```

### Base Cases

```txt
First row:
    can only come from left

First column:
    can only come from above
```

### Flow

```txt
Build cheapest cost
for every cell
until destination
```

---

Now compare **Unique Paths** and **Minimum Path Sum** and answer this:

```txt
Unique Paths:
    dp[r][c] = ?

Minimum Path Sum:
    dp[r][c] = ?
```

Can you state precisely how the meaning of the state changed, even though both problems use the same grid and traversal order? This distinction is the key to recognizing DP variants.
