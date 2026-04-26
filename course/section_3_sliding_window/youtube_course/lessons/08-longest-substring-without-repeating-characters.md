This is **the most important problem in Sliding Window**.

If you truly understand this one, you’ve crossed from “pattern exposure” → **pattern mastery**.

This is the canonical interview problem.

---

# 🧠 Study Guide — Longest Substring Without Repeating Characters

(Full variable window + constraint control)

---

# 1. Problem Reconstruction

## 🔹 Problem

You are given:

- A string `s`

Your task:

> Find the **length of the longest substring** with **all unique characters**

---

## 🔹 Example

```python id="p8qj4t"
s = "abccbbq"
```

Valid substrings:

```text id="qlj3r4"
"abc" → length 3
"cbq" → length 3
"bbq" → ❌ (duplicate)
```

👉 Longest = **3**

---

## 🔹 Key Constraints

- Substring must be **contiguous**
- Characters must be **unique (no duplicates)**

---

## 🔹 Why this is Sliding Window

- Substring → contiguous
- Size unknown → variable window
- Constraint-based → uniqueness

👉 **Variable Sliding Window**

---

# 2. Mental Model (CRITICAL)

---

## 🔴 What changed from previous problems?

Before:

```text id="p6gq2g"
Constraint = numeric (sum)
```

Now:

```text id="2ehl6k"
Constraint = structural (no duplicates)
```

---

## 🔹 Core Idea

We maintain:

```text id="sv8g1g"
window → substring [start … end]
window_map → frequency of characters
```

---

## 🔹 What defines a valid window?

```text id="lx7km9"
All character counts ≤ 1
```

---

## 🔹 Key Behavior

### Expand

- Add character
- Might break constraint

### Shrink

- Remove characters
- Until constraint restored

---

## 🔴 Critical Insight

> You don’t shrink once — you shrink **until valid**

---

## 🔹 Decision Rule

```text id="y2y82k"
if duplicate exists → shrink
else → expand and update answer
```

---

# 3. Step-by-Step Solution Development

---

## 🔸 Step 1 — Initialize State

```python id="x3g0ok"
from collections import Counter

window_map = Counter()
start = 0
longest = 0
```

---

### Why?

- Track frequencies
- Track window boundaries
- Track best answer

---

## 🔸 Step 2 — Expand Window

```python id="a0nn3m"
for end in range(len(s)):
    char = s[end]
    window_map[char] += 1
```

---

### Explanation

- Add new character to window
- This may introduce duplicates

---

## 🔸 Step 3 — Shrink Until Valid

```python id="3d5k7x"
while window_map[char] > 1:
    window_map[s[start]] -= 1
    start += 1
```

---

### Why check only `char`?

Because:

- Only the new character can break the constraint

---

### Why `while`?

Because:

- Removing one char may not fix the duplicate

---

## 🔴 Example of why while is needed

```text id="3n71lm"
window = "abca"
```

Adding `a` creates duplicate

You must remove until only one `a` remains

---

## 🔸 Step 4 — Update Longest

```python id="67hyx6"
length = end - start + 1
longest = max(longest, length)
```

---

### Why here?

Because:

- Window is guaranteed valid (no duplicates)

---

# 4. Visualization (Execution Trace)

```python id="g4q6qh"
s = "abccbbq"
```

---

### Step 1

```text id="3fl4l5"
[a] → valid → longest = 1
```

---

### Step 2

```text id="h6e73z"
[ab] → valid → longest = 2
```

---

### Step 3

```text id="67r8gy"
[abc] → valid → longest = 3
```

---

### Step 4 (duplicate)

```text id="7v5xg2"
[abcc] → duplicate 'c'
```

Shrink:

```text id="7vdc8q"
remove a → still duplicate
remove b → still duplicate
remove c → fixed
```

Window becomes:

```text id="gdks5p"
[c]
```

---

### Continue...

Eventually:

```text id="czjx22"
"cbq" → length 3
```

---

# 5. Complexity Analysis

---

## 🔹 Time Complexity

- Each char added once
- Each char removed once

👉

```text id="n6v5n8"
O(n)
```

---

## 🔹 Space Complexity

- Map stores characters

👉

```text id="2p7zv7"
O(n) (worst case: all unique)
```

---

# 6. Final Code

```python id="8rxt54"
from collections import Counter

def longest_unique_substring(s):
    window_map = Counter()
    start = 0
    longest = 0

    for end in range(len(s)):
        char = s[end]
        window_map[char] += 1

        while window_map[char] > 1:
            window_map[s[start]] -= 1
            start += 1

        length = end - start + 1
        longest = max(longest, length)

    return longest
```

---

# 7. Pattern Abstraction (VERY IMPORTANT)

---

## 🔹 Full Variable Window Template

```python id="jvsl2k"
start = 0
state = {}

for end in range(n):
    add element

    while constraint violated:
        remove element
        start += 1

    update answer
```

---

## 🔹 Constraint Types You've Seen

| Problem         | Constraint                   |
| --------------- | ---------------------------- |
| Sum problem     | sum ≤ target                 |
| This problem    | no duplicates                |
| Future problems | k distinct, frequency limits |

---

👉 This is the **universal template**

---

# 8. Common Mistakes

---

## ❌ 1. Using `if` instead of `while`

Fails when multiple removals needed

---

## ❌ 2. Checking all characters for duplicates

Unnecessary — only check the new one

---

## ❌ 3. Updating longest before fixing window

Leads to invalid answers

---

## ❌ 4. Using set instead of map

Set cannot track counts → breaks logic

---

## ❌ 5. Not understanding WHY shrinking works

Key idea:

> Shrinking removes violations step-by-step

---

# 🎯 Final Summary

---

## What did you actually learn?

You learned:

> Sliding Window with **constraint enforcement**

---

## Biggest Upgrade in Entire Section

```text id="z8wqgd"
Static rules → Dynamic constraints
```

---

## Complete Mental Model

```text id="ct43z9"
Expand → Break constraint → Shrink → Restore → Update
```

---

## Why this problem is critical

This exact logic appears in:

- Longest substring problems
- At most K distinct characters
- Minimum window substring (hard)

---

## Where you are now

You’ve completed:

> ✅ Fixed Window
> ✅ Variable Window (sum-based)
> ✅ Variable Window (constraint-based)

This satisfies your Section 3 goal:

> “Handle contiguous subarrays with dynamic boundaries”

---

## Final Instructor Insight

If you truly understand this problem, you should be able to answer:

> ❓ “What exactly triggers shrinking, and why must it be a loop?”

If you can answer that confidently:

👉 You’ve mastered Sliding Window.

---

## What I recommend next

Now don’t rush forward.

👉 You should:

1. Solve this problem **from scratch**
2. Then solve:
   - At most K distinct characters
   - Minimum window substring

These will test whether your understanding is **real or shallow**

---

If you want, I can now:

- Give you a **targeted practice set (2–3 problems)** to lock this in
- Or test you with a **tricky variation that breaks naive thinking**
