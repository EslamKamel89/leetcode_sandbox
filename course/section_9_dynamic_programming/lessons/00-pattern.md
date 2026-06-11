Excellent. You have already completed Arrays, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, and Graphs. That means Dynamic Programming is not your first algorithmic pattern anymore—it is the first pattern where **state management and decision reuse** become the central idea.

According to your study system, Section 9 is:

> Goal: Break problems into reusable subproblems.

So we begin with **PHASE 0 — Pattern Foundation**.

---

# SECTION 9 — Dynamic Programming

## First: What Problem Does DP Actually Solve?

Before DP, most problems you've solved looked like:

```txt
Input
 ↓
Process once
 ↓
Answer
```

DP problems look different:

```txt
Input
 ↓
Many choices
 ↓
Same subproblems appear repeatedly
 ↓
Huge amount of repeated work
```

Example:

```txt
Climb 5 stairs

From stair 0:
    go +1
    go +2
```

You eventually ask:

```txt
How many ways from stair 3?
```

Then later:

```txt
How many ways from stair 3?
```

again.

Then again.

The same question keeps appearing.

DP exists to answer:

> "How can I avoid solving the same subproblem repeatedly?"

---

# Mental Model

Imagine recursion as a decision tree.

Without DP:

```txt
                n
             /     \
          n-1      n-2
         /  \      /  \
      n-2  n-3  n-3  n-4
```

Notice:

```txt
n-2
```

appears multiple times.

So does:

```txt
n-3
```

We're recomputing identical work.

DP says:

```txt
Solve once
Store result
Reuse later
```

---

# The Core DP Formula

Every DP problem is secretly asking:

```txt
Current State
      ↓
Answer depends on
smaller states
```

or:

```txt
dp[state]
```

means

```txt
"The answer for this state"
```

Everything in DP revolves around defining that state correctly.

---

# The 4 Questions Every DP Problem Requires

Whenever you see a DP problem:

### Question 1

```txt
What is the state?
```

Example:

```txt
dp[i]
```

might mean:

```txt
answer starting from index i
```

or

```txt
best answer up to i
```

---

### Question 2

```txt
How do states connect?
```

Example:

```txt
dp[i] = dp[i-1] + dp[i-2]
```

This is called the:

```txt
State Transition
```

The most important concept in DP.

---

### Question 3

```txt
What are the base cases?
```

Without them:

```txt
dp[0]
dp[1]
```

everything collapses.

---

### Question 4

```txt
What order do we compute?
```

Because:

```txt
dp[i]
```

depends on:

```txt
dp[i-1]
dp[i-2]
```

those must already exist.

---

# Pattern 1 — 1D DP

This is where everyone should start.

---

## Recognition Signals

Look for:

```txt
Count ways
Minimum cost
Maximum profit
Best score
Can reach
Can construct
```

and

```txt
Current answer depends on
a few previous positions
```

Examples:

```txt
Climbing Stairs
House Robber
Coin Change
Decode Ways
Jump Game
```

---

## Mental Model

Imagine a line:

```txt
0 1 2 3 4 5 6
```

At each position:

```txt
What is the best answer here?
```

Store it.

Move forward.

---

## Generic Structure

```txt
dp[i]

answer for position i
```

Transition:

```txt
dp[i]
    depends on
previous positions
```

Example:

```txt
dp[i] = dp[i-1] + dp[i-2]
```

---

# Pattern 2 — 2D DP

When one variable isn't enough.

---

## Recognition Signals

Usually involves:

```txt
Two strings
Two sequences
Two indices
Grid movement
```

Examples:

```txt
Longest Common Subsequence
Edit Distance
Unique Paths
Distinct Subsequences
```

---

## Mental Model

Instead of:

```txt
dp[i]
```

we now need:

```txt
dp[i][j]
```

because the answer depends on TWO positions.

Example:

```txt
string1 index
string2 index
```

---

## Visual

```txt
      j
    0 1 2 3

i 0
  1
  2
  3
```

Each cell stores:

```txt
answer for (i,j)
```

---

# Pattern 3 — Decision DP

This is where many interview DP questions live.

---

## Recognition Signals

You repeatedly choose:

```txt
Take
or
Skip
```

Examples:

```txt
House Robber
House Robber II
House Robber III
Best Time to Buy and Sell Stock
```

---

## Mental Model

At every position:

```txt
What happens if I take this?
What happens if I skip this?
```

Then choose the better outcome.

---

## Generic Form

```txt
dp[i]

=
best(
    take,
    skip
)
```

---

# Pattern 4 — Knapsack Style DP

One of the most important families.

---

## Recognition Signals

Words like:

```txt
capacity
target
sum
amount
weight
subset
partition
```

Examples:

```txt
Coin Change
Coin Change II
Target Sum
Partition Equal Subset Sum
```

---

## Mental Model

You have:

```txt
Items
+
Constraint
```

and must decide:

```txt
use item?
skip item?
```

---

# Pattern 5 — Sequence Matching DP

Very common in interviews.

---

## Recognition Signals

Problems involving:

```txt
Two strings
Comparison
Transformation
Matching
Subsequence
```

Examples:

```txt
Longest Common Subsequence
Edit Distance
Distinct Subsequences
```

---

## Mental Model

At position:

```txt
(i,j)
```

Ask:

```txt
Characters match?
```

If yes:

```txt
use both
```

If no:

```txt
skip one side
```

---

# DP vs Graphs

You just finished Graphs.

This comparison is important.

### Graph Thinking

```txt
Can I reach node X?
```

### DP Thinking

```txt
What is the best answer for state X?
```

Graphs:

```txt
Traversal
```

DP:

```txt
Reuse computed answers
```

---

# DP vs Backtracking

Backtracking:

```txt
Explore everything
```

DP:

```txt
Explore once
remember result
```

---

# The Biggest Recognition Signal

When solving a problem, ask:

```txt
If I recursively solve this,
will I keep asking the same question again?
```

If the answer is:

```txt
YES
```

then DP should immediately enter your mind.

---

# DP Pattern Hierarchy (Interview ROI Order)

For backend interviews (Django/FastAPI/Laravel), the highest ROI order is:

```txt
1. 1D DP
    - Climbing Stairs
    - House Robber
    - Coin Change
    - Decode Ways

2. Grid / 2D DP
    - Unique Paths
    - Minimum Path Sum

3. String DP
    - Longest Common Subsequence

4. Knapsack-style DP
    - Partition Equal Subset Sum
    - Coin Change II

5. Advanced DP
    - Edit Distance
    - Word Break
```

---

## PHASE 1 — Step 1: LeetCode Tags/Topics

For Dynamic Programming, the tags we should target are:

```txt
Dynamic Programming
Memoization
1D Dynamic Programming
2D Dynamic Programming
Matrix DP
String DP
Knapsack
Decision DP
State Compression (optional)
```

More concretely, our curriculum will likely organize around:

```txt
1D DP
├─ Fibonacci Style
├─ Decision DP
└─ Optimization DP

2D DP
├─ Grid DP
├─ String DP
└─ Sequence DP

Knapsack Family
├─ Subset Sum
├─ Target Sum
└─ Coin Change Variations
```

This aligns with the study plan's 1D DP → 2D DP progression.

---

Next, send me the list of candidate DP problems you collect, and we'll do **PHASE 1 — Step 3 (curation)** to build the final learning path with the highest ROI and cleanest pattern progression.
