# Step 1 — Pattern Prediction

This is the canonical:

```txt id="v1c7rs"
Lower Bound / Upper Bound Binary Search
```

problem.

This problem is one of the most important Binary Search transitions because it teaches:

```txt id="if1m4x"
Binary Search can continue EVEN AFTER finding target.
```

That is the core conceptual jump.

---

# What Pattern Is This?

## Pattern

```txt id="mjlwm2"
Boundary Binary Search
```

More specifically:

- Left Boundary Search
- Right Boundary Search

---

# Why This Is Different from Classic Binary Search

Classic Binary Search asks:

```txt id="jlwm3l"
"Did we find target?"
```

This problem asks:

```txt id="jlwm4m"
"Where does the target RANGE begin and end?"
```

That changes the stopping condition entirely.

---

# The Core Difficulty

Suppose:

```txt id="jlwm5n"
nums = [5,7,7,8,8,10]
target = 8
```

Classic Binary Search might find:

```txt id="jlwm6o"
index 3
```

OR:

```txt id="jlwm7p"
index 4
```

Both are valid matches.

But this problem requires:

```txt id="jlwm8q"
FIRST occurrence
LAST occurrence
```

Meaning:

```txt id="jlwm9r"
finding equality is NOT enough
```

We must continue searching.

---

# Mental Model

Visualize the array as regions.

---

# Left Boundary

```txt id="0sljlwm"
smaller | target target | larger
             ^
       first occurrence
```

---

# Right Boundary

```txt id="1tmjlwm"
smaller | target target | larger
                    ^
             last occurrence
```

We are searching for boundaries, not values.

---

# The Key Binary Search Insight

Once target found:

```txt id="2unjlwm"
DO NOT STOP
```

Instead:

- continue LEFT to find first occurrence
- continue RIGHT to find last occurrence

This is the defining behavior of boundary binary search.

---

# Recognition Signals

Look for wording like:

| Phrase                     | Meaning                  |
| -------------------------- | ------------------------ |
| "first occurrence"         | lower bound              |
| "last occurrence"          | upper bound              |
| "range of target"          | boundary search          |
| duplicates in sorted array | multiple valid positions |

---

# Why Your Solution Is Excellent

Your implementation captures the exact mental model correctly.

This line is the key:

```python
i = m
```

It means:

```txt id="3vojlwm"
"We found a VALID answer,
but maybe not the BEST answer yet."
```

That is the heart of boundary search.

---

# Step 2 — Reconstruct the Logic

---

# Step 2.1 — Standard Binary Search Setup

```python
l, r = 0, len(nums) - 1
```

Same shrinking search space.

---

# Step 2.2 — Store Candidate Answer

```python
i = -1
```

---

# Why This Exists

Unlike classic binary search:

```txt id="4wpjlwm"
finding target does NOT terminate search
```

So we must remember:

```txt id="5xqjlwm"
latest valid occurrence
```

while continuing exploration.

---

# Step 2.3 — Standard Binary Search Loop

```python
while l <= r:
```

No change.

---

# Step 2.4 — Compare Against Target

```python
if nums[m] > target:
```

Target must be left.

---

```python
elif nums[m] < target:
```

Target must be right.

---

# Step 2.5 — Target Found

```python
else:
    i = m
```

Critical moment.

---

# Why We Save `m`

Because:

```txt id="6yrjlwm"
this IS a valid target occurrence
```

But:

```txt id="7zsjlwm"
we don't know if it's the boundary yet
```

---

# Left-Biased Search

```python
if left_biased:
    r = m - 1
```

---

# Why Move Left?

Because we are asking:

```txt id="80tjlwm"
"Can we find an EARLIER occurrence?"
```

We intentionally continue searching left.

---

# Right-Biased Search

```python
else:
    l = m + 1
```

---

# Why Move Right?

Because we are asking:

```txt id="91ujlwm"
"Can we find a LATER occurrence?"
```

---

# This Is The Most Important Concept

In classic binary search:

```txt id="a2vjlwm"
equality TERMINATES
```

In boundary binary search:

```txt id="b3wjlwm"
equality REDIRECTS the search
```

That distinction is foundational.

---

# Step 3 — Visual Execution

Input:

```txt id="c4xjlwm"
nums = [5,7,7,8,8,10]
target = 8
```

---

# LEFT Boundary Search

---

# Iteration 1

```txt id="d5yjlwm"
l = 0
r = 5
m = 2
nums[m] = 7
```

```txt id="e6zjlwm"
7 < 8
```

Move right.

```txt id="f70jlwm"
l = 3
```

---

# Iteration 2

```txt id="g81jlwm"
l = 3
r = 5
m = 4
nums[m] = 8
```

Found target.

Save:

```txt id="h92jlwm"
i = 4
```

But continue LEFT:

```txt id="ia3jlwm"
r = 3
```

---

# Iteration 3

```txt id="jb4jlwm"
l = 3
r = 3
m = 3
nums[m] = 8
```

Save:

```txt id="kc5jlwm"
i = 3
```

Continue LEFT:

```txt id="ld6jlwm"
r = 2
```

Loop ends.

Return:

```txt id="me7jlwm"
3
```

Correct first occurrence.

---

# RIGHT Boundary Search

Same logic, but continue RIGHT after equality.

Eventually returns:

```txt id="nf8jlwm"
4
```

---

# Why Two Searches?

Because:

```txt id="og9jlwm"
left boundary and right boundary
are DIFFERENT monotonic searches
```

Trying to combine them usually creates messy logic.

Separating them gives:

- cleaner invariants
- easier debugging
- clearer reasoning

---

# Complexity Analysis

Each search:

```txt id="phajlwm"
O(log n)
```

Two searches:

```txt id="qibjlwm"
O(log n) + O(log n)
= O(log n)
```

Still logarithmic.

---

# Pattern Extraction

| Component    | Meaning                            |
| ------------ | ---------------------------------- |
| Trigger      | duplicates + first/last occurrence |
| Pattern      | Boundary Binary Search             |
| Core Shift   | equality does NOT terminate        |
| Left Search  | continue left after match          |
| Right Search | continue right after match         |
| Key Variable | store latest valid answer          |
| Complexity   | O(log n)                           |

---

# Deepest Insight From This Problem

This problem teaches the real evolution of Binary Search:

---

# Stage 1 — Exact Match

```txt id="rjcjlwm"
Did we find target?
```

---

# Stage 2 — Boundary Search

```txt id="skdjlwm"
Where does a condition START or END?
```

That transition is what unlocks advanced binary search problems later.
