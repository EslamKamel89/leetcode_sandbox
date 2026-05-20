# Step 1 — Pattern Prediction

This is the second core pattern in:

```txt id="0a1rot"
Rotated Sorted Array Binary Search
```

But unlike the previous problem:

```txt id="1b2rot"
we are NOT searching for a target
```

We are searching for:

```txt id="2c3rot"
the rotation boundary itself
```

That is the key conceptual shift.

---

# What Pattern Is This?

## Pattern

```txt id="3d4rot"
Binary Search on Rotation Pivot
```

or:

```txt id="4e5rot"
Find rotation boundary
```

---

# The Deep Insight

A rotated sorted array actually contains:

```txt id="5f6rot"
TWO sorted regions
```

Example:

```txt id="6g7rot"
[4,5,6,7,0,1,2]
```

can be viewed as:

```txt id="7h8rot"
[4,5,6,7] + [0,1,2]
```

The minimum element is exactly where:

```txt id="8i9rot"
the ordering "breaks"
```

---

# Visualize The Rotation

Original sorted array:

```txt id="9j0rot"
[0,1,2,4,5,6,7]
```

Rotated:

```txt id="0k1rot"
[4,5,6,7,0,1,2]
```

Notice:

```txt id="1l2rot"
7 > 0
```

That discontinuity marks the pivot.

The minimum is always:

```txt id="2m3rot"
the FIRST element of the second sorted portion
```

---

# Recognition Signals

Look for:

| Signal               | Meaning                |
| -------------------- | ---------------------- |
| rotated sorted array | partial ordering       |
| minimum element      | pivot/boundary         |
| O(log n)             | binary search expected |

---

# Important Mental Shift

In previous rotated-array problem:

```txt id="3n4rot"
we searched for a VALUE
```

Here:

```txt id="4o5rot"
we search for a STRUCTURAL BREAK
```

That is a major evolution.

---

# Step 2 — Understanding Your First Solution

Your first solution:

```python
def findMin1(self, nums):
```

contains an extremely important insight.

---

# Key Observation

You compare against:

```python
nums[0]
```

Why does that work?

Because:

```txt id="5p6rot"
all elements BEFORE pivot
>= nums[0]
```

and:

```txt id="6q7rot"
all elements AFTER pivot
< nums[0]
```

Example:

```txt id="7r8rot"
[4,5,6,7,0,1,2]
```

Relative to `nums[0] = 4`:

```txt id="8s9rot"
4 >= 4 → True
5 >= 4 → True
6 >= 4 → True
7 >= 4 → True
0 >= 4 → False
1 >= 4 → False
2 >= 4 → False
```

This creates:

```txt id="9t0rot"
True True True True False False False
```

That is a monotonic boundary.

Binary Search LOVES boundaries.

---

# Why Your First Solution Works

---

# If `mid >= nums[0]`

```python
if mid >= nums[0]:
    left = m + 1
```

Meaning:

```txt id="0u1rot"
we are still in LEFT sorted region
```

Minimum must be farther right.

---

# Otherwise

```python
right = m - 1
```

Meaning:

```txt id="1v2rot"
we entered RIGHT sorted region
```

Minimum could be here or earlier.

---

# This Is Actually Brilliant

This solution directly searches for:

```txt id="2w3rot"
the first value smaller than nums[0]
```

Very elegant.

---

# But There Is One Weakness

This part:

```python
if left < len(nums):
    return nums[left]
else:
    return nums[0]
```

exists because:

```txt id="3x4rot"
fully sorted array becomes awkward
```

Example:

```txt id="4y5rot"
[1,2,3,4]
```

Then:

```txt id="5z6rot"
everything >= nums[0]
```

So search exits outside array.

Correct, but slightly indirect.

---

# Step 3 — Your Second Solution

Your second solution is the more standard interview approach.

And conceptually it is stronger.

---

# Core Insight of Second Solution

You detect:

```txt id="6a7rot"
whether current search space is already sorted
```

This is the key line:

```python
if nums[left] < nums[right]:
```

---

# Why This Matters

If:

```txt id="7b8rot"
left value < right value
```

then:

```txt id="8c9rot"
current region is fully sorted
```

Meaning:

```txt id="9d0rot"
minimum is simply nums[left]
```

No need to search further.

This is a very important optimization.

---

# Step 4 — Reconstruct The Standard Logic

---

# Step 4.1 — Initialize Answer

```python
res = nums[0]
```

Tracks smallest value seen so far.

---

# Step 4.2 — Binary Search Loop

```python
while left <= right:
```

Standard search-space maintenance.

---

# Step 4.3 — Detect Fully Sorted Region

```python
if nums[left] < nums[right]:
```

This means:

```txt id="0e1rot"
entire region sorted normally
```

Therefore:

```txt id="1f2rot"
leftmost element is minimum
```

Update:

```python
res = min(res, nums[left])
```

Then stop.

---

# Why Can We Break?

Because:

```txt id="2g3rot"
sorted ascending region
always has minimum at left edge
```

No further search needed.

---

# Step 4.4 — Examine Middle

```python
m = (left + right) // 2
res = min(res, nums[m])
```

We track minimum candidate.

---

# Step 4.5 — Determine Sorted Half

---

## Case 1 — Left Half Sorted

```python
if nums[left] <= nums[m]:
```

Meaning:

```txt id="3h4rot"
left half is properly ordered
```

Example:

```txt id="4i5rot"
[4,5,6,7]
```

---

# Important Insight

If left half sorted:

```txt id="5j6rot"
minimum CANNOT be inside it
```

because:

```txt id="6k7rot"
leftmost value already smallest there
```

So pivot/minimum must be:

```txt id="7l8rot"
to the RIGHT
```

Move:

```python
left = m + 1
```

---

## Case 2 — Rotation Exists Inside Left Half

Else:

```txt id="8m9rot"
pivot lies left
```

Move:

```python
right = m - 1
```

---

# Final Clean Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:

            # already sorted
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            m = (left + right) // 2

            res = min(res, nums[m])

            # left half sorted
            if nums[left] <= nums[m]:
                left = m + 1

            # pivot inside left half
            else:
                right = m - 1

        return res
```

---

# Step 5 — Visual Execution

Input:

```txt id="9n0rot"
nums = [4,5,6,7,0,1,2]
```

---

# Iteration 1

```txt id="0o1rot"
left = 0
right = 6
m = 3
nums[m] = 7
```

---

# Is Region Sorted?

```txt id="1p2rot"
4 < 2 → False
```

No.

---

# Is Left Half Sorted?

```txt id="2q3rot"
4 <= 7 → True
```

Yes.

Left side:

```txt id="3r4rot"
[4,5,6,7]
```

sorted.

Minimum cannot be there.

Move right:

```txt id="4s5rot"
left = 4
```

---

# Iteration 2

```txt id="5t6rot"
left = 4
right = 6
```

Check:

```txt id="6u7rot"
0 < 2 → True
```

Region already sorted.

Minimum:

```txt id="7v8rot"
nums[left] = 0
```

Return:

```txt id="8w9rot"
0
```

---

# Complexity Analysis

At every step:

```txt id="9x0rot"
half search space eliminated
```

So:

```txt id="0y1rot"
O(log n)
```

---

# Space Complexity

```txt id="1z2rot"
O(1)
```

---

# Pattern Extraction

| Component        | Meaning                          |
| ---------------- | -------------------------------- |
| Trigger          | rotated sorted array + minimum   |
| Pattern          | Rotation Pivot Binary Search     |
| Key Insight      | minimum lies at ordering break   |
| Structural Rule  | one half always sorted           |
| Elimination Rule | sorted half cannot contain pivot |
| Complexity       | O(log n)                         |

---

# Deepest Insight From This Problem

This problem teaches something profound:

```txt id="2a3rot"
Binary Search can locate
STRUCTURAL TRANSITIONS,
not just values.
```

You are not searching for:

```txt id="3b4rot"
a number
```

You are searching for:

```txt id="4c5rot"
where ordering changes
```

That is a much deeper Binary Search skill.
