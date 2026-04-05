Good. Now we move to the third pattern—this one is deceptively simple but **extremely important in interviews**.

---

# 🔵 PATTERN 3 — Same Direction (Read / Write Pointers)

---

# 🧠 1. PROBLEM THIS PATTERN SOLVES

This pattern is NOT about:

- pairs ❌
- cycles ❌

It is about:

> **Transforming an array (or string) in-place**

---

### Typical problem shapes:

- “Remove duplicates in-place”
- “Move elements to the front/back”
- “Return new length after modification”
- “Do it without extra space”

---

### Core constraint:

```text
O(1) extra space
```

---

### Naive approach (what we avoid):

```text
Create new array → copy valid elements → return
```

👉 Works, but violates space constraint

---

# 🧠 2. CORE IDEA (MENTAL MODEL)

You use **two pointers moving forward**:

```text
read  → scans every element
write → builds the result
```

---

### Visual:

```text
[ a, b, b, c, c, d ]

  r
  w
```

---

### Key concept:

> One pointer **reads everything**
> One pointer **decides what survives**

---

# 🧠 3. WHY THIS WORKS (CRITICAL)

You are **reusing the same array as output storage**

---

### Think of it like:

- `read` = input stream
- `write` = output stream (but inside same array)

---

### Every time you accept a value:

```text
nums[write] = nums[read]
write++
```

---

### What are you doing logically?

> Compressing valid elements toward the front

---

# 🧪 4. SIMPLEST PROBLEM (PURE PATTERN)

## ✅ “Remove Duplicates from Sorted Array”

---

### Problem:

Given:

```text
nums = sorted array
```

Remove duplicates **in-place**, return new length.

---

### Example:

```text
Input:  [1, 1, 2, 2, 3]
Output: [1, 2, 3, _, _]
Length = 3
```

---

# 🧠 5. THINK BEFORE CODE

---

### Step 1 — What do we need?

- Keep only **unique elements**

---

### Step 2 — What structure helps us?

- Array is **sorted**

👉 duplicates are adjacent

---

### Step 3 — Strategy

- Always keep the **first occurrence**
- Skip duplicates

---

# 💻 6. BUILD SOLUTION STEP BY STEP

---

## Step 1 — Initialize pointers

```python
write = 1
```

---

### Why start at 1?

- First element is always valid
- No need to process it

---

```python
for read in range(1, len(nums)):
```

---

### Why start read from 1?

- We compare with previous element
- Index 0 has no previous

---

---

## Step 2 — Compare current with previous

```python
if nums[read] != nums[read - 1]:
```

---

### What this checks:

- Is this a **new value**?

---

### Why this works:

- Sorted array → duplicates are adjacent

---

---

## Step 3 — Write valid element

```python
nums[write] = nums[read]
```

---

### What this does:

- Moves the valid element forward

---

### What if we don’t do this?

- We won’t overwrite duplicates
- Array remains unchanged → wrong result

---

---

## Step 4 — Move write pointer

```python
write += 1
```

---

### Why?

- Next valid element goes to next position

---

---

## Step 5 — Return result

```python
return write
```

---

### Why return write?

- It represents **new length**
- Everything before `write` is valid

---

# 🔁 7. VISUAL EXECUTION

---

### Example:

```text
nums = [1, 1, 2, 2, 3]
```

---

### Initial:

```text
write = 1
read  = 1
```

---

### Step 1:

```text
read = 1 → nums[1] = 1
compare with nums[0] = 1 → same ❌ skip
```

---

### Step 2:

```text
read = 2 → nums[2] = 2
compare with nums[1] = 1 → different ✅

nums[write=1] = 2
write = 2
```

Array becomes:

```text
[1, 2, 2, 2, 3]
```

---

### Step 3:

```text
read = 3 → nums[3] = 2
compare with nums[2] = 2 → same ❌ skip
```

---

### Step 4:

```text
read = 4 → nums[4] = 3
compare with nums[3] = 2 → different ✅

nums[write=2] = 3
write = 3
```

---

### Final array:

```text
[1, 2, 3, _, _]
```

Return:

```text
3
```

---

# 🧠 8. WHAT YOU SHOULD NOTICE

- We never created a new array
- We reused the same memory
- We only wrote when necessary

---

# ⚠️ 9. COMMON MISTAKES

---

### ❌ Confusing read and write roles

- `read` → scans ALL elements
- `write` → only moves when needed

---

### ❌ Updating write every iteration

Breaks logic → duplicates remain

---

### ❌ Forgetting sorted assumption

If not sorted → this approach fails

---

# 🔁 10. VARIATIONS OF THIS PATTERN

---

### 🔹 Move Zeroes

- Keep non-zero values
- Push zeros to end

---

### 🔹 Remove Element

- Skip specific value

---

### 🔹 String Compression

- Write compressed form

---

👉 Same idea:

```text
filter → write → advance
```

---

# 🧠 11. PATTERN EXTRACTION

---

## 🔥 Trigger → Pattern → Structure → Flow

---

### ✅ Trigger

- In-place modification
- Filtering / removing / compressing
- O(1) space required

---

### ✅ Pattern

- Same direction (read/write)

---

### ✅ Structure

```text
read → scans
write → builds
```

---

### ✅ Flow

```text
for read:
    if valid:
        nums[write] = nums[read]
        write++
```

---

# 🧠 FINAL MENTAL MODEL

> You are not searching.
> You are **rewriting the array in-place**

---

# 🔚 SECTION 2 FOUNDATION COMPLETE

You now have:

- Opposite Direction → **comparison**
- Fast & Slow → **movement**
- Same Direction → **transformation**

---

# ✅ NEXT STEP (VERY IMPORTANT)

Now we move to:

## 🔁 PROBLEM LOOP (PHASE 2)

You said:

> You want to mix patterns (non-linear order) ✅

That’s **excellent** for pattern recognition.

---

👉 Start with ANY problem from your list.

Send me:

### Step 1 — Pattern Prediction

- What pattern?
- Why?
- What structure?

---

Then we begin the **guided loop**.

Your move.
