Good—this is where things start to feel “clever”.

---

# 🧠 Pattern 2 — Complement Lookup (Two Sum Pattern)

---

# 1. What Problem Does This Pattern Solve?

---

## ❗ Core Problem

You are given:

- An array
- A target

And you need to:

> Find elements that satisfy a relationship (usually sum)

---

## 🧠 Example

```text
nums = [2, 7, 11, 15]
target = 9
```

---

## ❌ Naive Thinking

```text
Try all pairs → O(n²)
```

You compare every element with every other element.

---

## 💡 Key Insight (THIS IS THE PATTERN)

Instead of asking:

> “Which two numbers sum to 9?”

Ask:

> “For each number, what do I need to complete it?”

---

## 🔥 This is called the **complement**

```text
complement = target - current_number
```

---

# 2. Mental Model

---

## 🧠 Think like this:

```text
"I'm holding number X
I need Y to complete the target"
```

So you:

1. Check if Y exists
2. If not → store X for future

---

## 🔁 Flow

```text
current → compute complement → check memory → store current
```

---

# 3. LeetCode-Style Problem

---

## 🧩 Problem: “Two Sum”

> Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

---

## 🔍 Example

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

---

# 4. Think Like a Developer (CRITICAL)

---

## ❌ Wrong approach mindset

> “Let me try all combinations”

---

## ✅ Correct mindset

> “Let me remember what I’ve seen so far, so I can instantly check complements”

---

# 5. Step-by-Step Solution (Build Slowly)

---

## Step 1 — Create storage

```python
seen = {}
```

### Why?

We need:

```text
number → index
```

So we can return indices.

---

## Step 2 — Iterate

```python
for i, num in enumerate(nums):
```

### Why enumerate?

We need:

- value (`num`)
- index (`i`)

---

## Step 3 — Compute complement

```python
complement = target - num
```

### Why?

This tells us:

> “What number do I need to complete the target?”

---

## Step 4 — Check if complement exists

```python
if complement in seen:
    return [seen[complement], i]
```

### Explanation

- If complement is already seen → we found the pair
- `seen[complement]` gives its index

👉 This is the **O(1) lookup power**

---

## Step 5 — Store current number

```python
seen[num] = i
```

### ⚠️ VERY IMPORTANT ORDER

We store **after checking**

---

## ❗ Why order matters

If you store first:

```text
num = 3, target = 6
complement = 3
```

You might match the same element with itself ❌

---

# 6. Full Code

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
```

---

# 7. Visual Execution (Step-by-Step)

---

## Input

```text
nums = [2, 7, 11, 15]
target = 9
```

---

## Iteration 1

```text
i = 0, num = 2
complement = 7
```

Check:

```text
7 in seen? → NO
```

Store:

```text
seen = {2: 0}
```

---

## Iteration 2

```text
i = 1, num = 7
complement = 2
```

Check:

```text
2 in seen? → YES ✅
```

Return:

```text
[0, 1]
```

---

# 8. Why This Works

---

## 🧠 Key Idea

You convert:

```text
pair search (2D problem)
```

Into:

```text
lookup problem (1D + memory)
```

---

## 💡 Deep Insight

Instead of:

- searching forward AND backward

You:

- only move forward
- use memory to simulate the past

---

# 9. Complexity Analysis

---

## Time

```text
O(n)
```

- One pass
- Each lookup is O(1)

---

## Space

```text
O(n)
```

- In worst case, store all elements

---

# 10. Recognition Signals (VERY IMPORTANT)

---

## 🚨 Use this pattern when you see:

- “Two elements…”
- “Find pair…”
- “Sum equals target”
- “Difference equals k”
- “Return indices”

---

# 11. Variations You’ll See

---

## 🔁 Slight changes, same pattern:

### 1. Difference instead of sum

```text
a - b = k
```

---

### 2. Store values instead of indices

---

### 3. Count pairs instead of returning indices

---

# 12. What Would Break This?

---

## ❌ Storing before checking

Leads to:

```text
Using same element twice
```

---

## ❌ Not using hashmap

Back to:

```text
O(n²)
```

---

## ❌ Overwriting indices blindly

If duplicates matter, you must be careful.

---

# 🧾 Final Summary

---

## What this pattern is

A way to:

> Find relationships (like sum) using complement + memory

---

## What problem it solves

- Eliminates nested loops
- Converts pair search into lookup

---

## Core idea

> “For each element, compute what you need and check if you've already seen it.”

---

## How it fits into bigger system

This pattern evolves into:

- Prefix sum + hashmap
- Sliding window (with constraints)
- 2-sum variations in trees & graphs

---

---

If you're ready, next we go deeper:

👉 **Prefix Sum** — this is where subarray problems become solvable in O(n) instead of O(n²).
