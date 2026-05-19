# Step 1 — Pattern Prediction

Before touching the code, we identify the pattern.

---

# What Pattern Is This?

## Pattern

```txt id="0tmokm"
Classic Binary Search
```

This is the most fundamental binary search problem.

---

# Why Does This Pattern Apply?

Because the problem gives us the critical property:

```txt id="m4l4hk"
nums is sorted in ascending order
```

That single sentence changes everything.

Without sorting:

```txt id="tbbgvi"
You must inspect elements one-by-one
→ O(n)
```

With sorting:

```txt id="93pbqg"
One comparison lets us eliminate HALF the array
→ O(log n)
```

That is the core leverage of binary search.

---

# Recognition Signals

This problem contains several strong signals:

| Signal                      | Meaning                   |
| --------------------------- | ------------------------- |
| "sorted in ascending order" | ordered search space      |
| "search target"             | exact lookup              |
| "O(log n)"                  | binary search is expected |

The runtime requirement is especially important.

Whenever you see:

```txt id="5d1oq3"
O(log n)
```

you should immediately think:

```txt id="v4rjlwm"
Binary Search candidate
```

because logarithmic complexity almost always means:

```txt id="7ndg3w"
divide the search space repeatedly
```

---

# Mental Model

You are NOT “searching every element faster.”

You are:

```txt id="n3vjpm"
proving large regions impossible
```

Suppose:

```txt id="lcw9re"
[-1, 0, 3, 5, 9, 12]
```

Target:

```txt id="5zjlwm"
9
```

If middle element is:

```txt id="g64mj2"
3
```

Then because the array is sorted:

```txt id="i1i22e"
everything LEFT of 3
is also < 9
```

So the entire left side becomes impossible.

You discard it instantly.

That is the real power.

---

# Search Space

Binary Search is always about maintaining a valid search space.

Initially:

```txt id="c1ceux"
entire array
```

represented by:

```python
l = 0
r = len(nums) - 1
```

Meaning:

```txt id="y9ylkn"
target MAY exist between l and r
```

Every iteration shrinks this region.

---

# Why Middle Matters

The middle element acts like a decision checkpoint.

We compare:

```python
nums[m]
```

against:

```python
target
```

This tells us WHICH HALF remains possible.

---

# Core Invariant

This is the invariant we maintain throughout the algorithm:

```txt id="h6on9m"
If target exists,
it must remain inside [l, r]
```

Every update must preserve this truth.

This is the heart of correct binary search.

---

# Step 2 — Solution Reconstruction

Now we build the algorithm gradually.

---

# Step 2.1 — Define the Search Space

```python
l, r = 0, len(nums) - 1
```

## What This Does

Defines the current candidate region.

Initially:

```txt id="8k2xot"
search everywhere
```

---

## Why It Exists

We need boundaries that shrink over time.

Binary search is impossible without:

```txt id="mqlowc"
a shrinking interval
```

---

## Why `len(nums) - 1`?

Because arrays are zero-indexed.

Example:

```txt id="gcztcw"
length = 6
valid indices = 0 → 5
```

---

# Step 2.2 — Continue While Search Space Exists

```python
while l <= r:
```

---

## What This Means

As long as:

```txt id="tr0x5w"
there is still at least one candidate position
```

continue searching.

---

# Why `<=` and NOT `<`?

Very important.

Suppose:

```txt id="th4n4u"
l == r
```

That means:

```txt id="0bkrvx"
ONE candidate remains
```

We must still check it.

If you wrote:

```python
while l < r:
```

you would skip the final element.

This is one of the most common binary search bugs.

---

# Step 2.3 — Compute Middle

```python
m = (l + r) // 2
```

---

## What This Does

Finds the midpoint of the current search space.

---

## Why Middle?

Because checking the middle lets us eliminate HALF the possibilities.

---

## Why Integer Division?

Indices must be integers.

Example:

```txt id="4u5ks0"
(0 + 5) // 2 = 2
```

---

# Step 2.4 — Compare Against Target

```python
if nums[m] > target:
```

---

## What This Means

Middle value is TOO BIG.

Since array is sorted:

```txt id="88o3z0"
everything RIGHT of m
is even bigger
```

So:

```txt id="pq2jvx"
right side becomes impossible
```

---

# Step 2.5 — Shrink Right Side

```python
r = m - 1
```

---

## Why `m - 1`?

Because:

```txt id="srdn1t"
we already checked m
```

and know it is not the answer.

Keeping it would risk infinite loops.

---

# Step 2.6 — Middle Too Small

```python
elif nums[m] < target:
```

---

## Meaning

Middle value is TOO SMALL.

Since array is sorted:

```txt id="g9t0m7"
everything LEFT of m
is also too small
```

So left side becomes impossible.

---

# Step 2.7 — Shrink Left Side

```python
l = m + 1
```

---

## Why `m + 1`?

Again:

```txt id="0hrc9l"
m was already proven incorrect
```

So we exclude it.

---

# Step 2.8 — Found Target

```python
else:
    return m
```

---

## Meaning

```txt id="c8l37n"
nums[m] == target
```

We found the answer.

---

# Step 2.9 — Exhausted Search Space

```python
return -1
```

---

## Meaning

Eventually:

```txt id="mjlwm0"
l > r
```

This means:

```txt id="e6fifn"
no valid region remains
```

So target does not exist.

---

# Step 3 — Full Solution

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1

            elif nums[m] < target:
                l = m + 1

            else:
                return m

        return -1
```

---

# Step 4 — Visual Execution

Input:

```txt id="4s50a8"
nums = [-1,0,3,5,9,12]
target = 9
```

---

# Iteration 1

## State

```txt id="i7zlpn"
l = 0
r = 5
```

## Middle

```txt id="d02yv7"
m = 2
nums[m] = 3
```

Compare:

```txt id="ls5fj0"
3 < 9
```

Meaning:

```txt id="g7w7jv"
left half impossible
```

Update:

```txt id="fl0m6m"
l = 3
```

---

# Iteration 2

## State

```txt id="gw2u6d"
l = 3
r = 5
```

## Middle

```txt id="0xdrfv"
m = 4
nums[m] = 9
```

Compare:

```txt id="3r6gyk"
9 == 9
```

Return:

```txt id="yssw6u"
4
```

---

# Time Complexity

At every step:

```txt id="xk2rvt"
search space is cut in half
```

Sequence:

```txt id="w9gljl"
n
n/2
n/4
n/8
...
```

This produces:

```txt id="wbjlwm"
O(log n)
```

---

# Space Complexity

```txt id="3n7do7"
O(1)
```

Only pointers are used.

---

# Pattern Extraction

| Component        | Meaning                          |
| ---------------- | -------------------------------- |
| Trigger          | Sorted array + O(log n)          |
| Pattern          | Classic Binary Search            |
| Structure        | Shrinking search interval        |
| Core Invariant   | Target must remain inside [l, r] |
| Elimination Rule | Discard impossible half          |
| Complexity       | O(log n)                         |

---

# The Most Important Thing To Internalize

Binary Search is NOT:

```txt id="jlwmr2"
"check middle repeatedly"
```

Binary Search IS:

```txt id="nrylbq"
maintaining a valid search space
while eliminating impossible regions
using monotonic order
```

That mental model scales to every advanced binary search problem later.
