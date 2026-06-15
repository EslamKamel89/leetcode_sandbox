Excellent. This is the second core DP pattern:

```txt
Climbing Stairs  -> Counting DP
House Robber     -> Decision DP
```

The transition is no longer:

```txt
How many ways?
```

but:

```txt
Take?
or
Skip?
```

This distinction is extremely important.

---

# Step 1 — Pattern Prediction

## Recognition Signals

We see:

```txt
Maximum amount
```

and

```txt
Cannot take adjacent houses
```

This immediately suggests:

```txt
A decision at each position affects future positions.
```

---

## Why DP?

Suppose we're at house `i`.

We have two choices:

```txt
Take house i
```

or

```txt
Skip house i
```

The same question keeps appearing:

```txt
What is the best profit starting from here?
```

or

```txt
What is the best profit up to here?
```

Repeated optimal subproblems → DP.

---

# State Definition

Your solution implicitly uses:

```txt
dp[i]
=
maximum money obtainable
from houses [0..i]
```

This is the most common state for House Robber.

---

# Transition Derivation

This is the part people often memorize.

Let's derive it.

For house `i`:

## Option 1 — Skip

If we skip house `i`:

```txt
answer = dp[i-1]
```

because nothing changes.

---

## Option 2 — Take

If we rob house `i`:

```txt
nums[i]
```

is gained.

But:

```txt
i-1
```

cannot be robbed.

So the best previous profit comes from:

```txt
dp[i-2]
```

Therefore:

```txt
answer = nums[i] + dp[i-2]
```

---

Combine both:

```txt
dp[i]
=
max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

This is the entire pattern.

---

# Understanding Your Variables

You compressed the DP table.

---

## Initial State

```python
prev2 = nums[0]
```

Represents:

```txt
dp[0]
```

---

```python
prev1 = max(nums[1], prev2)
```

Represents:

```txt
dp[1]
```

Because:

```txt
House 0
or
House 1
```

You can only choose one.

---

# The Loop

```python
for i in range(2, len(nums)):
```

At the beginning of each iteration:

```txt
prev2 = dp[i-2]
prev1 = dp[i-1]
```

This invariant is the key to understanding the code.

---

## Current State

```python
max(nums[i] + prev2, prev1)
```

is:

```txt
max(
    take current,
    skip current
)
```

or:

```txt
max(
    nums[i] + dp[i-2],
    dp[i-1]
)
```

Exactly the recurrence.

---

## Simultaneous Assignment

```python
prev2, prev1 = prev1, max(nums[i] + prev2, prev1)
```

After this line:

```txt
prev2 = old dp[i-1]
prev1 = dp[i]
```

So the invariant remains true for the next iteration.

---

# Visual Execution

Input:

```txt
[2,7,9,3,1]
```

---

Initialization:

```txt
prev2 = 2
prev1 = 7
```

Meaning:

```txt
dp[0] = 2
dp[1] = 7
```

---

## i = 2

House value:

```txt
9
```

Take:

```txt
9 + dp[0]
=
9 + 2
=
11
```

Skip:

```txt
dp[1]
=
7
```

Choose:

```txt
11
```

Update:

```txt
prev2 = 7
prev1 = 11
```

---

## i = 3

Value:

```txt
3
```

Take:

```txt
3 + 7
=
10
```

Skip:

```txt
11
```

Choose:

```txt
11
```

Update:

```txt
prev2 = 11
prev1 = 11
```

---

## i = 4

Value:

```txt
1
```

Take:

```txt
1 + 11
=
12
```

Skip:

```txt
11
```

Choose:

```txt
12
```

Final:

```txt
12
```

---

# Why This Pattern Matters

Climbing Stairs taught:

```txt
Current answer
=
combine previous answers
```

House Robber teaches:

```txt
Current answer
=
best decision among choices
```

This exact pattern reappears in:

```txt
House Robber II
House Robber III
Stock Problems
Delete and Earn
Weighted Scheduling
Many Interview DP Problems
```

---

# Pattern Extraction

### Trigger

```txt
Maximum / Minimum value
+
Mutually exclusive choices
```

---

### Pattern

```txt
Decision DP
(Take / Skip)
```

---

### State

```txt
dp[i]
=
best answer considering houses [0..i]
```

---

### Transition

```txt
dp[i]
=
max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

---

### Flow

```txt
At each position:
    Skip current
        OR
    Take current

Choose the better result
```

---

One question before moving on:

For House Robber, why is this state valid?

```txt
dp[i] = best profit from houses [0..i]
```

Why don't we need to remember _which houses_ were robbed to compute future states? This question gets to the heart of why DP works here.
