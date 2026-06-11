# Dynamic Programming Foundations

## Course Sections Covered

```txt
— Course Introduction and Visual Intuition
— Fundamentals of Dynamic Programming
— The Staircase Problem: Counting Paths
— Implementing Recursive Solutions
— The Inefficiency of Simple Recursion
— Pattern 1: Memoization (Top-Down)
— Pattern 2: Tabulation (Bottom-Up)
— Comparing Memoization vs Tabulation
```

---

# 1. Section Overview

## What Is Being Taught?

These sections introduce the core idea behind Dynamic Programming (DP).

Not:

```txt
Dynamic Programming =
memorizing formulas
```

But:

```txt
Dynamic Programming =
Solve smaller problems
↓
Reuse their answers
↓
Build larger answers
```

The staircase problem is used as a vehicle to teach:

```txt
1. Recursive problem decomposition

2. Overlapping subproblems

3. Memoization (Top-Down DP)

4. Tabulation (Bottom-Up DP)
```

These four ideas form the foundation of almost every DP problem you'll encounter later.

---

## Why It Matters

Many problems seem impossible because the number of possible solutions grows exponentially.

Example:

```txt
How many ways to reach step 40?
```

Trying every path becomes infeasible.

DP teaches us:

```txt
Don't solve the same question twice.
```

---

## What Problem Does DP Solve?

DP solves problems where:

```txt
Large problem
↓
Can be split into smaller problems
↓
The same smaller problems appear repeatedly
```

Example:

```txt
Ways(6)
```

needs:

```txt
Ways(5)
Ways(4)
```

But:

```txt
Ways(5)
```

also needs:

```txt
Ways(4)
Ways(3)
```

Notice:

```txt
Ways(4)
```

appears twice.

That duplication is the entire reason DP exists.

---

# 2. Core Concepts

---

# Concept 1 — Recursive Decomposition

## Definition

Breaking a large problem into smaller versions of itself.

---

## Purpose

Instead of solving:

```txt
Ways(40)
```

directly, solve:

```txt
Ways(39)
Ways(38)
```

first.

---

## Staircase Example

You can reach step N from only:

```txt
N-1
N-2
```

because allowed moves are:

```txt
+1
+2
```

Therefore:

```txt
Ways(N)
=
Ways(N-1)
+
Ways(N-2)
```

This is called a recurrence relation.

---

## Common Misconception

Many beginners think:

```txt
Ways(N-1) + Ways(N-2)
```

is magic.

It is not.

It comes from:

```txt
How can I arrive at step N?
```

Only two possibilities exist:

```txt
From N-1
From N-2
```

Nothing else.

---

# Concept 2 — Base Cases

## Definition

Problems that are already known.

---

For the staircase:

```txt
Ways(1) = 1
Ways(2) = 2
```

---

## Why They Exist

Without base cases:

```txt
Ways(5)
→ Ways(4)
→ Ways(3)
→ Ways(2)
→ Ways(1)
→ Ways(0)
→ Ways(-1)
...
```

Recursion never stops.

---

## Mental Model

Think of base cases as:

```txt
Ground floor
```

Everything else stands on top of them.

---

# Concept 3 — Overlapping Subproblems

This is the most important DP concept.

---

## Definition

The same subproblem appears multiple times.

---

Example:

```txt
Ways(6)
```

Recursion Tree:

```txt
               6
            /     \
          5         4
        /  \      /   \
       4    3    3     2
      / \
     3   2
```

Notice:

```txt
Ways(4)
Ways(3)
```

appear repeatedly.

---

## Why This Is Bad

Each repeated calculation costs time.

The recursion tree explodes.

---

# Concept 4 — Memoization

## Definition

Store previously computed answers.

---

Instead of:

```txt
Compute Ways(3)
again
```

do:

```txt
Look up Ways(3)
```

---

## Why It Exists

Repeated work wastes time.

Memoization removes repetition.

---

## Mental Model

Imagine a calculator with memory.

First time:

```txt
Ways(3)
```

Compute it.

Store:

```txt
3 → 3
```

Later:

```txt
Need Ways(3)?
```

Just read memory.

No calculation.

---

# Concept 5 — Tabulation

## Definition

Compute answers in order from smallest to largest.

---

Instead of:

```txt
Need Ways(5)
↓
Ask for Ways(4)
↓
Ask for Ways(3)
```

You do:

```txt
Ways(1)
Ways(2)
Ways(3)
Ways(4)
Ways(5)
```

---

## Mental Model

Building a staircase:

```txt
Step 1 done
↓
Step 2 done
↓
Step 3 done
↓
Step 4 done
```

Each new step uses previous steps.

---

# 3. Mental Models

---

# Mental Model 1 — Family Tree

Recursive DP:

```txt
Parent
↓
Children
↓
Grandchildren
```

Every node asks:

```txt
Who are my smaller problems?
```

---

# Mental Model 2 — Ledger Book

Memoization:

```txt
Question Asked?
↓
Check notebook
↓
Already solved?
↓
Use answer
```

---

# Mental Model 3 — Assembly Line

Tabulation:

```txt
Known Parts
↓
Build Next Part
↓
Build Next Part
↓
Build Final Product
```

No recursion.

No backtracking.

Just forward progress.

---

# 4. Pattern Recognition

---

# Recognition Signals

Look for:

```txt
Count ways
Number of possibilities
Number of paths
```

or

```txt
Current answer depends on
smaller answers
```

or

```txt
Can break into
same type of problem
```

---

# When To Use DP

Use DP when:

```txt
Problem
↓
Break into smaller problems
↓
Same subproblems repeat
```

---

# When NOT To Use DP

Avoid DP when:

```txt
Every subproblem is unique
```

No repetition means:

```txt
No benefit from caching
```

---

# Similar Patterns

### Recursion

```txt
Solve smaller problems
```

### Dynamic Programming

```txt
Solve smaller problems
+
Store results
```

Difference:

```txt
Memory
```

---

# Recognition Checklist

Before solving:

```txt
□ Can I define smaller versions?

□ Do subproblems repeat?

□ Can I define base cases?

□ Can I reuse previous answers?

□ Does answer depend on smaller answers?
```

If yes:

```txt
Think DP.
```

---

# 5. Step-by-Step Walkthrough

## Staircase with 4 Steps

---

### Step 1

Known:

```txt
Ways(1)=1
Ways(2)=2
```

---

### Step 2

Compute:

```txt
Ways(3)
=
Ways(2)+Ways(1)

=
2+1

=
3
```

---

### Step 3

Compute:

```txt
Ways(4)
=
Ways(3)+Ways(2)

=
3+2

=
5
```

---

Final:

```txt
Step : Ways

1 : 1
2 : 2
3 : 3
4 : 5
```

---

# 6. Visual Execution

---

## Recursion Tree

For:

```txt
Ways(5)
```

```txt
                5
             /     \
            4       3
          /  \     / \
         3    2   2   1
       /  \
      2    1
```

Repeated nodes:

```txt
3
2
```

appear multiple times.

---

## Memoization

First visit:

```txt
Ways(3)
```

Store:

```txt
cache[3] = 3
```

Later:

```txt
Ways(3)
```

becomes:

```txt
Lookup
```

instead of:

```txt
Recompute
```

---

## Tabulation Table

```txt
Index

1  2  3  4  5

Value

1  2  3  5  8
```

Construction:

```txt
1
2
1+2=3
2+3=5
3+5=8
```

---

# 7. Python Lab

---

# Lab 1 — Observe Recursive Explosion

## Part A — Minimal Example

```python
def ways(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return ways(n - 1) + ways(n - 2)

print(ways(5))
```

---

## Part B — Guided Experiment

```python
call_count = 0

def ways(n):
    global call_count
    call_count += 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    return ways(n - 1) + ways(n - 2)

n = 10

answer = ways(n)

print("Answer:", answer)
print("Function calls:", call_count)
```

Try:

```python
n = 5
n = 10
n = 20
n = 30
```

Observe growth.

---

## Part C — Observation Questions

```txt
Why does call count grow so fast?

Which values are recomputed?

Can you identify repeated subproblems?
```

---

# Lab 2 — Memoization

## Part A — Runnable Example

```python
cache = {}

def ways(n):
    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n == 2:
        return 2

    cache[n] = ways(n - 1) + ways(n - 2)

    return cache[n]

print(ways(40))
```

---

## Part B — Experiment

```python
cache = {}

def ways(n):
    print("Computing:", n)

    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n == 2:
        return 2

    cache[n] = ways(n - 1) + ways(n - 2)

    return cache[n]

print(ways(10))
```

Watch:

```txt
Which numbers are computed once?
```

---

## Part C — Questions

```txt
What happens if cache is removed?

How many repeated computations return?

Why does performance improve?
```

---

# Lab 3 — Tabulation

## Runnable Example

```python
def ways(n):

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(ways(10))
```

---

## Experiment

Add:

```python
print(dp)
```

inside the loop.

Observe table growth.

---

## Questions

```txt
Why must dp[1] and dp[2] exist first?

What breaks if we start at i=2?

How does dp[i] depend on previous states?
```

---

# 8. Complexity Analysis

## Naive Recursion

Time:

```txt
O(2^N)
```

Reason:

```txt
Each call branches into two more calls.
```

---

Space:

```txt
O(N)
```

Reason:

```txt
Recursion depth.
```

---

## Memoization

Time:

```txt
O(N)
```

Reason:

```txt
Each state computed once.
```

---

Space:

```txt
O(N)
```

Reason:

```txt
Cache
+
Recursion stack
```

---

## Tabulation

Time:

```txt
O(N)
```

Reason:

```txt
One pass through states.
```

---

Space:

```txt
O(N)
```

Reason:

```txt
DP table
```

---

# 9. Common Mistakes

## Mistake 1

Memorizing:

```txt
dp[i]=dp[i-1]+dp[i-2]
```

without understanding why.

Always ask:

```txt
How can I arrive here?
```

---

## Mistake 2

Forgetting base cases.

Result:

```txt
Infinite recursion
```

or

```txt
Wrong table values
```

---

## Mistake 3

Thinking memoization and DP are different.

Memoization is DP.

Tabulation is DP.

They are two implementation styles.

---

## Mistake 4

Using recursion without checking for repeated work.

Always inspect:

```txt
Recursion Tree
```

for duplicates.

---

# 10. Knowledge Compression

---

# Key Takeaways

```txt
Large Problem
    ↓
Smaller Problems
    ↓
Repeated Problems
    ↓
Store Answers
    ↓
Reuse Answers
```

---

# Interview Recognition Signals

```txt
Count ways
    ↓
Recursive decomposition
    ↓
Overlapping subproblems
    ↓
Dynamic Programming
```

---

```txt
State
    ↓
Ways(n)

Transition
    ↓
Ways(n-1)+Ways(n-2)

Base Cases
    ↓
Ways(1)=1
Ways(2)=2
```

---

# One-Page Summary

```txt
Dynamic Programming

Goal:
Avoid repeated work.

Requirements:

1. Optimal substructure
   Large problem depends on
   smaller problems.

2. Overlapping subproblems
   Same questions appear repeatedly.

--------------------------------

Memoization

Top Down

Problem
    ↓
Subproblems
    ↓
Cache
    ↓
Reuse

Time: O(N)

--------------------------------

Tabulation

Bottom Up

Base Cases
    ↓
Fill Table
    ↓
Answer

Time: O(N)

--------------------------------

Staircase Problem

State:
Ways(i)

Meaning:
Number of ways to reach step i

Transition:
Ways(i)
=
Ways(i-1)+Ways(i-2)

Base Cases:
Ways(1)=1
Ways(2)=2

--------------------------------

Recognition Signals

✓ Count ways

✓ Answer depends on
  smaller answers

✓ Same subproblem repeats

✓ Recursive solution exists

=> Think Dynamic Programming
```
