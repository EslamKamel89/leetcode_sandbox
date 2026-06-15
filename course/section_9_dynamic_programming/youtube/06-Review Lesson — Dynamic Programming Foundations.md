I've reviewed the four study guides and implementations you attached:

- Tribonacci (constant transition + state compression)
- Min Cost Climbing Stairs (optimization DP)
- House Robber (take/skip DP)
- Unique Paths (Grid DP)

What follows is the review lesson I would give before moving to the next DP pattern.

---

# Review Lesson — Dynamic Programming Foundations

## Goal

By the end of this review, you should be able to look at a problem and immediately determine:

```txt
Problem
    ↓
State
    ↓
Transition
    ↓
Base Cases
    ↓
Traversal Order
    ↓
Space Optimization?
```

This is the core DP workflow.

---

# Part 1 — The Biggest DP Insight

Most beginners see:

```txt
Tribonacci

Min Cost Climbing Stairs

House Robber

Unique Paths
```

and think:

```txt
4 different problems
```

An experienced engineer sees:

```txt
4 different stories

but only

2 DP patterns
```

---

# Pattern A — Constant Transition DP

Problems:

```txt
Tribonacci

Min Cost Climbing Stairs

House Robber
```

All share:

```txt
dp[i]
depends on

a fixed number
of previous states
```

Visual:

```txt
dp[i]

← dp[i-1]
← dp[i-2]
```

or

```txt
dp[i]

← dp[i-1]
← dp[i-2]
← dp[i-3]
```

---

# Pattern B — Grid DP

Problem:

```txt
Unique Paths
```

State shape changes:

```txt
dp[row][col]
```

Transition changes:

```txt
Top
+
Left
```

But the process is still:

```txt
State
    ↓
Transition
    ↓
Base Cases
```

---

# Part 2 — The Universal DP Construction Process

Every DP problem should be approached in this order.

---

## Step 1 — Define State

Ask:

```txt
What exactly does dp mean?
```

Examples:

### Tribonacci

```txt
dp[i]

=
Tribonacci value at i
```

---

### Min Cost

```txt
dp[i]

=
minimum cost
to reach stair i
```

---

### House Robber

```txt
dp[i]

=
maximum money
from houses [0..i]
```

---

### Unique Paths

```txt
dp[r][c]

=
number of paths
to reach cell
```

---

Rule:

```txt
Never write transition first.

Always define state first.
```

---

## Step 2 — Find Transition

Ask:

```txt
How can I arrive
at this state?
```

---

Tribonacci

```txt
dp[i]

=
dp[i-1]
+
dp[i-2]
+
dp[i-3]
```

---

Min Cost

```txt
dp[i]

=
cost[i]
+
min(
    dp[i-1],
    dp[i-2]
)
```

---

House Robber

```txt
dp[i]

=
max(
    dp[i-1],
    dp[i-2]+nums[i]
)
```

---

Unique Paths

```txt
dp[r][c]

=
dp[r-1][c]
+
dp[r][c-1]
```

---

## Step 3 — Find Base Cases

Ask:

```txt
Which states
cannot be derived?
```

---

Tribonacci

```txt
0
1
1
```

---

Min Cost

```txt
cost[0]
cost[1]
```

---

House Robber

```txt
nums[0]

max(nums[0], nums[1])
```

---

Unique Paths

```txt
First Row = 1

First Column = 1
```

---

## Step 4 — Determine Computation Order

Ask:

```txt
Which states must exist
before this one?
```

---

Constant Transition:

```txt
Left → Right
```

---

Grid:

```txt
Top Left
↓
Bottom Right
```

---

# Part 3 — Pattern Comparison

| Problem      | State           | Transition |
| ------------ | --------------- | ---------- |
| Tribonacci   | Value           | Sum        |
| Min Cost     | Cheapest Cost   | Min        |
| House Robber | Maximum Profit  | Max        |
| Unique Paths | Number of Paths | Sum        |

---

Notice:

```txt
State Meaning Changes

Transition Changes

DP Framework Stays
Exactly The Same
```

---

# Part 4 — Space Optimization Mastery

This is the most important theme across all attached problems.

---

Ask:

```txt
How many previous states
do I actually need?
```

---

Tribonacci

Needs:

```txt
3 states
```

Therefore:

```txt
3 variables
```

---

Min Cost

Needs:

```txt
2 states
```

Therefore:

```txt
2 variables
```

---

House Robber

Needs:

```txt
2 states
```

Therefore:

```txt
2 variables
```

---

Unique Paths

Needs:

```txt
Current Row
Previous Row
```

Eventually:

```txt
1 row
```

---

Rule:

```txt
Store only states
future computations need.
```

---

# Python Lab 1 — State Recognition Lab

Goal:

Learn to identify state meaning.

```python
problems = [
    "Tribonacci",
    "Min Cost Climbing Stairs",
    "House Robber",
    "Unique Paths"
]

for p in problems:
    print(p)
```

Questions:

```txt
For each problem:

What does dp mean?

What is being stored?

Value?
Cost?
Profit?
Paths?
```

If you can't answer this immediately:

```txt
Do not write code yet.
```

---

# Python Lab 2 — Constant Transition Visualizer

```python
def visualize_tribonacci(n):

    t0, t1, t2 = 0, 1, 1

    print(f"{t0=}, {t1=}, {t2=}")

    for step in range(3, n + 1):

        nxt = t0 + t1 + t2

        print(
            f"step={step}",
            f"next={nxt}"
        )

        t0, t1, t2 = t1, t2, nxt

        print(
            f"window -> "
            f"{t0}, {t1}, {t2}"
        )

visualize_tribonacci(10)
```

Questions:

```txt
Which values disappear?

Why is it safe to forget them?
```

---

# Python Lab 3 — Min Cost State Evolution

```python
def visualize(cost):

    prev2 = cost[0]
    prev1 = cost[1]

    print(prev2, prev1)

    for i in range(2, len(cost)):

        current = cost[i] + min(prev1, prev2)

        print(
            f"stair={i}",
            f"cost={current}"
        )

        prev2, prev1 = prev1, current

visualize(
    [1,100,1,1,100,1]
)
```

Questions:

```txt
Why is min() used?

What does prev1 represent?

What does prev2 represent?
```

---

# Python Lab 4 — Take / Skip Simulator

```python
def simulate(nums):

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    print(
        f"house0={prev2}"
    )

    print(
        f"house1={prev1}"
    )

    for i in range(2, len(nums)):

        take = prev2 + nums[i]
        skip = prev1

        current = max(
            take,
            skip
        )

        print(
            f"house={i}",
            f"take={take}",
            f"skip={skip}",
            f"winner={current}"
        )

        prev2, prev1 = prev1, current

simulate([2,7,9,3,1])
```

Questions:

```txt
When does Take win?

When does Skip win?

Why?
```

---

# Python Lab 5 — Build a Grid Visually

```python
def unique_paths(m, n):

    dp = [[1] * n for _ in range(m)]

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

    return dp[-1][-1]

print(unique_paths(3,3))
```

Questions:

```txt
Why are borders all 1?

Which cells create dp[2][2]?

What breaks if we compute
cells randomly?
```

---

# Final Compression Sheet

## Constant Transition DP

Recognition:

```txt
Current state
depends on fixed number
of previous states
```

Framework:

```txt
State
    ↓
Base Cases
    ↓
Transition
    ↓
Loop
    ↓
Space Optimization
```

Examples:

```txt
Tribonacci

Min Cost Climbing Stairs

House Robber
```

---

## Grid DP

Recognition:

```txt
Grid

Matrix

Board
```

Framework:

```txt
dp[r][c]
    ↓
Top + Left
    ↓
Fill Table
    ↓
Bottom Right Answer
```

Example:

```txt
Unique Paths
```

---

## Interview Readiness Checklist

Before coding any DP problem:

```txt
□ What does dp mean?

□ What is the state?

□ How do I reach this state?

□ What are the base cases?

□ In what order should I compute?

□ Can memory be compressed?

□ What pattern is this?
```

If you can answer all seven questions, you are thinking about DP the way interviewers expect. The next patterns (LCS, Edit Distance, LIS, Knapsack, Interval DP) are all built on this exact foundation.
