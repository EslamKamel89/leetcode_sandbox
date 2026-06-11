# Study Guide — N-th Tribonacci Number

## Dynamic Programming Pattern: Constant Transition + Space Optimization

---

# 1. Section Overview

## What Is Being Taught?

At first glance, Tribonacci looks like a new problem.

But the entire purpose of this lesson is to show:

```txt
New problem
≠
New pattern
```

The course is teaching pattern recognition.

The staircase problem taught:

```txt
Current state
depends on
2 previous states
```

Tribonacci teaches:

```txt
Current state
depends on
3 previous states
```

The pattern itself has not changed.

Only the transition changed.

---

## Why This Matters

Many interview candidates learn problems.

Strong candidates learn patterns.

When an interviewer changes:

```txt
2 previous states
```

into

```txt
3 previous states
```

you should immediately think:

```txt
Same DP pattern.
Different transition.
```

That is exactly what this lesson is trying to teach.

---

## Problem Statement

The sequence starts as:

```txt
T(0) = 0
T(1) = 1
T(2) = 1
```

Every next value is:

```txt
T(n)
=
T(n-1)
+
T(n-2)
+
T(n-3)
```

Find:

```txt
T(n)
```

---

# 2. Core Concepts

---

# Concept 1 — State Definition

As with every DP problem:

Start by defining the state.

---

State:

```txt
T(i)
```

Meaning:

```txt
The Tribonacci value
at position i
```

---

Example:

```txt
T(4)
```

means:

```txt
Fourth Tribonacci number
```

Nothing more.

Nothing less.

---

# Concept 2 — Transition

The transition answers:

```txt
How is the current state built?
```

---

For Tribonacci:

```txt
T(i)
=
T(i-1)
+
T(i-2)
+
T(i-3)
```

Why?

Because the sequence definition says so.

---

This is exactly the same reasoning as:

```txt
Ways(n)
=
Ways(n-1)
+
Ways(n-2)
```

from Climbing Stairs.

Only one more dependency was added.

---

# Concept 3 — Base Cases

The recurrence cannot calculate:

```txt
T(0)
T(1)
T(2)
```

because they have no previous states.

So they must be given.

---

Base Cases:

```txt
T(0) = 0

T(1) = 1

T(2) = 1
```

---

Mental model:

```txt
These are the seeds.

Everything else grows from them.
```

---

# Concept 4 — Constant Transition DP

This is the first major DP family.

Recognition:

```txt
Current state
depends on
fixed number of previous states
```

Examples:

```txt
Fibonacci
Climbing Stairs
Tribonacci
Min Cost Climbing Stairs
House Robber
```

---

Visual:

```txt
dp[i]

← dp[i-1]
← dp[i-2]
← dp[i-3]
```

Fixed number.

Never changes.

---

# Concept 5 — Space Optimization

This is the main lesson of this section.

---

Most beginners stop here:

```txt
Store every answer.
```

Example:

```txt
0
1
1
2
4
7
13
24
...
```

inside an array.

---

But ask:

```txt
What do I actually need?
```

To compute:

```txt
T(10)
```

you only need:

```txt
T(9)
T(8)
T(7)
```

---

You do NOT need:

```txt
T(0)
T(1)
T(2)
```

anymore.

---

Mental Model:

Imagine a moving window.

```txt
Before

[0] [1] [1]

After

[1] [1] [2]

After

[1] [2] [4]

After

[2] [4] [7]
```

Only the last 3 values matter.

Everything older becomes irrelevant.

---

# 3. Mental Models

---

# Mental Model 1 — Rolling Memory

Imagine driving.

You need:

```txt
Current position
Previous position
Position before that
```

You don't need:

```txt
Position from 3 hours ago
```

---

Tribonacci works the same way.

Only recent history matters.

---

# Mental Model 2 — Conveyor Belt

Visual:

```txt
[a] [b] [c]
```

Create:

```txt
next = a+b+c
```

Slide belt:

```txt
[b] [c] [next]
```

Repeat.

---

DP is not storing the entire sequence.

It's maintaining enough information to continue.

---

# Mental Model 3 — State Compression

Array solution:

```txt
Store everything.
```

Optimized solution:

```txt
Store only
what future calculations need.
```

This is called:

```txt
State Compression
```

---

# 4. Pattern Recognition

---

# Recognition Signals

Look for:

```txt
dp[i]
depends on
few previous states
```

Examples:

```txt
dp[i-1]

dp[i-2]

dp[i-3]
```

---

Words often seen:

```txt
Nth value
Sequence
Ways
Cost
Profit
Score
```

---

# Recognition Checklist

During interviews:

```txt
□ Does current state depend on
  a fixed number of previous states?

□ Is there a natural left-to-right order?

□ Are base cases known?

□ Do old states become irrelevant?

□ Can memory be compressed?
```

If yes:

```txt
Constant Transition DP
```

---

# Similar Patterns

### Constant Transition

```txt
Look at 2-5 states.
```

Example:

```txt
Fibonacci
Tribonacci
House Robber
```

---

### Non-Constant Transition

```txt
Look at ALL previous states.
```

Example:

```txt
Longest Increasing Subsequence
```

Very different.

---

# 5. Step-by-Step Walkthrough

Find:

```txt
T(5)
```

---

Known:

```txt
T(0)=0

T(1)=1

T(2)=1
```

---

Compute:

```txt
T(3)

=
1+1+0

=
2
```

---

Compute:

```txt
T(4)

=
T(3)+T(2)+T(1)

=
2+1+1

=
4
```

---

Compute:

```txt
T(5)

=
T(4)+T(3)+T(2)

=
4+2+1

=
7
```

---

Result:

```txt
Index : Value

0 : 0
1 : 1
2 : 1
3 : 2
4 : 4
5 : 7
```

---

# 6. Visual Execution

---

# Array Version

```txt
Index

0 1 2 3 4 5

Value

0 1 1 2 4 7
```

Construction:

```txt
0
1
1

0+1+1 = 2

1+1+2 = 4

1+2+4 = 7
```

---

# Rolling Variables Version

Start:

```txt
t0=0
t1=1
t2=1
```

---

Iteration 1

```txt
next = 0+1+1

next = 2
```

Update:

```txt
0 1 1

↓

1 1 2
```

---

Iteration 2

```txt
next = 1+1+2

next = 4
```

Update:

```txt
1 1 2

↓

1 2 4
```

---

Iteration 3

```txt
next = 1+2+4

next = 7
```

Update:

```txt
1 2 4

↓

2 4 7
```

---

# 7. Python Lab

---

# Lab 1 — Build Tribonacci Table

## Part A — Minimal Example

```python
def tribonacci(n):

    if n == 0:
        return 0

    if n <= 2:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

print(tribonacci(5))
```

Output:

```txt
7
```

---

## Part B — Guided Experiment

```python
def tribonacci(n):

    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    if n >= 2:
        dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        print(
            f"i={i}",
            "table=",
            dp[:i+1]
        )

    return dp[n]

print(tribonacci(10))
```

---

## Part C — Observation Questions

```txt
Which values are used to build T(7)?

Does T(0) matter when computing T(10)?

Why not?
```

---

# Lab 2 — Space Optimization

## Runnable Code

```python
def tribonacci(n):

    if n == 0:
        return 0

    if n <= 2:
        return 1

    t0 = 0
    t1 = 1
    t2 = 1

    for _ in range(3, n + 1):

        nxt = t0 + t1 + t2

        t0, t1, t2 = t1, t2, nxt

    return t2

print(tribonacci(10))
```

---

## Experiment

Add:

```python
print(t0, t1, t2)
```

inside loop.

Watch:

```txt
How the window moves.
```

---

## Questions

```txt
Why can t0 be discarded?

What information is lost?

Why doesn't it matter?
```

---

# 8. Full Runnable Code

## Optimal Solution

```python
def tribonacci(n):
    """
    O(n) time
    O(1) space
    """

    if n == 0:
        return 0

    if n <= 2:
        return 1

    t0 = 0
    t1 = 1
    t2 = 1

    for _ in range(3, n + 1):

        nxt = t0 + t1 + t2

        t0, t1, t2 = t1, t2, nxt

    return t2


n = 10

print("Tribonacci:", tribonacci(n))
```

---

# 9. Complexity Analysis

---

## DP Array

Time:

```txt
O(n)
```

Why?

```txt
One pass through sequence.
```

---

Space:

```txt
O(n)
```

Why?

```txt
Store every state.
```

---

## Optimized Version

Time:

```txt
O(n)
```

Still:

```txt
Need to generate
all previous values.
```

---

Space:

```txt
O(1)
```

Why?

```txt
Only 3 variables.
```

No growth with n.

---

# 10. Common Mistakes

---

## Mistake 1

Seeing Tribonacci as a new pattern.

Wrong:

```txt
New problem
=
new technique
```

Correct:

```txt
Same pattern
Different transition
```

---

## Mistake 2

Storing entire array unnecessarily.

Ask:

```txt
Which states are actually needed?
```

---

## Mistake 3

Forgetting base cases.

Without:

```txt
T(0)
T(1)
T(2)
```

the recurrence cannot start.

---

## Mistake 4

Updating variables in wrong order.

Wrong:

```python
t0 = t1
t1 = t2
t2 = t0 + t1 + t2
```

Because:

```txt
Old values are lost.
```

Use tuple assignment.

---

# 11. Knowledge Compression

---

# Key Takeaways

```txt
Sequence
    ↓
State Definition

T(i)
    ↓

Depends On

T(i-1)
T(i-2)
T(i-3)
    ↓

Constant Transition DP
    ↓

Store only needed states
    ↓

O(1) Space
```

---

# Interview Recognition Signals

```txt
Problem says:

Current value
depends on
fixed number
of previous values
```

↓

```txt
Constant Transition DP
```

↓

```txt
State

dp[i]
```

↓

```txt
Transition

dp[i]
=
previous states
```

↓

```txt
Check if
space optimization
is possible
```

---

# One-Page Summary

```txt
N-th Tribonacci Number

State:

T(i)

Meaning:

Value at position i

--------------------------------

Base Cases

T(0)=0
T(1)=1
T(2)=1

--------------------------------

Transition

T(i)
=
T(i-1)
+
T(i-2)
+
T(i-3)

--------------------------------

Pattern

Constant Transition DP

--------------------------------

Observation

Only last 3 states matter

--------------------------------

Optimization

Array:
O(n) space

Rolling Variables:
O(1) space

--------------------------------

Recognition Signal

Current state
depends on
fixed number
of previous states

⇒ Constant Transition DP
```
