# Step 1 — Pattern Prediction

This is a:

```txt id="q1v7sa"
Lower Bound / Boundary Binary Search
```

problem.

More specifically:

```txt id="jjlwm1"
Find the smallest value >= target
```

This is one of the most important binary search patterns.

---

# First — Understand The Problem Deeply

This problem is confusing at first because:

```txt id="kjlwm2"
we are NOT searching inside intervals
```

We are searching among:

```txt id="ljlwm3"
interval START values
```

That distinction is critical.

---

# What Is A "Right Interval"?

For interval:

```txt id="mjlwm4"
[start_i, end_i]
```

we need another interval:

```txt id="njlwm5"
[start_j, end_j]
```

such that:

```txt id="ojlwm6"
start_j >= end_i
```

AND:

```txt id="pjlwm7"
start_j is as SMALL as possible
```

This is the key phrase.

---

# Mental Model

Suppose:

```txt id="qjlwm8"
intervals = [[3,4],[2,3],[1,2]]
```

Extract only starts:

```txt id="rjlwm9"
3, 2, 1
```

Now consider interval:

```txt id="0akjlwm"
[2,3]
```

Its end is:

```txt id="1bljlwm"
3
```

We need:

```txt id="2cmjlwm"
smallest start >= 3
```

Among starts:

```txt id="3dnjlwm"
1,2,3
```

answer is:

```txt id="4eojlwm"
3
```

which belongs to interval index:

```txt id="5fpjlwm"
0
```

That is the whole problem.

---

# The Core Transformation

This problem secretly becomes:

```txt id="6gqjlwm"
For every interval:
find LOWER BOUND of end_i
inside sorted starts
```

This is classical lower-bound binary search.

---

# Why Binary Search Works

Because after sorting starts:

```txt id="7hrjlwm"
starts become monotonic
```

Example:

```txt id="8isjlwm"
[1,2,3]
```

Now we search for:

```txt id="9jtjlwm"
first value >= target
```

This produces the classic boundary shape:

```txt id="0kuljlwm"
False False False True True
```

Binary Search loves boundaries.

---

# Step 2 — Build The Solution Slowly

---

# Step 2.1 — We Need Original Indices

Problem asks for:

```txt id="1lvjlwm"
interval indices
```

not the start values themselves.

So we store:

```txt id="2mwjlwm"
(start_value, original_index)
```

---

# Example

Input:

```txt id="3nxjlwm"
[[3,4],[2,3],[1,2]]
```

Becomes:

```python
[(3,0), (2,1), (1,2)]
```

---

# Step 2.2 — Sort By Start Values

```python
starts.sort()
```

Now:

```python
[(1,2), (2,1), (3,0)]
```

---

# Why Sorting Matters

Binary Search requires:

```txt id="4oy’wini"
ordered search space
```

Now starts are monotonic.

---

# Step 2.3 — For Each Interval

We process every interval independently.

Example:

```txt id="5pzjlwm"
[2,3]
```

Need:

```txt id="6q0jlwm"
smallest start >= 3
```

This is LOWER BOUND.

---

# Step 2.4 — Binary Search

This is the key operation.

We binary search on:

```txt id="7r1jlwm"
sorted start values
```

looking for:

```txt id="8s2jlwm"
first start >= current_end
```

---

# Step 3 — Full Step-by-Step Code

---

# Create Sorted Starts

```python
starts = []

for i, (start, end) in enumerate(intervals):
    starts.append((start, i))
```

---

## What This Does

Stores:

```txt id="9t3jlwm"
(start value, original index)
```

We need indices later.

---

# Sort Starts

```python
starts.sort()
```

Now binary search becomes possible.

---

# Prepare Answer

```python
res = [-1] * len(intervals)
```

Default:

```txt id="0u4jlwm"
no right interval exists
```

---

# Process Each Interval

```python
for i, (start, end) in enumerate(intervals):
```

Now solve independently for each interval.

---

# Binary Search Setup

```python
l, r = 0, len(starts) - 1
ans = -1
```

---

# Why `ans = -1`?

If no valid start found:

```txt id="1v5jlwm"
problem requires -1
```

---

# Binary Search Loop

```python
while l <= r:
```

Standard search space.

---

# Middle

```python
m = (l + r) // 2
```

---

# Check Start Value

```python
if starts[m][0] >= end:
```

Critical condition.

---

# What This Means

We found:

```txt id="2w6jlwm"
a VALID candidate
```

But maybe not the smallest valid one.

This is lower-bound logic again.

---

# Save Candidate

```python
ans = starts[m][1]
```

Store original interval index.

---

# Continue LEFT

```python
r = m - 1
```

Because maybe there exists:

```txt id="3x7jlwm"
smaller valid start
```

---

# Otherwise

```python
else:
    l = m + 1
```

Meaning:

```txt id="4y8’wini"
start too small
```

Must search right.

---

# Save Final Answer

```python
res[i] = ans
```

---

# Final Code

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        starts = []

        for i, (start, end) in enumerate(intervals):
            starts.append((start, i))

        starts.sort()

        res = [-1] * len(intervals)

        for i, (start, end) in enumerate(intervals):

            l, r = 0, len(starts) - 1
            ans = -1

            while l <= r:

                m = (l + r) // 2

                if starts[m][0] >= end:
                    ans = starts[m][1]
                    r = m - 1

                else:
                    l = m + 1

            res[i] = ans

        return res
```

---

# Step 4 — Visual Execution

Input:

```txt id="5z9’wini"
intervals = [[3,4],[2,3],[1,2]]
```

---

# Build Starts

```python
[(3,0), (2,1), (1,2)]
```

Sort:

```python
[(1,2), (2,1), (3,0)]
```

---

# Process [2,3]

Need:

```txt id="60a

```

smallest start >= 3

````

Binary Search on:

```txt id="71bjlwm"
[1,2,3]
````

---

# Iteration 1

```txt id="82cjlwm"
l = 0
r = 2
m = 1
start = 2
```

```txt id="93djlwm"
2 < 3
```

Move right.

---

# Iteration 2

```txt id="a4ejlwm"
l = 2
r = 2
m = 2
start = 3
```

Valid candidate.

Save:

```txt id="b5fjlwm"
ans = 0
```

Continue left:

```txt id="c6gjlwm"
r = 1
```

Loop ends.

Answer:

```txt id="d7hjlwm"
0
```

Correct.

---

# Complexity Analysis

Suppose:

```txt id="e8ijlwm"
n = number of intervals
```

---

# Sorting

```txt id="f9jjlwm"
O(n log n)
```

---

# Binary Search For Every Interval

Each interval:

```txt id="g0kjlwm"
O(log n)
```

Total:

```txt id="h1l’wini"
O(n log n)
```

---

# Space Complexity

```txt id="i2m’wini"
O(n)
```

for sorted starts.

---

# Pattern Extraction

| Component         | Meaning                         |
| ----------------- | ------------------------------- |
| Trigger           | smallest value >= target        |
| Pattern           | Lower Bound Binary Search       |
| Search Space      | sorted interval starts          |
| Goal              | first valid start               |
| Key Condition     | start >= end                    |
| Important Insight | continue left after valid match |
| Complexity        | O(n log n)                      |

---

# Most Important Thing To Learn From This Problem

This problem teaches a critical Binary Search abstraction:

```txt id="j3n’wini"
Binary Search is often NOT searching the original data directly.
```

We transformed:

```txt id="k4o’wini"
intervals
```

into:

```txt id="l5p’wini"
sorted searchable starts
```

That transformation skill is extremely important in advanced problems.
