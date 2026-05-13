# Step 1 — Pattern Prediction

This is one of the BEST:

# Pattern C — Stack Simulation

problems.

It is a major milestone because it teaches:

# Chain-Reaction Simulation

and

# Repeated State Resolution

This is a deeper simulation pattern than:

- Baseball Game
- Simplify Path

because:

- one incoming element may trigger multiple interactions

That makes the while-loop reasoning extremely important.

---

# The Real Problem

The problem is NOT:

```text id="ac1"
compare asteroid sizes
```

The real problem is:

> simulate sequential collisions while preserving unresolved survivors

This is fundamentally:

```text id="ac2"
dynamic interaction history
```

---

# Core Physical Insight

Two asteroids collide ONLY when:

```text id="ac3"
left asteroid moves right
AND
right asteroid moves left
```

Meaning:

```text id="ac4"
positive ... negative
```

Example:

```text id="ac5"
[5, -3]
```

Collision possible.

---

# Why Same-Direction Asteroids Never Collide

Example:

```text id="ac6"
[5,10]
```

Both moving right.

Distance between them:

- never decreases

So:

- impossible to meet

---

# Why Opposite Order Also Never Collides

Example:

```text id="ac7"
[-5,10]
```

They move away from each other.

Again:

- no collision

---

# Critical Recognition Signal

Collision occurs ONLY when:

```text id="ac8"
stack[-1] > 0 and current < 0
```

This is the key condition in the entire problem.

---

# Mental Model

The stack represents:

```text id="ac9"
surviving unresolved asteroid state
```

Each new asteroid asks:

```text id="ac10"
"Can I destroy previous survivors?"
```

This creates:

- chain reactions
- repeated interactions

---

# Why Stack Fits Perfectly

When a new asteroid arrives:

- it only interacts with the most recent surviving asteroid first

That is pure stack behavior.

Example:

```text id="ac11"
[3,5,-6]
```

`-6` hits:

- 5 first
- then 3

Newest survivor interacts first.

LIFO.

---

# Step 2 — High-Level Strategy

Process asteroids left → right.

The stack stores:

- surviving asteroids

---

# For Each New Asteroid

If no collision possible:

- push directly

Otherwise:

- repeatedly resolve collisions

---

# Collision Outcomes

Suppose:

```text id="ac12"
top = 5
current = -3
```

Sizes:

- 5 > 3

Result:

- current explodes

---

# Suppose

```text id="ac13"
top = 3
current = -5
```

Sizes:

- 5 > 3

Result:

- top explodes
- current continues moving

This continuation is VERY important.

---

# Suppose Equal

```text id="ac14"
5 and -5
```

Both explode.

---

# Step 3 — Understanding Your Collision Trick

You used:

```python id="ac15"
diff = stack[-1] + a
```

This is clever.

Let’s analyze carefully.

---

# Example 1

```text id="ac16"
top = 10
a = -5
```

Then:

```python id="ac17"
diff = 10 + (-5) = 5
```

Positive result:

- top survives

---

# Example 2

```text id="ac18"
top = 5
a = -10
```

Then:

```python id="ac19"
diff = 5 + (-10) = -5
```

Negative:

- incoming asteroid survives

---

# Example 3

```text id="ac20"
5 + (-5) = 0
```

Equal sizes:

- both destroyed

---

# Why This Works

Because:

- signs already encode directions

and:

- magnitudes encode sizes

So addition effectively compares absolute sizes.

Nice compact trick.

---

# Step 4 — Code Reconstruction

---

# Stack Initialization

```python id="ac21"
stack = []
```

---

# What Stack Stores

Current surviving asteroid state.

Example:

```python id="ac22"
[5,10]
```

means:

- these asteroids survived all previous interactions

---

# Main Loop

```python id="ac23"
for a in asteroids:
```

Sequential simulation.

Order matters completely.

---

# Collision While Loop

```python id="ac24"
while stack and stack[-1] > 0 and a < 0:
```

This is the heart of the problem.

---

# Condition 1 — `stack`

Need previous survivor to collide with.

---

# Condition 2 — `stack[-1] > 0`

Previous asteroid moving right.

---

# Condition 3 — `a < 0`

Current asteroid moving left.

---

# Combined Meaning

```text id="ac25"
right-moving survivor meets left-moving incoming asteroid
```

Collision guaranteed.

---

# Why While Instead of If?

This is EXTREMELY important.

One asteroid may survive multiple collisions.

Example:

```text id="ac26"
[3,5,-10]
```

`-10` destroys:

- 5
- then 3

That requires repeated interactions.

Thus:

- while loop

---

# Case 1 — Incoming Asteroid Wins

```python id="ac27"
if diff < 0:
    stack.pop()
```

---

# Meaning

Incoming asteroid larger.

Previous survivor destroyed.

But incoming asteroid still alive.

So:

- continue collision loop

This continuation is critical.

---

# Example

```text id="ac28"
stack = [3,5]
a = -10
```

First:

- destroys 5

Then:

- still collides with 3

---

# Case 2 — Stack Asteroid Wins

```python id="ac29"
elif diff > 0:
    a = 0
```

---

# Meaning

Incoming asteroid destroyed.

Setting:

```python id="ac30"
a = 0
```

acts as:

```text id="ac31"
dead marker
```

Now:

- stop future processing
- do not append

---

# Why No Pop?

Top asteroid survives.

Remains on stack.

---

# Case 3 — Equal Sizes

```python id="ac32"
else:
    a = 0
    stack.pop()
```

---

# Meaning

Both explode.

So:

- remove top survivor
- incoming asteroid dies too

---

# Why Both Actions Needed?

Without pop:

- dead asteroid incorrectly survives

Without `a = 0`:

- destroyed incoming asteroid incorrectly appended later

---

# Final Append

```python id="ac33"
if a:
    stack.append(a)
```

---

# Meaning

Only surviving asteroids enter final state.

Destroyed asteroids:

- marked with `a = 0`
- skipped

---

# Step 5 — Visual Execution

Let’s trace:

```text id="ac34"
[10,2,-5]
```

---

# Read 10

Push:

```python id="ac35"
[10]
```

---

# Read 2

No collision.

Push:

```python id="ac36"
[10,2]
```

---

# Read -5

Collision possible:

- 2 vs -5

Compute:

```python id="ac37"
2 + (-5) = -3
```

Negative:

- 2 destroyed

Pop:

```python id="ac38"
[10]
```

---

# Continue While

Now:

- 10 vs -5

Compute:

```python id="ac39"
10 + (-5) = 5
```

Positive:

- -5 destroyed

Set:

```python id="ac40"
a = 0
```

Stop.

---

# Final State

```python id="ac41"
[10]
```

Correct.

---

# Harder Example

```text id="ac42"
[3,5,-6]
```

---

# Push 3

```python id="ac43"
[3]
```

---

# Push 5

```python id="ac44"
[3,5]
```

---

# Read -6

Collision:

- 5 destroyed

Stack:

```python id="ac45"
[3]
```

Continue:

- 3 destroyed

Stack:

```python id="ac46"
[]
```

No more collisions.

Push -6:

```python id="ac47"
[-6]
```

Correct.

---

# Time Complexity

Each asteroid:

- pushed once
- popped at most once

Total:

```text id="ac48"
O(n)
```

---

# Space Complexity

Worst case:

- no collisions

```text id="ac49"
O(n)
```

---

# Deep Conceptual Insight

Previous stack problems stored:

- unresolved matches
- unresolved future questions
- compressed regions
- greedy constructions

This problem stores:

```text id="ac50"
surviving dynamic state after repeated interactions
```

That is a very important simulation abstraction.

---

# Pattern Extraction

# Trigger

- chain reactions
- repeated collisions/interactions
- newest survivor interacts first

---

# Pattern

Stack Simulation with Repeated Resolution

---

# Structure

```text id="ac51"
stack stores surviving active state
```

---

# Flow

```text id="ac52"
new asteroid arrives
→ collide with latest survivor
→ destroy one/both
→ possibly continue collisions
→ append if survives
```

---

# Most Important Insight

The stack is NOT storing unresolved future answers.

It is storing:

```text id="ac53"
the currently surviving world state
```

And each new asteroid dynamically modifies that state through repeated interactions.
