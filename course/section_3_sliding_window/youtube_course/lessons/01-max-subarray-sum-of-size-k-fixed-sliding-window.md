Great — this is exactly the kind of foundational lesson that defines the **entire Sliding Window section**. I’m going to reconstruct it as a proper instructor-led study guide.

---

# 🧠 Study Guide — Max Subarray Sum of Size K (Fixed Sliding Window)

(Extracted and reconstructed from your lesson)

---

# 1. Problem Reconstruction

## 🔹 Problem (in your own words)

You are given:

- An array of integers `nums`
- An integer `k`

Your task:

> Find the **maximum sum of any contiguous subarray of size exactly k**

---

## 🔹 Key Constraints

- Subarray must be **continuous**
- Subarray size is **fixed (exactly k)**
- `k ≤ len(nums)` (otherwise invalid)

---

## 🔹 Example

```
nums = [1, 4, 1, 10, 25, 3, 5, 0]
k = 4
```

Valid windows:

```
[1,4,1,10] → 16
[4,1,10,25] → 40
[1,10,25,3] → 39
[10,25,3,5] → 43  ← max
...
```

---

## 🔹 Edge Cases

- `k == 1` → just return max element
- All negative numbers → still valid (max might be negative)
- `k == len(nums)` → only one window

---

## 🔹 Why this is a Sliding Window problem

### Recognition Signals:

- “subarray” → contiguous → important
- “size k” → **fixed window size**
- “consider all such subarrays” → moving window

👉 This is the **strongest signal for fixed sliding window**

---

# 2. Mental Model (CRITICAL)

## 🔹 What are we really doing?

We are scanning the array using a **window of size k**.

Think of it like this:

> You place a box of size k on the array, and slide it one step at a time.

---

## 🔹 Window Behavior

- Start at index `0`
- Always contains exactly `k` elements
- Move right by 1 each step

```
[ i ........ i+k-1 ]
```

---

## 🔹 Brute Force Thinking (IMPORTANT)

What would a naive solution do?

For every starting index:

1. Take k elements
2. Compute sum from scratch

### Complexity:

- Number of windows ≈ `n - k`
- Work per window = `k`

👉 Total = **O(n \* k)**

---

## 🔹 Why Sliding Window Works

Key observation:

> Adjacent windows overlap heavily

Example:

```
[1,4,1,10]
   [4,1,10,25]
```

Overlap = 3 elements

---

### Insight:

Instead of recomputing:

```
new_sum = old_sum - outgoing + incoming
```

This reduces:

- From recomputing k elements
- To updating **2 elements only**

---

# 3. Step-by-Step Solution Development

We build this like a real developer.

---

## 🔸 Step 1 — Initialize First Window

```python
current_sum = sum(nums[:k])
max_sum = current_sum
```

### Explanation:

- `nums[:k]` → first window
- We compute its sum once

Why necessary?

- We need a **starting state**
- Without it, we cannot compare future windows

If removed:

- You’d have no baseline → incorrect results

---

## 🔸 Step 2 — Start Sliding

```python
for i in range(k, len(nums)):
```

### Explanation:

- `i` represents the **new incoming element**
- Starts at index `k` (first element outside initial window)

---

## 🔸 Step 3 — Update Window Efficiently

```python
current_sum += nums[i]
current_sum -= nums[i - k]
```

---

### Line 1:

```python
current_sum += nums[i]
```

- Add new element entering window

---

### Line 2:

```python
current_sum -= nums[i - k]
```

- Remove element leaving window

---

### Why this works:

Window shift:

```
Old: [i-k, ..., i-1]
New: [i-k+1, ..., i]
```

So:

- Remove `nums[i-k]`
- Add `nums[i]`

---

### If you skip subtraction:

- Window size becomes > k → wrong answer

### If you skip addition:

- Window loses elements → incorrect sum

---

## 🔸 Step 4 — Update Maximum

```python
max_sum = max(max_sum, current_sum)
```

### Why:

- Track best result so far

If removed:

- You’d only get last window, not maximum

---

# 4. Visualization (Execution Trace)

Let’s walk through:

```
nums = [1,4,1,10,25,3,5]
k = 4
```

---

### Initial Window

```
[1,4,1,10] → sum = 16
max = 16
```

---

### Slide 1

Remove `1`, add `25`

```
16 - 1 + 25 = 40
max = 40
```

---

### Slide 2

Remove `4`, add `3`

```
40 - 4 + 3 = 39
max = 40
```

---

### Slide 3

Remove `1`, add `5`

```
39 - 1 + 5 = 43
max = 43
```

---

### Final Answer

```
43
```

---

# 5. Complexity Analysis

## 🔹 Time Complexity

- Initial sum: O(k)
- Loop runs: O(n - k)

Each step = O(1)

👉 Total = **O(n)**

---

## 🔹 Space Complexity

- Only variables used

👉 **O(1)**

---

# 6. Final Code

```python
def max_subarray_sum(nums, k):
    # Step 1: initial window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Step 2: slide window
    for i in range(k, len(nums)):
        current_sum += nums[i]        # add incoming
        current_sum -= nums[i - k]    # remove outgoing

        max_sum = max(max_sum, current_sum)

    return max_sum
```

---

# 7. Pattern Abstraction

## 🔹 Fixed Window Template

Use when:

- Window size is **constant (k)**

---

### Template

```python
window = sum(first k elements)

for i in range(k, n):
    window += nums[i]
    window -= nums[i - k]
```

---

## 🔹 Variable Window (contrast)

Use when:

- Size is NOT fixed
- Condition-based (e.g., sum ≤ k, no duplicates)

---

### Key Difference:

| Type            | Behavior        |
| --------------- | --------------- |
| Fixed Window    | Always size k   |
| Variable Window | Expand + shrink |

---

## 🔹 Recognition Triggers

- “subarray of size k”
- “maximum sum of k elements”
- “average of k elements”

👉 Immediately think: **Fixed Sliding Window**

---

# 8. Common Mistakes

## ❌ 1. Recomputing sum every time

Why it happens:

- Thinking in brute force

Fix:

- Always reuse previous computation

---

## ❌ 2. Off-by-one errors in loop

Example mistake:

```python
range(len(nums) - k + 1)  # used incorrectly in optimized version
```

Why:

- Mixing naive and optimized approaches

---

## ❌ 3. Going out of bounds

```python
nums[i + k]
```

Why:

- Incorrect indexing logic

---

## ❌ 4. Not initializing first window separately

Why:

- Trying to handle everything in one loop

Fix:

- Always treat first window as base case

---

# 🎯 Final Summary

## What is this concept?

Sliding Window (Fixed Size)

---

## What problem does it solve?

Efficiently process **contiguous subarrays of fixed size**

---

## Why is it powerful?

Transforms:

```
O(n * k) → O(n)
```

by reusing computation

---

## How it fits in your system

This is:

> 🔥 The **entry point** of Sliding Window (Section 3)

Mastering this enables:

- Variable window problems
- String-based window problems
- Advanced frequency-based windows

---

If you’re ready, next step I recommend:

👉 I give you **2–3 carefully selected problems** that force you to apply this exact pattern (with increasing difficulty)
