# Study Guide — House Robber

## Dynamic Programming Pattern: Constant Transition + Take/Skip Decision

---

# 1. Section Overview

## What Is Being Taught?

This lesson introduces the first major variation of Constant Transition DP.

Previous problems were:

```txt
Climbing Stairs
    ↓
Count ways

Tribonacci
    ↓
Generate sequence

Min Cost Climbing Stairs
    ↓
Minimize cost
```

House Robber introduces:

```txt
Optimization Through Decisions
```

Specifically:

```txt
Take
or
Skip
```

This idea appears everywhere in DP.

---

## Why This Problem Matters

Many interview DP questions can be reduced to:

```txt
At position i

Should I use this element?

or

Should I ignore it?
```

House Robber is the simplest and most important version of that pattern.

---

# The Real Problem

The story about robbing houses is irrelevant.

The actual problem is:

```txt
Choose numbers

such that

No two adjacent numbers
are chosen

while maximizing
the total sum
```

---

Example:

```txt
[2,7,9,3,1]
```

Valid:

```txt
2 + 9 + 1 = 12
```

Invalid:

```txt
7 + 9
```

because:

```txt
Adjacent
```

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
Maximum money
that can be robbed

from houses

0...i
```

This is the most important sentence in the problem.

---

Example:

```txt
dp[4]
```

means:

```txt
Best possible robbery plan

using houses

0 through 4
```

---

Notice:

```txt
Not:

money in house 4

Not:

money after robbing house 4
```

Instead:

```txt
Best answer up to 4
```

Huge difference.

---

# Concept 2 — The Two Choices

When standing at house:

```txt
i
```

there are only two possibilities.

---

Option 1

Skip current house.

```txt
House i
not robbed
```

Then:

```txt
Answer stays:

dp[i-1]
```

because nothing changed.

---

Option 2

Rob current house.

Because adjacent houses are forbidden:

```txt
i-1
```

cannot be robbed.

Therefore:

```txt
Best previous answer

must come from

i-2
```

Result:

```txt
dp[i-2]
+
nums[i]
```

---

# Concept 3 — Choosing the Better Decision

We now have:

```txt
Skip

dp[i-1]
```

and

```txt
Take

dp[i-2] + nums[i]
```

Which one should we choose?

---

Obviously:

```txt
Maximum
```

Therefore:

```txt
dp[i]
=
max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

This is the entire problem.

---

# Why This Formula Works

Every possible valid robbery plan must belong to one of two categories:

```txt
Current house robbed
```

or

```txt
Current house skipped
```

No third option exists.

---

Therefore:

```txt
Best answer
=
best of those two categories
```

which is exactly what the formula computes.

---

# Concept 4 — Base Cases

---

First house:

```txt
dp[0]
=
nums[0]
```

Only one option.

---

Second house:

Choose:

```txt
House 0
```

or

```txt
House 1
```

but not both.

---

Therefore:

```txt
dp[1]
=
max(
    nums[0],
    nums[1]
)
```

---

These are the foundations of the entire table.

---

# 3. Mental Models

---

# Mental Model 1 — Security Cameras

Imagine every house has a camera connected to neighbors.

Rob:

```txt
House i
```

and the camera automatically blocks:

```txt
House i-1
```

and

```txt
House i+1
```

---

Therefore every decision creates constraints.

---

# Mental Model 2 — Take or Skip

Every position asks:

```txt
Take?
```

or

```txt
Skip?
```

---

Visual:

```txt
House i

      Take
     /
Current
     \
      Skip
```

---

Almost all decision-based DP problems use this idea.

---

# Mental Model 3 — Best Plan So Far

Think of:

```txt
dp[i]
```

as:

```txt
My best robbery strategy
up to this point.
```

Not:

```txt
Money inside house i
```

This distinction is critical.

---

# 4. Pattern Recognition

---

# Recognition Signals

Words like:

```txt
Maximum
```

or

```txt
Best
```

or

```txt
Largest
```

combined with:

```txt
Restrictions
```

---

Examples:

```txt
Maximum profit

Maximum score

Maximum money

Maximum points
```

---

and especially:

```txt
Choose element

or

Skip element
```

---

# Recognition Checklist

During interviews:

```txt
□ Am I choosing elements?

□ Is there a constraint?

□ Do I have a Take/Skip decision?

□ Does current answer depend
  on fixed previous states?

□ Am I maximizing something?
```

If yes:

```txt
Decision DP
```

inside:

```txt
Constant Transition DP
```

---

# Distinguishing From Previous Problems

---

Climbing Stairs

```txt
Combine all paths
```

Transition:

```txt
+
```

---

Min Cost Climbing Stairs

```txt
Choose cheaper path
```

Transition:

```txt
min()
```

---

House Robber

```txt
Choose richer path
```

Transition:

```txt
max()
```

---

Notice the pattern:

```txt
Same DP structure

Different operation
```

---

# 5. Step-by-Step Walkthrough

Example:

```txt
nums

[2,7,9,3,1]
```

---

Base Cases

```txt
dp[0]=2

dp[1]=7
```

because:

```txt
max(2,7)=7
```

---

House 2

Value:

```txt
9
```

---

Skip:

```txt
dp[1]
=
7
```

---

Take:

```txt
dp[0]
+
9

=
11
```

---

Choose:

```txt
max(7,11)

=
11
```

---

Table:

```txt
2
7
11
```

---

House 3

Value:

```txt
3
```

---

Skip:

```txt
11
```

---

Take:

```txt
7 + 3

=
10
```

---

Choose:

```txt
11
```

---

Table:

```txt
2
7
11
11
```

---

House 4

Value:

```txt
1
```

---

Skip:

```txt
11
```

---

Take:

```txt
11 + 1

=
12
```

---

Choose:

```txt
12
```

---

Final Table

```txt
2
7
11
11
12
```

---

Answer:

```txt
12
```

---

# 6. Visual Execution

---

# DP Table Construction

```txt
nums

[2,7,9,3,1]
```

---

Start

```txt
dp

[2,7]
```

---

House 2

```txt
max(
    7,
    2+9
)

=
11
```

---

Table

```txt
[2,7,11]
```

---

House 3

```txt
max(
    11,
    7+3
)

=
11
```

---

Table

```txt
[2,7,11,11]
```

---

House 4

```txt
max(
    11,
    11+1
)

=
12
```

---

Table

```txt
[2,7,11,11,12]
```

---

# Decision Tree View

At every house:

```txt
Current House

      Skip
       |
       v

     dp[i-1]

OR

      Take
       |
       v

dp[i-2]+nums[i]
```

---

Then:

```txt
Take maximum
```

---

# 7. Python Lab

---

# Lab 1 — Build the DP Table

## Part A — Minimal Example

```python
def rob(nums):

    n = len(nums)

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):

        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + nums[i]
        )

    return dp[-1]


print(
    rob([2,7,9,3,1])
)
```

---

## Part B — Guided Experiment

```python
def rob(nums):

    n = len(nums)

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    print(dp)

    for i in range(2, n):

        skip = dp[i - 1]
        take = dp[i - 2] + nums[i]

        dp[i] = max(
            skip,
            take
        )

        print(
            f"house={i}",
            f"take={take}",
            f"skip={skip}",
            f"dp={dp}"
        )

    return dp[-1]


print(
    rob([2,7,9,3,1])
)
```

---

## Part C — Observation Questions

```txt
Which decision won?

Take or Skip?

Why?

When does Skip beat Take?

When does Take beat Skip?
```

---

# Lab 2 — Space Optimization

Observe:

```txt
dp[i]
depends only on

dp[i-1]
dp[i-2]
```

---

Runnable Example

```python
def rob(nums):

    prev2 = nums[0]

    prev1 = max(
        nums[0],
        nums[1]
    )

    for i in range(2, len(nums)):

        current = max(
            prev1,
            prev2 + nums[i]
        )

        prev2, prev1 = (
            prev1,
            current
        )

    return prev1


print(
    rob([2,7,9,3,1])
)
```

---

## Questions

```txt
Why can dp[0]
be forgotten?

Why can dp[1]
be forgotten?

Which states are truly needed?
```

---

# 8. Full Runnable Code

## Optimal Solution

```python
def rob(nums):

    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]

    prev1 = max(
        nums[0],
        nums[1]
    )

    for i in range(2, len(nums)):

        current = max(
            prev1,
            prev2 + nums[i]
        )

        prev2, prev1 = (
            prev1,
            current
        )

    return prev1


houses = [2,7,9,3,1]

print(
    rob(houses)
)
```

---

# 9. Complexity Analysis

## DP Array Version

Time:

```txt
O(n)
```

One pass.

---

Space:

```txt
O(n)
```

Entire table stored.

---

## Optimized Version

Time:

```txt
O(n)
```

Unchanged.

---

Space:

```txt
O(1)
```

Only:

```txt
prev1
prev2
```

are stored.

---

# 10. Common Mistakes

---

## Mistake 1

Thinking:

```txt
Take larger house.
```

Greedy.

Wrong.

---

Example:

```txt
[2,1,1,2]
```

Best answer:

```txt
2+2=4
```

not:

```txt
Take biggest visible house.
```

---

## Mistake 2

Wrong State Meaning

Incorrect:

```txt
dp[i]
=
money in house i
```

Correct:

```txt
dp[i]
=
best answer up to i
```

---

## Mistake 3

Forgetting Take/Skip

Every house creates exactly two decisions.

If your formula doesn't contain:

```txt
Take

or

Skip
```

you're probably missing the pattern.

---

# 11. Knowledge Compression

## Key Takeaways

```txt
House i
    ↓

Take
or
Skip

    ↓

Skip

dp[i-1]

Take

dp[i-2]
+
nums[i]

    ↓

Choose Maximum

    ↓

dp[i]
```

---

## Interview Recognition Signals

```txt
Maximum value
        ↓

Choose elements
        ↓

Constraint exists
        ↓

Take / Skip decision
        ↓

dp[i]
=
best answer up to i
        ↓

max(
    skip,
    take
)
```

---

## One-Page Summary

```txt
House Robber

State

dp[i]
=
maximum money
from houses [0..i]

--------------------------------

Base Cases

dp[0]=nums[0]

dp[1]
=
max(
    nums[0],
    nums[1]
)

--------------------------------

Transition

Skip

dp[i-1]

Take

dp[i-2]
+
nums[i]

dp[i]
=
max(
    dp[i-1],
    dp[i-2]+nums[i]
)

--------------------------------

Pattern

Constant Transition DP

Decision DP

--------------------------------

Recognition

Take / Skip

Maximum Value

Non-Adjacent Constraint

--------------------------------

Optimization

Store only

dp[i-1]
dp[i-2]

Space

O(n)
↓
O(1)
```

This problem is the first time DP becomes a **decision-making system** rather than a counting or cost-accumulation system. That idea reappears later in House Robber II, House Robber III, Stock DP, and many other interview problems.
