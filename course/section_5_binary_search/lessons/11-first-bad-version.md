# Step 1 — Pattern Prediction

This is one of the purest forms of:

```txt id="fbv001"
Lower Bound / Boundary Binary Search
```

In fact, this problem is almost the “mathematical essence” of boundary search.

---

# The Deep Insight

We are NOT searching for:

```txt id="fbv002"
a value
```

We are searching for:

```txt id="fbv003"
the FIRST position
where a condition becomes TRUE
```

That is the exact definition of lower-bound binary search.

---

# Visualize The Versions

Suppose:

```txt id="fbv004"
n = 10
bad = 6
```

Then versions behave like:

```txt id="fbv005"
1 2 3 4 5 6 7 8 9 10
F F F F F T T T T T
```

Where:

- `F` = good version
- `T` = bad version

Notice the structure:

```txt id="fbv006"
False False False False True True True
```

This is the canonical Binary Search boundary shape.

---

# The Problem Is Secretly Asking

Find:

```txt id="fbv007"
the FIRST TRUE
```

That is the core transformation.

---

# Recognition Signals

Look for phrases like:

| Phrase                     | Meaning                |
| -------------------------- | ---------------------- |
| first bad version          | first true             |
| all versions after are bad | monotonic condition    |
| minimize API calls         | binary search expected |

---

# Why Binary Search Works

Because the condition:

```txt id="fbv008"
isBadVersion(x)
```

is monotonic.

Once it becomes:

```txt id="fbv009"
True
```

it remains:

```txt id="fbv010"
True forever
```

That monotonicity is what enables Binary Search.

---

# Step 2 — Understanding Your Solution

Your solution is correct.

And importantly:

```txt id="fbv011"
you are NOT returning when finding a bad version
```

That is the key conceptual leap.

---

# Why Don't We Return Immediately?

Suppose:

```txt id="fbv012"
m = 7
```

and:

```txt id="fbv013"
isBadVersion(7) = True
```

Does that mean:

```txt id="fbv014"
7 is FIRST bad version?
```

No.

Maybe:

```txt id="fbv015"
6 is bad
5 is bad
```

We only know:

```txt id="fbv016"
7 belongs to bad region
```

So we must continue LEFT.

This is classic boundary search behavior.

---

# Step 3 — Reconstruct The Algorithm Slowly

---

# Step 3.1 — Define Search Space

```python id="fbv017"
left, right = 1, n
```

---

# Important Correction

Your code used:

```python
left = 0
```

But versions start at:

```txt id="fbv018"
1
```

So cleaner search space is:

```txt id="fbv019"
[1 → n]
```

---

# Step 3.2 — Binary Search Loop

```python id="fbv020"
while left <= right:
```

Standard shrinking search interval.

---

# Step 3.3 — Middle Version

```python id="fbv021"
m = (left + right) // 2
```

Candidate boundary.

---

# Step 3.4 — Check Condition

```python id="fbv022"
if isBadVersion(m):
```

This asks:

```txt id="fbv023"
Did we enter bad region?
```

---

# If TRUE

Then:

```txt id="fbv024"
m COULD be first bad version
```

But maybe there exists an earlier bad version.

So we continue LEFT:

```python id="fbv025"
right = m - 1
```

---

# If FALSE

Then:

```txt id="fbv026"
m definitely NOT bad
```

And because bad versions only occur AFTER first bad:

```txt id="fbv027"
everything LEFT of m also safe
```

So:

```python id="fbv028"
left = m + 1
```

---

# Step 3.5 — Return Left

```python id="fbv029"
return left
```

This is the most important insight.

---

# Why Does `left` Become The Answer?

At loop termination:

```txt id="fbv030"
right points to last GOOD version
left points to first BAD version
```

Visualize:

```txt id="fbv031"
GOOD GOOD GOOD | BAD BAD BAD
                 ^
               left
```

That is the lower-bound invariant.

---

# Final Clean Solution

```python id="fbv032"
class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n

        while left <= right:

            m = (left + right) // 2

            if isBadVersion(m):
                right = m - 1

            else:
                left = m + 1

        return left
```

---

# Step 4 — Visual Execution

Suppose:

```txt id="fbv033"
n = 5
bad = 4
```

Meaning:

```txt id="fbv034"
1 2 3 4 5
F F F T T
```

---

# Iteration 1

```txt id="fbv035"
left = 1
right = 5
m = 3
```

Check:

```txt id="fbv036"
isBadVersion(3) = False
```

So:

```txt id="fbv037"
first bad must be RIGHT
```

Update:

```txt id="fbv038"
left = 4
```

---

# Iteration 2

```txt id="fbv039"
left = 4
right = 5
m = 4
```

Check:

```txt id="fbv040"
isBadVersion(4) = True
```

Possible answer.

Continue LEFT.

```txt id="fbv041"
right = 3
```

---

# Loop Ends

```txt id="fbv042"
left = 4
right = 3
```

Return:

```txt id="fbv043"
4
```

Correct.

---

# Complexity Analysis

At every step:

```txt id="fbv044"
half the versions eliminated
```

So:

```txt id="fbv045"
O(log n)
```

---

# Space Complexity

```txt id="fbv046"
O(1)
```

---

# Pattern Extraction

| Component           | Meaning                             |
| ------------------- | ----------------------------------- |
| Trigger             | first position satisfying condition |
| Pattern             | Lower Bound Binary Search           |
| Search Space        | versions                            |
| Monotonic Condition | isBadVersion(x)                     |
| Boundary Shape      | False False False True True         |
| Key Insight         | finding TRUE does NOT terminate     |
| Final Answer        | left pointer                        |
| Complexity          | O(log n)                            |

---

# Deepest Insight From This Problem

This problem teaches the pure essence of boundary binary search:

```txt id="fbv047"
Binary Search is fundamentally
about locating transitions.
```

Not values.

Not indices.

Transitions.

This problem is essentially:

```txt id="fbv048"
Find where FALSE becomes TRUE.
```

That mental model generalizes to a huge number of advanced problems.
