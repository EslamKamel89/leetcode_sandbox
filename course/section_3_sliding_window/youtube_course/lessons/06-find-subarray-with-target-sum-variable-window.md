This is the **turning point of Section 3**.

Everything before this was preparation.

Now you’re entering:

> 🔥 **Variable Sliding Window (the real pattern used in interviews)**

This lesson is critical. Don’t rush it.

---

# 🧠 Study Guide — Find Subarray with Target Sum (Variable Window)

(First variable-size sliding window problem)

---

# 1. Problem Reconstruction

## 🔹 Problem

You are given:

- An array `nums` (non-negative integers)
- A target sum `target`

Your task:

> Find a **contiguous subarray** whose sum equals `target`
> Return its **start and end indices (inclusive)**

---

## 🔹 Example

```python
nums = [3, 1, 4, 9, 2, 1, 7, 3]
target = 10
```

Valid answer:

```text
[2, 1, 7] → indices (4, 6)
```

---

## 🔹 Key Constraints

- Numbers are **non-negative** (VERY IMPORTANT)
- Subarray size is **NOT fixed**

---

## 🔹 Why this is Sliding Window

Signals:

- “subarray”
- “contiguous”
- need to scan efficiently

BUT:

❗ No fixed size → **Variable Window**

---

# 2. Mental Model (CRITICAL)

---

## 🔴 What changed from previous lessons?

Before:

```text
Window size = fixed (k)
```

Now:

```text
Window size = dynamic
```

---

## 🔹 Core Idea

We maintain:

```text
start → left boundary
end   → right boundary
window_sum → sum of current window
```

---

## 🔹 Window Behavior

Two operations:

### 1. Expand window (move `end`)

- Add element
- When sum is too small

### 2. Shrink window (move `start`)

- Remove element
- When sum is too large

---

## 🔹 Decision Rule (VERY IMPORTANT)

```text
if sum < target → expand
if sum > target → shrink
if sum == target → done
```

---

## 🔴 Why this works (IMPORTANT)

Because:

> All numbers are **non-negative**

So:

- Expanding → increases sum
- Shrinking → decreases sum

---

### If negatives existed:

❌ This logic breaks

---

## 🔹 Brute Force

Try all subarrays:

```text
O(n²)
```

---

## 🔹 Sliding Window Insight

We avoid rechecking by:

- Moving pointers only forward
- Never resetting

---

# 3. Step-by-Step Solution Development

---

## 🔸 Step 1 — Initialize State

```python
start = 0
window_sum = 0
```

---

### Why?

- `start` tracks left boundary
- `window_sum` tracks current sum

---

## 🔸 Step 2 — Expand Window

```python
for end in range(len(nums)):
    window_sum += nums[end]
```

---

### Explanation

- `end` grows the window
- Adds new element

---

## 🔸 Step 3 — Shrink Window (CRITICAL)

```python
while window_sum > target:
    window_sum -= nums[start]
    start += 1
```

---

### Why a **while loop**, not if?

Because:

- You may need to shrink multiple times

---

### What this does:

- Removes elements from left
- Keeps shrinking until valid

---

## 🔸 Step 4 — Check Condition

```python
if window_sum == target:
    return (start, end)
```

---

### Why here?

Because:

- After shrinking → window is valid
- This is the correct moment to check

---

# 4. Visualization (Execution Trace)

```python
nums = [3,1,4,9,2,1,7,3]
target = 10
```

---

### Step 1

```text
[3] → sum = 3 (<10) → expand
```

---

### Step 2

```text
[3,1] → sum = 4 (<10) → expand
```

---

### Step 3

```text
[3,1,4] → sum = 8 (<10) → expand
```

---

### Step 4

```text
[3,1,4,9] → sum = 17 (>10) → shrink
```

Shrink:

```text
remove 3 → sum = 14
remove 1 → sum = 13
remove 4 → sum = 9
```

---

### Step 5

```text
[9] → sum = 9 (<10) → expand
```

---

### Step 6

```text
[9,2] → sum = 11 (>10) → shrink
```

```text
remove 9 → sum = 2
```

---

### Step 7

```text
[2,1,7] → sum = 10 ✅
```

👉 Return `(4, 6)`

---

# 5. Complexity Analysis

---

## 🔹 Time Complexity

At first glance:

- for loop + while loop → looks like O(n²)

BUT:

👉 Each element is added once and removed once

```text
Total operations ≤ 2n
```

👉 Final:

```text
O(n)
```

---

## 🔹 Space Complexity

- Only variables

👉 **O(1)**

---

# 6. Final Code

```python
def find_subarray_sum(nums, target):
    start = 0
    window_sum = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum > target:
            window_sum -= nums[start]
            start += 1

        if window_sum == target:
            return (start, end)

    return None
```

---

# 7. Pattern Abstraction (CRITICAL)

---

## 🔹 Variable Window Template

```python
start = 0

for end in range(n):
    add(nums[end])

    while condition violated:
        remove(nums[start])
        start += 1

    check condition
```

---

## 🔹 Key Difference from Fixed Window

| Fixed Window           | Variable Window         |
| ---------------------- | ----------------------- |
| size = k               | size changes            |
| always move both sides | move based on condition |
| no shrinking logic     | shrinking is essential  |

---

## 🔹 Recognition Triggers

- “longest / shortest subarray”
- “sum ≤ / ≥ / == target”
- “dynamic size”

👉 Think: **Variable Sliding Window**

---

# 8. Common Mistakes

---

## ❌ 1. Using `if` instead of `while`

Leads to:

- incomplete shrinking

---

## ❌ 2. Forgetting non-negative constraint

If negatives exist:

- algorithm fails

---

## ❌ 3. Checking before shrinking

Wrong:

```python
if window_sum == target:
```

Before fixing overflow

---

## ❌ 4. Thinking it's O(n²)

Because of nested loop illusion

---

## ❌ 5. Resetting pointers

Never do:

```text
start = 0 again
```

---

# 🎯 Final Summary

---

## What did you actually learn?

You learned:

> Sliding Window can adapt **dynamically based on conditions**

---

## Biggest Upgrade So Far

```text
Fixed Window → Variable Window
```

---

## Core Principle

```text
Expand when too small
Shrink when too big
```

---

## Why this is important

This pattern is used in:

- Longest substring problems
- Minimum window substring
- Subarray constraints

---

## Where you are now

You just entered:

> 🔥 **Real Sliding Window (Variable)**

This is exactly the progression your system expects:

> from fixed understanding → dynamic control of window boundaries

---

## What comes next (VERY IMPORTANT)

Next problems will:

- Remove the “exact match” condition
- Introduce constraints like:
  - no duplicates
  - max length
  - min length

---

If you want to proceed correctly:

👉 I strongly recommend next:

**“Longest Substring Without Repeating Characters”**

This is the **canonical variable window problem** and will test if you truly understood this lesson.
