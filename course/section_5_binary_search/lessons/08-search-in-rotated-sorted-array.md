# Step 1 — Pattern Prediction

This is the canonical:

```txt id="jlwm0a"
Search in Rotated Sorted Array
```

pattern.

This problem is extremely important because it teaches a deep Binary Search idea:

```txt id="jlwm1b"
Binary Search does NOT require FULL sorting.
```

It only requires:

```txt id="’wini2c"
enough structure to eliminate half safely
```

That is the core lesson.

---

# First — Why This Problem Feels Difficult

Normal Binary Search relies on:

```txt id="’wini3d"
fully sorted array
```

Example:

```txt id="

```

[1,2,3,4,5,6,7]

````id="4ejlwm"

Then:

```txt id="5fjlwm"
nums[mid] < target
→ search right
````

works naturally.

---

# But Rotation Breaks Global Order

Example:

```txt id="6g’wini"
[4,5,6,7,0,1,2]
```

This is NOT globally sorted.

So normal binary search logic breaks.

---

# The Key Insight

Even though the WHOLE array is not sorted:

```txt id="7h’wini"
ONE HALF always IS sorted
```

This is the entire trick.

---

# Mental Model

At every midpoint:

```txt id="8i’wini"
one side is "normal"
one side contains the rotation
```

Example:

```txt id="9j’wini"
[4,5,6,7,0,1,2]
         ^
        mid
```

Left side:

```txt id="0k’wini"
[4,5,6,7]
```

is perfectly sorted.

Right side:

```txt id="1l’wini"
[0,1,2]
```

contains the rotation boundary.

---

# Binary Search Still Works

Because if one side is sorted:

```txt id="2m’wini"
we can determine whether target
can exist there or not
```

That is enough to eliminate half.

---

# Recognition Signals

Look for phrases like:

| Phrase               | Meaning                |
| -------------------- | ---------------------- |
| rotated sorted array | partial ordering       |
| shifted sorted array | pivot exists           |
| O(log n)             | binary search expected |

---

# Step 2 — Your Core Strategy

Your implementation is structurally correct.

You correctly identified the key idea:

```txt id="3n’wini"
determine WHICH HALF is sorted
```

That is the heart of the problem.

---

# But Your Conditions Are Harder Than Necessary

This part:

```python
if mid <= target or target < nums[l]:
```

and:

```python
if mid >= target or target > nums[r]:
```

works, but it is difficult to reason about.

The cleaner approach is:

```txt id="4o’wini"
1. identify sorted half
2. check whether target lies INSIDE it
```

This produces much cleaner invariants.

---

# Step 3 — Build The Clean Logic

---

# Step 3.1 — Standard Binary Search Setup

```python
l, r = 0, len(nums) - 1
```

Search space boundaries.

---

# Step 3.2 — Standard Loop

```python
while l <= r:
```

Same invariant:

```txt id="5p’wini"
if target exists,
it must remain inside [l, r]
```

---

# Step 3.3 — Middle

```python
m = (l + r) // 2
```

---

# Step 3.4 — Exact Match

```python
if nums[m] == target:
    return m
```

Always check equality first.

---

# Step 3.5 — Determine Sorted Half

This is the key step.

---

## Case 1 — Left Half Sorted

```python
if nums[l] <= nums[m]:
```

---

# Why Does This Work?

Suppose:

```txt id="6q’wini"
[4,5,6,7,0,1,2]
```

and:

```txt id="7r’wini"
m = 3
nums[m] = 7
```

Then:

```txt id="8s’wini"
nums[l] <= nums[m]
```

means:

```txt id="9t’wini"
left half is properly ordered
```

---

# Important Insight

In rotated arrays:

```txt id="0u’wini"
one half MUST remain sorted
```

because there is only ONE rotation point.

---

# Step 3.6 — Is Target Inside Sorted Left Half?

```python
if nums[l] <= target < nums[m]:
```

---

# Why This Condition?

If target lies inside sorted left region:

```txt id="1v’wini"
search left
```

Otherwise:

```txt id="2w’wini"
search right
```

---

# Move Left

```python
r = m - 1
```

---

# Move Right

```python
else:
    l = m + 1
```

---

# Step 3.7 — Right Half Sorted

Else:

```python
else:
```

means:

```txt id="3x’wini"
right half must be sorted
```

---

# Check If Target Inside Right Half

```python
if nums[m] < target <= nums[r]:
```

---

# If Yes

```python
l = m + 1
```

---

# Otherwise

```python
r = m - 1
```

---

# Final Clean Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left half sorted
            if nums[l] <= nums[m]:

                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right half sorted
            else:

                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
```

---

# Step 4 — Visual Execution

Input:

```txt id="4y’wini"
nums = [4,5,6,7,0,1,2]
target = 0
```

---

# Iteration 1

```txt id="5z’wini"
l = 0
r = 6
m = 3
nums[m] = 7
```

---

# Determine Sorted Half

```txt id="60a’wini"
nums[l] <= nums[m]
4 <= 7
```

So:

```txt id="71b’wini"
left half sorted
```

---

# Is Target Inside Left Half?

Check:

```txt id="82c’wini"
4 <= 0 < 7
```

False.

So target must be:

```txt id="93d’wini"
in right half
```

Update:

```txt id="a4e’wini"
l = 4
```

---

# Iteration 2

```txt id="b5f’wini"
l = 4
r = 6
m = 5
nums[m] = 1
```

---

# Left Half Sorted?

```txt id="c6g’wini"
0 <= 1
```

Yes.

Left half:

```txt id="d7h’wini"
[0,1]
```

sorted.

---

# Is Target Inside It?

```txt id="e8i’wini"
0 <= 0 < 1
```

Yes.

Search left.

```txt id="f9j’wini"
r = 4
```

---

# Iteration 3

```txt id="g0k’wini"
l = 4
r = 4
m = 4
nums[m] = 0
```

Found target.

Return:

```txt id="h1l’wini"
4
```

---

# Why This Problem Is Important

This problem teaches a huge Binary Search evolution:

---

# Normal Binary Search

```txt id="i2m’wini"
Entire search space is sorted
```

---

# Rotated Binary Search

```txt id="j3n’wini"
Only PART of the search space is sorted
```

Yet Binary Search still works.

That is a major conceptual leap.

---

# Complexity Analysis

At every step:

```txt id="k4o’wini"
we still eliminate half
```

So:

```txt id="l5p’wini"
O(log n)
```

---

# Space Complexity

```txt id="m6q’wini"
O(1)
```

---

# Pattern Extraction

| Component            | Meaning                                           |
| -------------------- | ------------------------------------------------- |
| Trigger              | rotated sorted array                              |
| Pattern              | Partial-Order Binary Search                       |
| Key Insight          | one half always sorted                            |
| Decision Rule        | determine sorted half                             |
| Elimination Strategy | check whether target belongs inside sorted region |
| Complexity           | O(log n)                                          |

---

# Deepest Insight From This Problem

Binary Search does NOT fundamentally require:

```txt id="n7r’wini"
fully sorted arrays
```

It requires:

```txt id="o8s’wini"
enough monotonic structure
to eliminate half safely
```

That abstraction is what makes advanced Binary Search possible.
