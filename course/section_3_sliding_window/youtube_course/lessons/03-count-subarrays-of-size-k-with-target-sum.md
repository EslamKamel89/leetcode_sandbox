This lesson is where the pattern **starts to stabilize in your brain**.

You’re no longer learning _how sliding window works_ — you’re learning:

> how to **adapt the same window mechanics to different problem goals**

Let’s reconstruct it properly.

---

# 🧠 Study Guide — Count Subarrays of Size K with Target Sum

(Third lesson — reinforces fixed sliding window abstraction)

---

# 1. Problem Reconstruction

## 🔹 Problem

You are given:

- An array `nums`
- An integer `target`
- An integer `k`

Your task:

> Count how many contiguous subarrays of size **exactly k** have a sum equal to `target`

---

## 🔹 Example

```python
nums = [2, 3, 2, 2, 3, 1, 3]
k = 3
target = 7
```

Valid windows:

```text
[2,3,2] → 7 ✅
[3,2,2] → 7 ✅
[2,2,3] → 7 ✅
[2,3,1] → 6 ❌
[3,1,3] → 7 ✅
...
```

👉 Total = **5 matches**

---

## 🔹 Constraints & Edge Cases

- Must be **contiguous**
- Must be exactly size `k`
- Can contain:
  - Negative numbers
  - Zero

- If `k > len(nums)` → return 0

---

## 🔹 Why this is Sliding Window

Recognition triggers:

- “subarray”
- “size k”
- “scan all possibilities”

👉 This is **Fixed Sliding Window again**

---

# 2. Mental Model (CRITICAL)

## 🔹 What changed from previous lessons?

Nothing in structure.

Only the **goal** changed:

| Lesson | Goal          |
| ------ | ------------- |
| 1      | Max sum       |
| 2      | Max product   |
| 3      | Count matches |

---

## 🔹 Core Idea

We maintain:

```text
current_sum → sum of current window
count → number of valid windows
```

---

## 🔹 What are we really doing?

We are sliding a fixed window and asking:

> “Does this window satisfy a condition?”

Instead of:

- maximizing
- minimizing

We are now **counting**

---

## 🔹 Brute Force Thinking

For each window:

- Compute sum from scratch → O(k)

Total:

```text
O(n * k)
```

---

## 🔹 Sliding Window Optimization

Reuse previous sum:

```text
new_sum = old_sum - outgoing + incoming
```

👉 Total becomes **O(n)**

---

# 3. Step-by-Step Solution Development

---

## 🔸 Step 1 — Process Initial Window

```python
current_sum = 0
for i in range(k):
    current_sum += nums[i]
```

---

### Why?

- Builds the first window
- Required baseline

If removed:

- No starting state

---

## 🔸 Step 2 — Initialize Count

```python
count = 1 if current_sum == target else 0
```

---

### Why this is CRITICAL

The first window is:

- Already valid
- Already computed

👉 If you skip this:

You **lose one valid answer**

This is one of the most common mistakes.

---

## 🔸 Step 3 — Slide the Window

```python
for i in range(len(nums) - k):
```

---

### Why this range?

- `i` = start of current window
- Stops before going out of bounds

---

## 🔸 Step 4 — Update Window

```python
current_sum -= nums[i]
current_sum += nums[i + k]
```

---

### Explanation

- Remove outgoing element
- Add incoming element

---

### If you remove only one:

- Window size becomes invalid

---

## 🔸 Step 5 — Check Condition

```python
if current_sum == target:
    count += 1
```

---

### Why?

This is the **problem-specific logic**

Important idea:

> Sliding window gives you candidates — you decide what to do with them

---

# 4. Visualization (Execution Trace)

```python
nums = [2,3,2,2,3,1,3]
k = 3
target = 7
```

---

### Initial Window

```text
[2,3,2] → sum = 7 → count = 1
```

---

### Slide 1

```text
remove 2, add 2 → sum = 7 → count = 2
```

---

### Slide 2

```text
remove 3, add 3 → sum = 7 → count = 3
```

---

### Slide 3

```text
remove 2, add 1 → sum = 6 → no count
```

---

### Slide 4

```text
remove 2, add 3 → sum = 7 → count = 4
```

---

### Final Answer

```text
count = 5
```

---

# 5. Complexity Analysis

## 🔹 Time

- Initial window: O(k)
- Sliding: O(n)

👉 **O(n)**

---

## 🔹 Space

- Only variables

👉 **O(1)**

---

# 6. Final Code

```python
def count_subarrays_with_target(nums, k, target):
    # Step 1: initial window
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]

    # Step 2: initialize count
    count = 1 if current_sum == target else 0

    # Step 3: slide window
    for i in range(len(nums) - k):
        current_sum -= nums[i]        # remove outgoing
        current_sum += nums[i + k]    # add incoming

        if current_sum == target:
            count += 1

    return count
```

---

# 7. Pattern Abstraction (IMPORTANT)

You now have the **full fixed window template**

---

## 🔹 General Template

```python
# 1. initialize window
state = process first k elements

# 2. apply logic on first window

# 3. slide
for i in range(...):
    remove outgoing
    add incoming

    apply logic
```

---

## 🔹 What changes per problem?

Only this part:

```python
apply logic
```

---

### Examples:

| Problem          | Logic                  |
| ---------------- | ---------------------- |
| Max sum          | max(...)               |
| Max product      | max(...)               |
| Count target sum | if condition → count++ |

---

👉 This is the **core abstraction**

---

# 8. Common Mistakes

---

## ❌ 1. Forgetting to count the first window

Why:

- It’s handled outside the loop

---

## ❌ 2. Wrong loop bounds

```python
range(len(nums) - k + 1)
```

Used incorrectly in optimized version

---

## ❌ 3. Mixing logic inside/outside loop

- First window logic must be separate

---

## ❌ 4. Forgetting problem goal

Mistake:

- Using `max` instead of counting

---

## ❌ 5. Not recognizing this is identical to previous problems

This is dangerous:

> You think you're solving a new problem, but you're not

---

# 🎯 Final Summary

---

## What did you actually learn?

You learned:

> Sliding Window = **structure + customizable logic**

---

## The Pattern Fully Formed

```text
Window mechanics → SAME
Problem goal → DIFFERENT
```

---

## Mental Model Upgrade

Before:

> Sliding window = sum trick

Now:

> Sliding window = **state maintenance + evaluation**

---

## Where you are in the curriculum

You are now solidifying:

> 🔹 Fixed Window Mastery (Section 3 — Lesson 1–3)

This directly aligns with your system:

> You should now recognize this pattern instantly and apply it confidently

---

## What comes next (important)

The next real jump will be:

> ❗ Variable Sliding Window (expand + shrink)

That’s where:

- logic becomes dynamic
- difficulty increases significantly

---

If you want to proceed correctly, I recommend:

👉 I give you **2–3 problems now that mix all 3 variations (max / product / count)**
This will test whether you truly internalized the pattern or just followed examples.
