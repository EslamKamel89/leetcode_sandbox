This lesson is where **variable sliding window becomes real skill**, not just a trick.

You’re no longer just _finding a window_ — you’re now **optimizing over all valid windows**.

That’s a major jump.

---

# 🧠 Study Guide — Longest Subarray with Target Sum

(First optimization problem using variable window)

---

# 1. Problem Reconstruction

## 🔹 Problem

You are given:

- An array `nums` (non-negative integers)
- A target sum `target`

Your task:

> Find the **length of the longest subarray** whose sum equals `target`

---

## 🔹 Example

```python
nums = [4, 3, 3, 2, 1, 1, 7]
target = 10
```

Valid windows:

```text
[4,3,3] → 10 (length 3)
[3,3,2,1,1] → 10 (length 5) ← longest
```

👉 Answer = **5**

---

## 🔹 Key Differences from Previous Problem

| Previous            | Current            |
| ------------------- | ------------------ |
| Return indices      | Return length      |
| Stop when found     | Continue searching |
| One solution enough | Need best solution |

---

## 🔹 Why this is Sliding Window

- Subarray
- Contiguous
- Variable size

👉 **Variable Sliding Window**

---

# 2. Mental Model (CRITICAL)

---

## 🔹 What changed conceptually?

Before:

```text
Find ONE valid window
```

Now:

```text
Find the BEST among ALL valid windows
```

---

## 🔹 Core Idea

We maintain:

```text
start → left boundary
end → right boundary
window_sum → sum of current window
longest → best length found so far
```

---

## 🔹 Decision Logic

Same as previous lesson:

```text
if sum < target → expand
if sum > target → shrink
if sum == target → update answer
```

---

## 🔴 Critical Difference

Even when you find a valid window:

❌ DO NOT stop
✅ KEEP searching

---

## 🔹 Why this works

Because:

- All numbers are non-negative
- Expanding increases sum
- Shrinking decreases sum

---

# 3. Step-by-Step Solution Development

---

## 🔸 Step 1 — Initialize State

```python
start = 0
window_sum = 0
longest = -1
```

---

### Why `-1`?

- If no valid subarray exists → return -1

---

## 🔸 Step 2 — Expand Window

```python
for end in range(len(nums)):
    window_sum += nums[end]
```

---

### Explanation

- Add new element into window
- Grow window

---

## 🔸 Step 3 — Shrink When Needed

```python
while window_sum > target:
    window_sum -= nums[start]
    start += 1
```

---

### Why while?

- You may overshoot heavily
- Need multiple removals

---

## 🔸 Step 4 — Check and Update

```python
if window_sum == target:
    length = end - start + 1
    longest = max(longest, length)
```

---

### Why `end - start + 1`?

Because:

- Both indices are inclusive

---

## 🔴 Important Order

1. Expand
2. Shrink if needed
3. THEN check

---

# 4. Visualization (Execution Trace)

```python
nums = [4,3,3,2,1,1,7]
target = 10
```

---

### Step 1

```text
[4] → sum = 4 → expand
```

---

### Step 2

```text
[4,3] → sum = 7 → expand
```

---

### Step 3

```text
[4,3,3] → sum = 10 ✅
length = 3 → longest = 3
```

---

### Step 4

```text
[4,3,3,2] → sum = 12 ❌ → shrink
```

```text
remove 4 → sum = 8
```

---

### Step 5

```text
[3,3,2,1] → sum = 9 → expand
```

---

### Step 6

```text
[3,3,2,1,1] → sum = 10 ✅
length = 5 → longest = 5
```

---

### Continue...

Other matches exist but smaller → ignored

---

# 5. Complexity Analysis

---

## 🔹 Time Complexity

- Each element added once
- Each element removed once

👉

```text
O(n)
```

---

## 🔹 Space Complexity

```text
O(1)
```

---

# 6. Final Code

```python
def longest_subarray_sum(nums, target):
    start = 0
    window_sum = 0
    longest = -1

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum > target:
            window_sum -= nums[start]
            start += 1

        if window_sum == target:
            length = end - start + 1
            longest = max(longest, length)

    return longest
```

---

# 7. Pattern Abstraction (VERY IMPORTANT)

---

## 🔹 Variable Window Template (Refined)

```python
start = 0
state = initial

for end in range(n):
    add element

    while constraint violated:
        remove element
        start += 1

    if condition satisfied:
        update answer
```

---

## 🔹 What varies per problem?

| Problem          | Logic             |
| ---------------- | ----------------- |
| Find subarray    | return indices    |
| Longest subarray | max length        |
| Count subarrays  | increment counter |

---

👉 Same structure, different goal

---

# 8. Common Mistakes

---

## ❌ 1. Returning early

Wrong:

```python
return when sum == target
```

---

## ❌ 2. Updating longest before shrinking

Leads to:

- invalid windows

---

## ❌ 3. Forgetting `+1` in length

```python
end - start   ❌
end - start + 1 ✅
```

---

## ❌ 4. Using this with negative numbers

Algorithm breaks

---

## ❌ 5. Thinking this is different from previous problem

It’s the **same structure + different goal**

---

# 🎯 Final Summary

---

## What did you actually learn?

You learned:

> Sliding Window can **optimize across all valid windows**

---

## Concept Upgrade

```text
Find one → Track best
```

---

## Full Mental Model Now

```text
Expand → Shrink → Evaluate → Continue
```

---

## Why this matters

This exact pattern appears in:

- Longest substring problems
- Maximum window constraints
- Optimization problems in interviews

---

## Where you are now

You’ve completed:

> ✅ Variable Window Core (Find + Optimize)

This is the **heart of sliding window mastery** in your system

---

## What comes next (VERY IMPORTANT)

Next problems will introduce:

> 🔥 Constraint-based windows (harder)

Examples:

- No repeating characters
- At most K distinct elements
- Minimum window substring

---

If you want to move correctly:

👉 Next step should be:

**Longest Substring Without Repeating Characters**

This is the **most important problem in sliding window** and will test everything you’ve learned so far.
