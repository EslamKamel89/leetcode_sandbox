This lesson is **the most important one so far in Section 3**.

Why? Because it fixes a **fundamental limitation** from the previous lesson and introduces the **correct general solution for anagram problems**.

Let’s go step by step.

---

# 🧠 Study Guide — Count Substring Anagrams (Fixed Window + HashMap)

(Transition from set → frequency map)

---

# 1. Problem Reconstruction

## 🔹 Problem

You are given:

- A string `s`
- A string `pattern`

Your task:

> Count how many substrings of `s` are anagrams of `pattern`

---

## 🔹 Example

```python
s = "gattaca"
pattern = "at"
```

Substrings of size 2:

```text
ga → ❌
at → ✅
tt → ❌
ta → ✅
ac → ❌
ca → ❌
```

👉 Answer = **2**

---

## 🔹 Key Difference from Previous Lesson

| Previous              | Current               |
| --------------------- | --------------------- |
| Characters are unique | Characters can repeat |

---

## 🔴 Why this matters

Example:

```text
Window: "tt"
Set → {t}
```

You lose:

- Frequency information ❌

👉 Set is no longer valid

---

## 🔹 Why this is Sliding Window

Signals:

- substring
- fixed size = len(pattern)

👉 Fixed window again

---

# 2. Mental Model (CRITICAL)

---

## 🔹 What changed conceptually?

You upgraded:

```text
Set  →  Frequency Map (HashMap)
```

---

## 🔹 Why a Map?

Because:

> We care about **how many times each character appears**

---

## 🔹 Core Idea

We maintain:

```text
window_map   → counts of chars in window
pattern_map  → counts of chars in pattern
```

---

## 🔹 What are we checking?

At each window:

> “Do both maps have identical frequencies?”

---

## 🔹 Sliding Window Behavior

Same structure:

```text
remove outgoing char → decrement count
add incoming char → increment count
```

---

## 🔹 Key Insight

This is the **correct generalization** of anagram detection.

---

# 3. Step-by-Step Solution Development

---

## 🔸 Step 1 — Build Pattern Map

```python
from collections import Counter

pattern_map = Counter(pattern)
```

---

### Why?

- Stores required frequencies
- Example:

```text
pattern = "aab"
→ {a:2, b:1}
```

---

## 🔸 Step 2 — Build Initial Window Map

```python
window_map = Counter(s[:k])
```

Where:

```python
k = len(pattern)
```

---

### Why?

- First window must be processed separately

---

## 🔸 Step 3 — Initialize Count

```python
count = 1 if window_map == pattern_map else 0
```

---

### Why?

Same recurring rule:

> First window is already valid candidate

---

## 🔸 Step 4 — Slide Window

```python
for i in range(len(s) - k):
```

---

## 🔸 Step 5 — Update Window Map

```python
window_map[s[i]] -= 1
window_map[s[i + k]] += 1
```

---

### Explanation

#### Remove outgoing

```python
window_map[s[i]] -= 1
```

- Decrease frequency

---

#### Add incoming

```python
window_map[s[i + k]] += 1
```

---

## 🔸 ⚠️ Important Detail (VERY IMPORTANT)

When count becomes 0:

```python
if window_map[s[i]] == 0:
    del window_map[s[i]]
```

---

### Why?

Without this:

```text
{a:1, b:1, c:0} ≠ {a:1, b:1}
```

Even though logically same

---

## 🔸 Step 6 — Compare Maps

```python
if window_map == pattern_map:
    count += 1
```

---

# 4. Visualization (Execution Trace)

```python
s = "gattaca"
pattern = "at"
k = 2
```

---

### Initial Window

```text
"ga" → {g:1, a:1} ≠ {a:1, t:1}
count = 0
```

---

### Slide 1

```text
remove g, add t → {a:1, t:1} ✅
count = 1
```

---

### Slide 2

```text
remove a, add t → {t:2} ❌
```

---

### Slide 3

```text
remove t, add a → {t:1, a:1} ✅
count = 2
```

---

# 5. Complexity Analysis

---

## 🔹 Time Complexity

- Sliding: O(n)
- Map comparison: O(k)

👉 Total:

```text
O(n * k)
```

---

## 🔹 Space Complexity

- Map size ≤ k

👉 **O(k)**

---

# 6. Final Code

```python
from collections import Counter

def count_anagram_substrings(s, pattern):
    k = len(pattern)

    pattern_map = Counter(pattern)
    window_map = Counter(s[:k])

    count = 1 if window_map == pattern_map else 0

    for i in range(len(s) - k):
        # remove outgoing
        window_map[s[i]] -= 1
        if window_map[s[i]] == 0:
            del window_map[s[i]]

        # add incoming
        window_map[s[i + k]] += 1

        if window_map == pattern_map:
            count += 1

    return count
```

---

# 7. Pattern Abstraction (CRITICAL)

---

## 🔹 Fixed Window + Frequency Map Template

```python
state = Counter(first k elements)

for i:
    decrement outgoing
    remove if zero
    increment incoming

    compare with target
```

---

## 🔹 What changed across lessons?

| Lesson                  | State Type |
| ----------------------- | ---------- |
| Max sum                 | number     |
| Max product             | number     |
| Has anagram (unique)    | set        |
| Count anagram (general) | map        |

---

👉 This is **progressive abstraction**

---

# 8. Common Mistakes

---

## ❌ 1. Using set instead of map

Why wrong:

- loses duplicates

---

## ❌ 2. Not removing zero-count keys

Leads to:

- false mismatches

---

## ❌ 3. Thinking equality is O(1)

Reality:

- O(k)

---

## ❌ 4. Forgetting first window

Still the most common bug

---

## ❌ 5. Mixing logic

- Using max instead of count
- Using sum logic incorrectly

---

# 🎯 Final Summary

---

## What did you actually learn?

You learned:

> Sliding Window can maintain **frequency distributions**

---

## Biggest Upgrade So Far

```text
Set → Map (frequency-aware state)
```

---

## Real Understanding

Sliding Window is:

```text
State representation + incremental update + condition check
```

---

## Why this lesson is critical

Because:

> This is the **real version of anagram problems used in interviews**

---

## Where you are now

You have mastered:

> ✅ Fixed Window (full spectrum)

- numeric state
- structural state
- frequency state

This satisfies your section goal:

> “Handle contiguous subarrays with dynamic boundaries (fixed stage first)”

---

## What comes next (VERY IMPORTANT)

Now you’re ready for:

> 🔥 Variable Sliding Window

Where:

- window size is NOT fixed
- you must decide when to shrink

---

If you want to continue correctly, I recommend:

👉 Next step: I guide you through your **first variable window problem (Longest Substring Without Repeating Characters)**
This is where difficulty jumps significantly.
