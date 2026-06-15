Excellent. This is the first true **2D DP** problem in the curriculum.

Notice how the mental model changes:

```txt id="m6k2jt"
Climbing Stairs
    ↓
One coordinate
    ↓
dp[i]
```

```txt id="cgg8xh"
Unique Paths
    ↓
Two coordinates
    ↓
dp[row][col]
```

The core DP ideas are identical:

```txt id="g4w7l2"
State
Transition
Base Cases
```

Only the state dimension changed.

---

# Step 1 — Pattern Prediction

Before coding, the signals should be:

### Signal 1

```txt id="5cf55x"
How many ways?
```

This is a counting problem.

Same as Climbing Stairs.

---

### Signal 2

```txt id="r4a6l5"
Grid
```

Whenever you see:

```txt id="zkvvw0"
matrix
grid
board
row
column
```

you should immediately ask:

```txt id="pcdfgc"
Can I define a state for each cell?
```

---

### Signal 3

Current cell depends on neighboring cells.

That strongly suggests:

```txt id="4n0wzg"
2D Dynamic Programming
```

---

# Step 2 — State Definition

The most important question:

What does:

```txt id="l2v48z"
dp[r][c]
```

mean?

A good definition is:

```txt id="fw71ew"
Number of ways to reach cell (r,c)
```

Everything else follows from this definition.

---

# Visualizing the State

For:

```txt id="4ohx2s"
m = 3
n = 4
```

Grid:

```txt id="08bvl5"
(0,0) (0,1) (0,2) (0,3)

(1,0) (1,1) (1,2) (1,3)

(2,0) (2,1) (2,2) (2,3)
```

Each cell stores:

```txt id="z9c7tu"
How many ways can I get here?
```

Not:

```txt id="hn0pdq"
How many ways can I leave here?
```

Both are valid state definitions, but your solution uses:

```txt id="q3sl7s"
ways to reach
```

---

# Step 3 — Transition Derivation

This is the heart of the problem.

Suppose we're computing:

```txt id="qqf6ye"
dp[r][c]
```

How can we arrive there?

Robot can only move:

```txt id="fj8ir6"
Right
Down
```

Therefore:

To reach:

```txt id="n9rr9x"
(r,c)
```

we must come from either:

```txt id="gqjg4s"
(r-1,c)
```

or

```txt id="5f9v9m"
(r,c-1)
```

There are no other possibilities.

---

If:

```txt id="9f3c3t"
5 ways reach from above
```

and

```txt id="bdj3i7"
3 ways reach from left
```

then:

```txt id="s2a9yt"
8 ways reach current cell
```

Therefore:

```txt id="6e2l5z"
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

This is the entire DP transition.

---

# Step 4 — Why Are The Borders All Ones?

Your initialization:

```python
dp = [[1] * n for _ in range(m)]
```

looks magical at first.

Let's understand why.

---

## First Row

```txt id="tv6n8h"
(0,0) (0,1) (0,2) (0,3)
```

Can only move right.

So:

```txt id="n0jw5m"
1 way
1 way
1 way
1 way
```

---

## First Column

```txt id="4b9v25"
(0,0)
(1,0)
(2,0)
(3,0)
```

Can only move down.

So:

```txt id="sml8v7"
1 way
1 way
1 way
1 way
```

---

Therefore:

```txt id="n81jfd"
Entire top row = 1
Entire left column = 1
```

Those are the base cases.

---

# Step 5 — Visual Execution

Let's run:

```txt id="zsz48d"
m = 3
n = 4
```

Initial DP:

```txt id="r6m3lb"
1 1 1 1
1 1 1 1
1 1 1 1
```

---

## Cell (1,1)

```txt id="m5tqq7"
1 + 1 = 2
```

Grid:

```txt id="d0mx1n"
1 1 1 1
1 2 1 1
1 1 1 1
```

---

## Cell (1,2)

```txt id="h92pdn"
1 + 2 = 3
```

Grid:

```txt id="bhrwqf"
1 1 1 1
1 2 3 1
1 1 1 1
```

---

## Cell (1,3)

```txt id="8d33ew"
1 + 3 = 4
```

Grid:

```txt id="3w7bx6"
1 1 1 1
1 2 3 4
1 1 1 1
```

---

## Cell (2,1)

```txt id="nhjlwm"
2 + 1 = 3
```

Grid:

```txt id="ps2hnn"
1 1 1 1
1 2 3 4
1 3 1 1
```

---

## Cell (2,2)

```txt id="av6opb"
3 + 3 = 6
```

Grid:

```txt id="8gl4r6"
1 1 1 1
1 2 3 4
1 3 6 1
```

---

## Cell (2,3)

```txt id="wc4g9i"
4 + 6 = 10
```

Grid:

```txt id="qb0xmd"
1 1 1 1
1 2 3 4
1 3 6 10
```

Answer:

```txt id="fby3t5"
10
```

---

# Reviewing Your Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]
```

This is the canonical bottom-up solution.

Complexity:

```txt id="e6g8rk"
Time  : O(m × n)
Space : O(m × n)
```

---

# Connection to Climbing Stairs

Look closely:

### Climbing Stairs

```txt id="9pjlwm"
dp[i]
=
dp[i-1]
+
dp[i-2]
```

Current state depends on previous states.

---

### Unique Paths

```txt id="qkxq3z"
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

Current state depends on neighboring states.

---

The pattern is actually the same:

```txt id="frg4si"
State
    ↓
Build from smaller states
    ↓
Reuse results
```

Only the state shape changed:

```txt id="4yvw4i"
1D DP → dp[i]

2D DP → dp[r][c]
```

---

# Pattern Extraction

### Trigger

```txt id="j74syj"
Grid
+
Count number of ways
+
Movement restrictions
```

### Pattern

```txt id="jv45v2"
2D Dynamic Programming
(Grid DP)
```

### State

```txt id="v6pp7v"
dp[r][c]
=
ways to reach cell (r,c)
```

### Transition

```txt id="ibzowu"
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

### Base Cases

```txt id="8n7aqf"
Top row = 1
Left column = 1
```

### Flow

```txt id="pnqx39"
Fill grid
left-to-right
top-to-bottom
until destination
```

Before moving to **63. Unique Paths II**, answer this:

> Why is it safe to compute the table row-by-row from top-left to bottom-right? What exactly would break if we tried to fill the table from bottom-right toward top-left while keeping the same state definition?
