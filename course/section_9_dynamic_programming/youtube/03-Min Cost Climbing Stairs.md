# Study Guide — Min Cost Climbing Stairs

## Dynamic Programming Pattern: Constant Transition DP

---

# 1. Section Overview

## What Is Being Taught?

This lesson is extremely important because it teaches the transition from:

```txt
Counting DP
```

to

```txt
Optimization DP
```

Up until now:

```txt
Climbing Stairs
```

asked:

```txt
How many ways exist?
```

Now:

```txt
Min Cost Climbing Stairs
```

asks:

```txt
What is the cheapest way?
```

The problem changed.

The DP pattern did not.

That is the entire lesson.

---

## Why This Matters

Many people learn DP like this:

```txt
Climbing Stairs
=
one formula

House Robber
=
another formula

Coin Change
=
another formula
```

Strong interview candidates think:

```txt
What state am I storing?
```

because changing:

```txt
count ways
```

into

```txt
minimum cost
```

changes only:

```txt
State meaning
```

not the overall DP structure.

---

# The Most Important Insight

Compare:

### Climbing Stairs

State:

```txt
dp[i]
=
number of ways
to reach stair i
```

Transition:

```txt
dp[i]
=
dp[i-1]
+
dp[i-2]
```

---

### Min Cost Climbing Stairs

State:

```txt
dp[i]
=
minimum cost
to reach stair i
```

Transition:

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

Same staircase.

Same movement rules.

Different meaning of the state.

This is how DP evolves.

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
dp[i]
```

Meaning:

```txt
Minimum cost
required to land
on stair i
```

Notice:

```txt
LAND on stair i
```

not

```txt
Reach the floor
```

This distinction is important.

---

Example:

```txt
dp[4]
```

means:

```txt
Cheapest possible way
to stand on stair 4
```

---

# Concept 2 — The Floor Is Special

A common source of confusion.

The floor:

```txt
Top
```

is NOT a stair.

---

Visual:

```txt
Floor
  ↑

Step 4
Step 3
Step 2
Step 1
Step 0
```

---

You pay for:

```txt
Step 0
Step 1
Step 2
...
```

You do NOT pay for:

```txt
Floor
```

---

This is why the final answer becomes:

```txt
min(
    dp[n-1],
    dp[n-2]
)
```

because:

```txt
From either of them
you can jump
to the floor.
```

---

# Concept 3 — Transition Logic

Ask:

```txt
How can I arrive
at stair i?
```

Only two possibilities:

```txt
i-1
i-2
```

Exactly like Climbing Stairs.

---

But now we care about:

```txt
Cheapest route.
```

So choose:

```txt
minimum(
    previous options
)
```

instead of:

```txt
sum(
    previous options
)
```

---

Transition:

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

# Why This Works

To stand on stair:

```txt
i
```

you must:

1. Reach either

```txt
i-1
```

or

```txt
i-2
```

2. Pay the current stair cost

```txt
cost[i]
```

3. Choose the cheaper path

Hence:

```txt
cost[i]
+
min(previous)
```

---

# Concept 4 — Base Cases

You may start from:

```txt
stair 0
```

or

```txt
stair 1
```

---

Therefore:

```txt
dp[0]
=
cost[0]

dp[1]
=
cost[1]
```

These are immediately known.

---

Mental model:

```txt
You are allowed
to begin there.

No previous journey exists.
```

---

# 3. Mental Models

---

# Mental Model 1 — Cheapest Route Map

Imagine every stair is a city.

Each city has a toll.

```txt
City 0 = $10

City 1 = $15

City 2 = $20
```

To reach City 2:

```txt
Come from City 1
or
Come from City 0
```

Choose:

```txt
Cheapest route so far
```

then pay the new toll.

---

# Mental Model 2 — Water Flow

Think of cost flowing upward.

```txt
          20
         /
10 ---- 20
 \
  15
```

The cheapest accumulated cost propagates upward.

---

# Mental Model 3 — Local Decisions Built on Global Decisions

A beginner often thinks:

```txt
Choose the cheaper stair.
```

Wrong.

We choose:

```txt
Cheaper PATH.
```

Example:

```txt
Current stair cost
might be small

but route leading to it
might be expensive.
```

DP stores:

```txt
best path so far
```

not just local values.

---

# 4. Pattern Recognition

---

# Recognition Signals

Look for:

```txt
Minimum cost
Minimum steps
Minimum effort
Minimum energy
Cheapest path
```

combined with:

```txt
Current state depends
on fixed previous states
```

---

Example Signals

```txt
You can move
1 step or 2 steps
```

or

```txt
Current answer depends
only on previous 2 positions
```

---

# Recognition Checklist

```txt
□ Need minimum value?

□ State depends on
  fixed previous states?

□ Natural left-to-right order?

□ Previous states already solve
  smaller versions?

□ Same transition everywhere?
```

If yes:

```txt
Constant Transition DP
```

---

# Distinguishing from Climbing Stairs

Climbing Stairs:

```txt
Count all possibilities
```

Transition:

```txt
+
```

---

Min Cost Climbing Stairs:

```txt
Choose best possibility
```

Transition:

```txt
min(...)
```

---

# 5. Step-by-Step Walkthrough

Example:

```txt
cost =

[10, 15, 20]
```

---

Base:

```txt
dp[0] = 10

dp[1] = 15
```

---

Compute stair 2:

```txt
dp[2]

=
20
+
min(10,15)

=
20+10

=
30
```

---

DP table:

```txt
10
15
30
```

---

Now floor:

Can be reached from:

```txt
stair 1
or
stair 2
```

Choose:

```txt
min(15,30)
```

---

Answer:

```txt
15
```

---

# Larger Example

```txt
cost

[1,100,1,1]
```

---

Base:

```txt
dp[0]=1

dp[1]=100
```

---

Stair 2:

```txt
1 + min(1,100)

=
2
```

---

Stair 3:

```txt
1 + min(100,2)

=
3
```

---

Table:

```txt
1
100
2
3
```

---

Answer:

```txt
min(2,3)

=
2
```

---

# 6. Visual Execution

---

# DP Table Construction

Example:

```txt
cost

[10,15,20,5]
```

---

Initialize:

```txt
Index

0   1   2   3

DP

10  15
```

---

Compute 2

```txt
20 + min(10,15)

=
30
```

---

Table:

```txt
10 15 30
```

---

Compute 3

```txt
5 + min(15,30)

=
20
```

---

Table:

```txt
10 15 30 20
```

---

Floor:

```txt
min(30,20)

=
20
```

---

# Visual State Flow

```txt
dp[i]

      dp[i-2]
          \
           \
            min()
           /
          /
      dp[i-1]

            +
        cost[i]

            ↓

         dp[i]
```

---

# 7. Python Lab

---

# Lab 1 — Build DP Table

## Part A — Minimal Example

```python
def min_cost(cost):

    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(
            dp[i - 1],
            dp[i - 2]
        )

    return min(dp[-1], dp[-2])


print(min_cost([10,15,20]))
```

---

## Part B — Guided Experiment

```python
def min_cost(cost):

    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    print("start:", dp)

    for i in range(2, n):

        dp[i] = cost[i] + min(
            dp[i - 1],
            dp[i - 2]
        )

        print(
            f"step={i}",
            dp
        )

    return min(dp[-1], dp[-2])


print(
    min_cost(
        [1,100,1,1,100,1]
    )
)
```

---

## Part C — Observation Questions

```txt
Which previous state was chosen?

Why wasn't the larger cost chosen?

What happens if min()
becomes max()?
```

---

# Lab 2 — Observe Space Optimization

```python
cost = [1,100,1,1,100,1]

prev2 = cost[0]
prev1 = cost[1]

print(prev2, prev1)

for i in range(2, len(cost)):

    current = cost[i] + min(
        prev1,
        prev2
    )

    print(
        "new =", current
    )

    prev2, prev1 = prev1, current

print(
    min(prev1, prev2)
)
```

---

Questions:

```txt
Why is prev2 no longer needed?

At which point does old information become irrelevant?

Why can the entire DP array be removed?
```

---

# 8. Full Runnable Code

## Optimal O(1) Space Solution

```python
def min_cost_climbing_stairs(cost):

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):

        current = cost[i] + min(
            prev1,
            prev2
        )

        prev2, prev1 = (
            prev1,
            current
        )

    return min(
        prev1,
        prev2
    )


cost = [10,15,20]

print(
    min_cost_climbing_stairs(cost)
)
```

---

# 9. Complexity Analysis

## DP Array Version

Time:

```txt
O(n)
```

Reason:

```txt
Single pass.
```

---

Space:

```txt
O(n)
```

Reason:

```txt
Store every state.
```

---

## Optimized Version

Time:

```txt
O(n)
```

Nothing changes.

---

Space:

```txt
O(1)
```

Because:

```txt
Only two states exist
at any moment.
```

---

# 10. Constant Transition Pattern

This section introduces one of the most important DP families.

---

Pattern Definition

```txt
Current state
depends on
constant number
of previous states.
```

Examples:

```txt
Climbing Stairs

Tribonacci

Min Cost Climbing Stairs

House Robber
```

---

Generic Form

```txt
dp[i]

depends on

dp[i-1]
dp[i-2]
...
dp[i-k]
```

where:

```txt
k
=
constant
```

---

# Recognition Signal

Immediately ask:

```txt
How many previous states
are required?
```

If answer is:

```txt
2
3
4
```

and never grows:

```txt
Think Constant Transition DP
```

---

# Space Optimization Rule

If:

```txt
dp[i]
```

needs only:

```txt
dp[i-1]
dp[i-2]
```

then:

```txt
Full array
↓
Two variables
```

---

If:

```txt
dp[i]
```

needs:

```txt
3 states
```

then:

```txt
Three variables
```

---

General Rule:

```txt
Need k previous states

↓

Store k variables

↓

O(1) space
```

---

# 11. Knowledge Compression

## Key Takeaways

```txt
State

dp[i]
=
minimum cost
to reach stair i

        ↓

Transition

cost[i]
+
min(
    dp[i-1],
    dp[i-2]
)

        ↓

Constant Transition DP

        ↓

Only last two states matter

        ↓

Space Optimization
```

---

## Interview Recognition Signals

```txt
Minimum Cost
        ↓

Depends on
fixed previous states
        ↓

State Definition
        ↓

dp[i]
=
best answer at i
        ↓

Transition
        ↓

Choose best previous state
        ↓

Consider O(1) space
```

---

## One-Page Summary

```txt
Min Cost Climbing Stairs

State

dp[i]
=
minimum cost
to reach stair i

Base Cases

dp[0]=cost[0]
dp[1]=cost[1]

Transition

dp[i]
=
cost[i]
+
min(
    dp[i-1],
    dp[i-2]
)

Answer

min(
    dp[n-1],
    dp[n-2]
)

Pattern

Constant Transition DP

Recognition

Current state
depends on
fixed number
of previous states

Optimization

Array
↓
Two Variables

O(n) space
↓
O(1) space
```
