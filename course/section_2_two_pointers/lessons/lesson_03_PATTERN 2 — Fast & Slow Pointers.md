Good. Now we shift mental models completely.

---

# 🔵 PATTERN 2 — Fast & Slow Pointers

---

# 🧠 1. PROBLEM THIS PATTERN SOLVES

This pattern is NOT about pairs.

It solves problems where:

- You have **movement over time**
- You care about:
  - **cycles**
  - **meeting points**
  - **relative position**

---

### Typical problem shapes:

- “Does this structure contain a **cycle**?”
- “Find the **middle** of a list”
- “Do two paths eventually **meet**?”

---

### Important distinction:

> Opposite pointers → comparing values
> Fast/Slow pointers → tracking **movement behavior**

---

# 🧠 2. CORE IDEA (MENTAL MODEL)

You create two pointers:

```text
slow → moves 1 step
fast → moves 2 steps
```

---

### Visual:

```text
Node1 → Node2 → Node3 → Node4 → Node5
  ↑
 slow

  ↑↑
 fast
```

---

### Key concept:

> They move at **different speeds on the same path**

---

# 🧠 3. WHY THIS WORKS (CRITICAL)

This pattern is based on **relative speed**.

---

## 🎯 Case 1 — No Cycle

```text
1 → 2 → 3 → 4 → 5 → None
```

- `fast` moves faster
- It reaches `None` first

👉 Conclusion: **No cycle**

---

## 🎯 Case 2 — Cycle Exists

```text
1 → 2 → 3 → 4 → 5
          ↑     ↓
          ← ← ← ←
```

Now imagine:

- slow = walking
- fast = running

---

### What happens?

Eventually:

```text
fast catches slow
```

👉 Because in a loop, faster always laps slower

---

### This is the key invariant:

> If there is a cycle, **they MUST meet**

---

# 🧪 4. SIMPLEST PROBLEM (PURE PATTERN)

## ✅ “Linked List Cycle”

---

### Problem:

Given a linked list:

👉 Determine if it contains a cycle

---

# 🧠 5. THINK BEFORE CODE

---

### Step 1 — What are we detecting?

- A loop in the structure

---

### Step 2 — What’s the constraint?

- We CANNOT use extra memory (like a set)

---

### Step 3 — Key insight

> If we move at different speeds,
> loop behavior reveals itself

---

# 💻 6. BUILD SOLUTION STEP BY STEP

---

## Step 1 — Initialize pointers

```python
slow = head
fast = head
```

### Why both start at same place?

- We want to compare their movement over time
- Starting differently breaks the invariant

---

## Step 2 — Move inside loop

```python
while fast and fast.next:
```

### Why this condition?

- `fast` moves 2 steps
- So we must ensure:
  - `fast` exists
  - `fast.next` exists

Otherwise → crash

---

## Step 3 — Move pointers

```python
slow = slow.next
fast = fast.next.next
```

---

### What this does:

- slow → +1 step
- fast → +2 steps

👉 This creates **relative motion**

---

## Step 4 — Check meeting

```python
if slow == fast:
    return True
```

---

### Why this works:

If there’s a cycle:

- fast keeps looping
- slow keeps looping
- fast eventually **laps** slow

---

## Step 5 — If loop ends

```python
return False
```

---

### Why?

- If fast reaches `None`
- That means no cycle

---

# 🔁 7. VISUAL EXECUTION (VERY IMPORTANT)

---

## Example with cycle:

```text
1 → 2 → 3 → 4 → 5
          ↑     ↓
          ← ← ← ←
```

---

### Step-by-step:

---

### Step 0:

```text
slow = 1
fast = 1
```

---

### Step 1:

```text
slow = 2
fast = 3
```

---

### Step 2:

```text
slow = 3
fast = 5
```

---

### Step 3:

```text
slow = 4
fast = 4   ← 💥 meet
```

👉 Cycle detected

---

# 🧠 8. DEEP INSIGHT (IMPORTANT)

---

## Why must they meet?

Let’s think mathematically:

- slow moves: +1 each step
- fast moves: +2 each step

---

### Relative speed:

```text
fast - slow = 1 step per iteration
```

---

### Inside a cycle:

- Distance is finite
- Fast is gaining 1 node per step

👉 Eventually distance = 0 → they meet

---

# 🔁 9. SECOND USE CASE — FIND MIDDLE

---

## Problem:

Find middle of linked list

---

### Same pattern, different goal:

```python
slow = head
fast = head
```

---

```python
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

```python
return slow
```

---

## 🧠 Why this works:

- fast moves twice as fast
- when fast reaches end
- slow is at **halfway point**

---

### Visual:

```text
1 → 2 → 3 → 4 → 5

slow → 3
fast → None
```

---

# ⚠️ 10. COMMON MISTAKES

---

### ❌ Using this for value comparison

Wrong pattern → use opposite pointers instead

---

### ❌ Forgetting fast.next check

Leads to crash

---

### ❌ Thinking it only works for linked lists

Also works for:

- arrays (cycle problems)
- math transformations (Happy Number)

---

# 🧠 11. PATTERN EXTRACTION

---

## 🔥 Trigger → Pattern → Structure → Flow

---

### ✅ Trigger

- Cycle detection
- Middle finding
- Repeated movement

---

### ✅ Pattern

- Fast & Slow pointers

---

### ✅ Structure

```text
slow = head
fast = head
```

---

### ✅ Flow

```text
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle exists
```

---

# 🧠 FINAL MENTAL MODEL

> You are not comparing values.
> You are analyzing **motion over time**

---

# ✅ YOUR TASK

You should now be able to answer:

1. Why does fast eventually catch slow in a cycle?
2. Why does fast reaching `None` guarantee no cycle?
3. Why does slow land at the middle?

---

When ready:

👉 **“Move to Pattern 3 — Same Direction”**

Or if you want:

👉 We can do a **guided cycle detection problem** before moving on.
