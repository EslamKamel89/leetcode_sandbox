Excellent—this is a **Same Direction pattern + frequency preprocessing**, applied to a **linked list**.

This problem is very important because it looks like “remove duplicates,” but it is actually:

> ❗ **Remove ALL nodes that appear more than once**
> (not “keep one copy”)

---

# 🧠 Step 1 — Pattern Prediction

### Correct classification:

> Same Direction (filtering) ✅
>
> - Hashing (frequency counting) ✅

---

### Why?

| Signal                | Present? |
| --------------------- | -------- |
| Unsorted data         | ✅       |
| Need frequency info   | ✅       |
| In-place filtering    | ✅       |
| Linked list traversal | ✅       |

---

👉 This is **NOT a pure two-pointer problem**

Because:

```text
We cannot decide locally (like sorted list)
```

---

# 🧠 Step 2 — What Makes This Problem HARD?

---

Compare with previous:

| Problem                       | Sorted? | Can decide locally? |
| ----------------------------- | ------- | ------------------- |
| Remove Duplicates (array)     | ✅      | ✅                  |
| Remove Duplicates (LL sorted) | ✅      | ✅                  |
| This problem                  | ❌      | ❌                  |

---

👉 Because:

```text
You don't know if a value is duplicate until you scan entire list
```

---

# 🧠 Step 3 — Correct Strategy (CRITICAL)

---

## Two-phase solution:

---

### 🔹 Phase 1 — Count frequencies

```text
value → count
```

---

### 🔹 Phase 2 — Filter nodes

```text
Keep nodes where count == 1
```

---

👉 This is the only clean way

---

# 💻 Step 4 — Your Optimal Solution

---

## 🔹 Phase 1 — Build frequency map

```python
freq = {}
current = head
while current:
    freq[current.val] = freq.get(current.val, 0) + 1
    current = current.next
```

---

### What this does:

- Counts occurrences of each value
- Time: O(n)
- Space: O(n)

---

---

## 🔹 Phase 2 — Build filtered list

```python
prev = ListNode()
new_head = prev
current = head
```

---

### Why dummy node?

```text
Avoid special case for head
```

---

---

## 🔹 Filtering logic

```python
if freq[current.val] == 1:
    prev.next = current
    prev = current
```

---

### Meaning:

- Keep only unique elements

---

---

## 🔹 Move forward

```python
current = current.next
```

---

---

## 🔹 Final cleanup

```python
prev.next = None
```

---

### ⚠️ CRITICAL

Without this:

```text
Old links may remain → corrupted list
```

---

---

## 🔹 Return

```python
return new_head.next
```

---

---

# 🔁 Step 5 — Visual Execution

---

### Input:

```text
1 → 2 → 3 → 2
```

---

## Phase 1:

```text
freq = {1:1, 2:2, 3:1}
```

---

## Phase 2:

```text
Keep: 1, 3
Remove: 2
```

---

### Result:

```text
1 → 3
```

---

---

# 🧠 Step 6 — What You Did RIGHT

---

### ✅ Correct decomposition (2 phases)

---

### ✅ Used hashmap appropriately

---

### ✅ Used dummy node (important skill)

---

### ✅ Properly terminated list

---

---

# ⚠️ Step 7 — Problems in First Solution

---

## 🔴 deleteDuplicatesUnsorted1

---

### Issue 1 — Order is broken

```python
for node_info in seen.values():
```

---

### Why?

```text
Dictionary iteration does NOT preserve original list order
```

---

👉 Violates requirement:

```text
Maintain original order
```

---

---

### Issue 2 — Storing nodes in dict

```python
seen[val] = [node, count]
```

---

### Problem:

- Only keeps one node reference
- Loses structure of list

---

👉 Incorrect design

---

---

# 🧠 Step 8 — Pattern Extraction

---

## 🔥 Trigger → Pattern → Structure → Flow

---

### ✅ Trigger

- Unsorted data
- Need to remove duplicates completely
- Cannot decide locally

---

### ✅ Pattern

- Hashing + Same Direction filtering

---

### ✅ Structure

```text
Phase 1 → count frequencies
Phase 2 → filter nodes
```

---

### ✅ Flow

```text
count values

for each node:
    if freq == 1:
        keep
    else:
        skip
```

---

# 🧠 Step 9 — DEEP INTUITION

---

This is the key idea:

> When decision depends on **global information**,
> you must **precompute it first**

---

### Compare:

| Problem                    | Strategy         |
| -------------------------- | ---------------- |
| Remove Duplicates (sorted) | local check      |
| This problem               | global frequency |

---

👉 That’s the key distinction

---

# 🧠 Step 10 — Pattern Connection

---

Compare:

| Problem              | Pattern                   |
| -------------------- | ------------------------- |
| Remove Element       | filter (local)            |
| Move Zeroes          | filter (local)            |
| Remove Duplicates II | filter (local constraint) |
| This problem         | filter (global condition) |

---

👉 Same pattern → different dependency

---

# 🧠 FINAL SUMMARY

---

### What is this problem?

Remove all nodes that appear more than once

---

### What problem does it solve?

Filtering based on global frequency

---

### Why does it work?

Because:

```text
We separate counting from filtering
```

---

### How it fits into system?

```text
Problem → global condition →
hash map →
Same Direction filtering →
O(n)
```

---

# 🧠 BIG TAKEAWAY

---

This problem teaches:

> If condition is not locally decidable →
> **compute global metadata first**

---

# ✅ NEXT STEP

You’re now handling:

- Local filtering
- Constraint filtering
- Partitioning
- Global filtering

---

Pick the next problem.

Start with:

### Step 1 — Pattern Prediction

We continue strengthening your pattern system.
