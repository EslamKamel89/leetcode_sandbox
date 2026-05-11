# Step 1 — Pattern Prediction

This is another:

# Pattern B — Monotonic Stack

problem.

More specifically:

# Next Greater Element Pattern

This is one of the canonical monotonic stack templates.

---

# Why This Problem Matters

Daily Temperatures taught:

```text id="n1ge1"
future elements resolve past unresolved elements
```

This problem isolates that pattern even more cleanly.

In fact:

> Daily Temperatures is essentially a disguised Next Greater Element problem.

This problem removes:

- waiting days calculation
- index distance logic

and focuses purely on:

```text id="n2ge1"
nearest future greater value
```

That makes the monotonic pattern easier to see directly.

---

# The Real Problem

For each number:

```text id="n3ge1"
find first larger number to the right
```

This is the critical signal:

```text id="n4ge1"
first greater to the right
```

Whenever you see:

- next greater
- previous smaller
- nearest larger
- first greater

you should immediately think:

# monotonic stack

---

# Brute Force Perspective

Your first solution does:

```python id="n5ge1"
for i:
    for j:
```

For each number:

- scan right side
- stop at first greater element

Works logically.

But complexity:

```text id="n6ge1"
O(n²)
```

because repeated rescanning happens.

---

# Core Monotonic Insight

Suppose:

```text id="n7ge1"
nums2 = [1,3,4,2]
```

When processing:

- `1`
  → unresolved

Then `3` arrives:

- resolves `1`

Then `4` arrives:

- resolves `3`

Notice:

```text id="n8ge1"
future larger values progressively resolve previous smaller values
```

That is the exact monotonic stack lifecycle.

---

# Important Difference from Daily Temperatures

Daily Temperatures needed:

- indices
- distance calculations

This problem only needs:

- next larger VALUE

So your stack stores:

```text id="n9ge1"
numbers themselves
```

instead of:

- `[temp, index]`

This simplification is important.

---

# Step 2 — High-Level Strategy

We process `nums2` left → right.

Why `nums2`?

Because:

- next-greater relationships exist inside nums2

`nums1` is just:

- query subset

---

# Main Idea

The stack stores:

```text id="n10ge1"
numbers still waiting for next greater element
```

Whenever larger number arrives:

- resolve smaller unresolved numbers

---

# Why HashMap Exists

This line:

```python id="n11ge1"
nums1_hash = {num: i for i, num in enumerate(nums1)}
```

creates:

```text id="n12ge1"
value → answer index
```

Example:

```python id="n13ge1"
nums1 = [4,1,2]
```

Hash map:

```python id="n14ge1"
{
    4:0,
    1:1,
    2:2
}
```

---

# Why Needed?

When we resolve a value:

```text id="n15ge1"
we must know WHERE to write answer
```

Without hashmap:

- linear search required
- complexity worsens

---

# Step 3 — Code Reconstruction

---

# HashMap Creation

```python id="n16ge1"
nums1_hash = {num: i for i, num in enumerate(nums1)}
```

---

# What This Stores

Maps:

- number
  → result-array position

---

# Why Numbers Are Safe Keys

Problem guarantees:

```text id="n17ge1"
all integers are unique
```

Very important.

Otherwise:

- duplicates create ambiguity

---

# Result Initialization

```python id="n18ge1"
result = [-1] * len(nums1)
```

---

# Why Default = -1?

Default meaning:

```text id="n19ge1"
no greater future element exists
```

Only resolved elements get updated.

---

# Stack Initialization

```python id="n20ge1"
stack = []
```

---

# What Stack Stores

Unresolved numbers from nums1.

Important detail:

- only nums1 values matter

So your optimization:

```python id="n21ge1"
if num in nums1_hash:
    stack.append(num)
```

reduces unnecessary storage.

Good optimization.

---

# Main Loop

```python id="n22ge1"
for i, num in enumerate(nums2):
```

---

# Why Traverse nums2?

Because:

- next-greater relationships are defined there

nums1 only asks queries about those relationships.

---

# Core While Loop

```python id="n23ge1"
while stack and stack[-1] < num:
```

This is the monotonic-stack heart.

---

# Meaning

As long as current number is larger than unresolved top:

```text id="n24ge1"
we found next greater element
```

---

# Why Stack Is Monotonic

Suppose stack:

```text id="n25ge1"
[4,2]
```

top = 2

If current number = 5:

- 5 resolves 2
- then resolves 4

After popping:

- remaining stack still decreasing

Thus:

- stack maintains decreasing order

---

# Pop Unresolved Value

```python id="n26ge1"
val = stack.pop()
```

---

# Conceptual Meaning

This value waited until:

- first larger future element appeared

Now resolved forever.

---

# Record Answer

```python id="n27ge1"
result[nums1_hash[val]] = num
```

---

# Why This Works

Example:

```python id="n28ge1"
val = 1
num = 3
```

Meaning:

```text id="n29ge1"
next greater element of 1 is 3
```

Hash map gives:

- where 1 belongs inside result array

---

# Conditional Push

```python id="n30ge1"
if num in nums1_hash:
    stack.append(num)
```

---

# Why Only nums1 Values?

We only care about answering:

- nums1 queries

So numbers not in nums1:

- do not need future tracking

This is a clever optimization.

---

# Important Alternative Design

Many solutions:

- process ALL nums2 values
- build complete next-greater map

Then:

- answer nums1 queries afterward

That version is often cleaner conceptually.

Your version:

- saves some memory
- slightly more optimized

Both are valid.

---

# Step 4 — Visual Execution

Let’s trace:

```text id="n31ge1"
nums1 = [4,1,2]
nums2 = [1,3,4,2]
```

---

# Initial

```python id="n32ge1"
result = [-1,-1,-1]
stack = []
```

Hash map:

```python id="n33ge1"
{
    4:0,
    1:1,
    2:2
}
```

---

# num = 1

Stack empty.

1 belongs to nums1.

Push:

```python id="n34ge1"
[1]
```

---

# num = 3

3 > 1

Resolve:

```python id="n35ge1"
result[1] = 3
```

Stack empty.

3 not in nums1:

- don't push

---

# num = 4

4 in nums1.

Push:

```python id="n36ge1"
[4]
```

---

# num = 2

2 < 4

Cannot resolve.

Push:

```python id="n37ge1"
[4,2]
```

---

# End of Array

Stack still contains:

```text id="n38ge1"
4
2
```

Meaning:

- no greater future element exists

Their results remain:

```text id="n39ge1"
-1
```

Final:

```python id="n40ge1"
[-1,3,-1]
```

Correct.

---

# Why Time Complexity Is O(n)

Each relevant number:

- pushed once
- popped once

Total operations:

```text id="n41ge1"
O(n)
```

Hash lookups:

```text id="n42ge1"
O(1)
```

Overall:

```text id="n43ge1"
O(nums1 + nums2)
```

which satisfies follow-up requirement.

---

# Space Complexity

Hash map:

```text id="n44ge1"
O(nums1)
```

Stack:

```text id="n45ge1"
O(nums1)
```

Result:

```text id="n46ge1"
O(nums1)
```

Total:

```text id="n47ge1"
O(nums1)
```

---

# Deep Monotonic Stack Insight

The stack stores:

```text id="n48ge1"
elements whose future answer is still unknown
```

Current larger element acts like:

```text id="n49ge1"
new information resolving pending questions
```

That is the unifying mental model for monotonic stacks.

---

# Pattern Extraction

# Trigger

- next greater
- nearest larger to right
- first bigger future element

---

# Pattern

Monotonic Decreasing Stack

---

# Structure

```text id="n50ge1"
stack stores unresolved decreasing values
```

---

# Flow

```text id="n51ge1"
new value arrives
→ resolve smaller unresolved values
→ assign next-greater answers
→ push current unresolved value
```

---

# Most Important Insight

The stack is NOT storing sorted values for lookup.

It is storing:

```text id="n52ge1"
questions waiting for future answers
```

That mental model is the core of monotonic stack reasoning.
