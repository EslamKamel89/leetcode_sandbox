Good. We’ll treat this like a focused module.

---

# 🧠 Pattern 1 — Frequency Map

---

# 1. What Problem Does This Pattern Solve?

Before code, lock this in:

## ❗ Core Problem

You are given a collection (array/string), and you need to:

- Count occurrences
- Compare distributions
- Detect duplicates or matches

---

## 🧠 Mental Model

Think of it like:

```text
You scan once → build a "count table" → use it to answer questions instantly
```

Instead of repeatedly asking:

> “How many times does X appear?”

You precompute it once.

---

# 2. What Is a Frequency Map?

A **frequency map** is:

```python
value → number of occurrences
```

---

## 🔍 Example

```text
s = "aabccc"
```

Becomes:

```text
{
  'a': 2,
  'b': 1,
  'c': 3
}
```

---

## 🧠 Why It Matters

Without it:

```text
Every count query = O(n)
```

With it:

```text
Every count query = O(1)
```

---

# 3. When Should Your Brain Trigger This Pattern?

You should **immediately think "frequency map"** when you see:

- “Count…”
- “How many times…”
- “Same characters?”
- “Anagram?”
- “Duplicates?”

---

# 4. LeetCode-Style Problem

---

## 🧩 Problem: “Valid Anagram”

> Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise `False`.

---

## 🔍 Examples

```text
Input: s = "anagram", t = "nagaram"
Output: True
```

```text
Input: s = "rat", t = "car"
Output: False
```

---

# 5. Think Like a Developer (VERY IMPORTANT)

---

## ❌ Naive Thinking

Sort both strings:

```text
O(n log n)
```

Works—but misses the pattern.

---

## ✅ Correct Thinking (Pattern-Based)

> “If both strings have the SAME frequency for every character → they are anagrams”

---

# 6. Step-by-Step Solution (Build It Slowly)

---

## Step 1 — Create Frequency Maps

```python
freq_s = {}
freq_t = {}
```

### Why?

We need to **store counts separately** for comparison.

If you skip this → you have nothing to compare.

---

## Step 2 — Count Characters in `s`

```python
for ch in s:
    freq_s[ch] = freq_s.get(ch, 0) + 1
```

### Explanation

- `ch` → current character
- `get(ch, 0)` → safe access
- `+1` → increment count

👉 This builds the full distribution of `s`.

---

## Step 3 — Count Characters in `t`

```python
for ch in t:
    freq_t[ch] = freq_t.get(ch, 0) + 1
```

👉 Same logic, separate storage.

---

## Step 4 — Compare Maps

```python
return freq_s == freq_t
```

### Why this works

Python compares:

- keys
- values

👉 If anything differs → False

---

# 7. Full Code (Clean Version)

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq_s = {}
    freq_t = {}

    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0) + 1

    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0) + 1

    return freq_s == freq_t
```

---

# 8. Visual Execution (Step-by-Step)

---

## Input

```text
s = "anagram"
t = "nagaram"
```

---

## Build freq_s

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

---

## Build freq_t

```text
n → 1
a → 3
g → 1
r → 1
m → 1
```

---

## Comparison

```text
freq_s == freq_t → True
```

---

# 9. Optimization Insight (Important)

You can reduce space to **one hashmap**.

---

## Improved Idea

- Increment for `s`
- Decrement for `t`

---

### Code

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0
```

---

## 🧠 Why This Works

- Matching characters cancel out
- Leftover values → mismatch

---

# 10. Complexity Analysis

---

## Time Complexity

```text
O(n)
```

- One pass over both strings

---

## Space Complexity

```text
O(k)
```

- `k` = unique characters

---

# 11. What Would Break This?

---

## ❌ If you forget `.get(ch, 0)`

```python
freq[ch] += 1  # ERROR if ch not exists
```

---

## ❌ If you don’t check lengths

```text
"ab" vs "a" → wrong True risk
```

---

## ❌ If you reuse same dict incorrectly

You’ll mix counts and corrupt logic.

---

# 🧾 Final Summary

---

## What this pattern is

A way to:

> Count occurrences efficiently using a hashmap.

---

## What problem it solves

- Avoid repeated counting
- Enable O(n) solutions for frequency-based problems

---

## Core idea

> “Precompute counts once, reuse them instantly.”

---

## How it fits into bigger system

This pattern is the base for:

- Anagrams
- Duplicates
- Sliding Window (frequency tracking)
- Many string problems

---

---

If you’re ready, next we’ll do:

👉 **Complement Lookup (Two Sum pattern)** — this is where things start getting really powerful.
