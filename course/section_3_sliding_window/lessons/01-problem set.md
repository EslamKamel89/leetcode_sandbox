Good. This is the right move.

If we get this list right, the rest of the section becomes **mechanical execution**, not guesswork.

We are going to build this like a **curriculum**, not a random list.

---

# 🟢 Goal: SSOT for Section 3 (Sliding Window)

This list must satisfy:

- Covers **all core variations**
- Avoids redundancy
- Builds difficulty progressively
- Maximizes **pattern clarity per problem**

---

# 🧠 First — What MUST be Covered

From Phase 0, sliding window has **distinct sub-patterns**:

---

## 🟩 Category A — Fixed Window

- Constant size
- Rolling update

---

## 🟨 Category B — Variable Window (Core)

This splits into **constraint types**:

---

### 1. Duplicate / Uniqueness Constraint

- “no repeating characters”

---

### 2. Frequency / Replacement Constraint

- “you can replace up to k”

---

### 3. Distinct Count Constraint

- “at most k distinct”

---

### 4. Sum Constraint

- “sum ≥ target” or “≤ target”

---

### 5. Exact Match / Covering Constraint (Hardest)

- “window must contain all required chars”

---

### 6. Advanced Window Structure

- monotonic queue / max in window

---

👉 If your list doesn’t cover ALL of these → it’s incomplete

---

# 🟢 AUTHORITATIVE LIST (SSOT)

This is your **final, locked list**.

---

# 🟩 Phase 1 — Fixed Window (Foundation)

---

### 1. Maximum Average Subarray I

👉 Why:

- Pure fixed window
- Teaches rolling sum

---

### 2. Permutation in String

👉 Why:

- Fixed window + frequency matching
- Bridge to variable window

---

---

# 🟨 Phase 2 — Core Variable Window (Entry)

---

### 3. Longest Substring Without Repeating Characters

👉 Teaches:

- expand + shrink
- duplicate handling
- **first real sliding window**

---

---

# 🟨 Phase 3 — Constraint Variations (CRITICAL)

---

### 4. Longest Repeating Character Replacement

👉 Teaches:

- “window can be invalid within budget”
- most misunderstood concept

---

---

### 5. Fruit Into Baskets

👉 Teaches:

- at most k distinct
- hashmap control

---

---

### 6. Longest Substring with At Most K Distinct Characters

👉 Teaches:

- generalization of previous problem

---

---

### 7. Minimum Size Subarray Sum

👉 Teaches:

- sum-based shrinking
- different trigger direction

---

---

# 🟥 Phase 4 — Advanced Window Logic

---

### 8. Minimum Window Substring

👉 Teaches:

- exact requirement matching
- most complex validity logic

---

---

### 9. Sliding Window Maximum

👉 Teaches:

- monotonic queue
- structural upgrade of window

---

---

# 🟣 Optional (Only if Needed)

Add ONLY if you feel gaps:

---

### 10. Find All Anagrams in a String

👉 Reinforces:

- frequency + fixed/variable hybrid

---

---

# 🔵 Why This List is Optimal

---

## ❌ What we removed

- All DP, graph, backtracking noise
- Redundant problems
- Pattern-ambiguous questions

---

## ✅ What we ensured

Each problem teaches **something new**:

| Problem               | New Concept       |
| --------------------- | ----------------- |
| Max Avg Subarray      | fixed window      |
| Permutation in String | freq + fixed      |
| Longest Substring     | base variable     |
| Character Replacement | budget constraint |
| Fruit Into Baskets    | distinct tracking |
| K Distinct            | generalization    |
| Min Subarray Sum      | sum constraint    |
| Min Window Substring  | exact matching    |
| Sliding Window Max    | monotonic queue   |

---

---

# 🧠 How You Should Treat This List

This is NOT:

> “problems to solve once”

This is:

> **training dataset for a pattern**

---

For each problem:

- extract pattern
- generalize it
- reuse mental model

---

---

# 🔒 Final Decision

This list is now your:

> ✅ **Single Source of Truth (SSOT) for Section 3**

Do NOT add random problems.

If something is missing → we refine, not expand blindly.

---

---

# 🔜 Next Step

We start the loop with:

👉 **Maximum Average Subarray I**

You go first:

### Step 1 — Pattern Prediction

- What pattern is this?
- Why?
- What structure will you use?

Don’t write code yet.
