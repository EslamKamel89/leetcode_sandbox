# Step 1 — Pattern Prediction

This problem is still:

# Pattern A — Basic Stack

But it introduces an important evolution:

> Stack Augmentation

This is the first time the stack becomes more than:

- push/pop storage

Now the stack also maintains:

```text id="npx8xu"
derived state
```

specifically:

```text id="v8ztxf"
the minimum element so far
```

This is a major conceptual upgrade.

---

# The Real Problem

At first glance, the problem looks trivial:

```text id="wy9whg"
just keep a stack
```

But the constraint changes everything:

```text id="bzkjlwm"
getMin() must be O(1)
```

That requirement is the core challenge.

---

# Why a Normal Stack Fails

Suppose:

```text id="jlwm25"
stack = [5, 2, 8, 1]
```

If we ask:

```text id="jlwm26"
getMin()
```

A normal stack would need:

```text id="jlwm27"
scan entire stack
```

to find minimum.

That costs:

```text id="jlwm28"
O(n)
```

which violates the requirement.

---

# Key Insight

The minimum changes over time.

When new elements arrive:

- minimum may change
- old minimum may remain

So we need a structure that tracks:

```text id="jlwm29"
minimum state at every stack depth
```

That is the core insight.

---

# Mental Model

Think of each stack level carrying metadata.

Not just:

```text id="jlwm30"
"value"
```

but also:

```text id="jlwm31"
"minimum up to this point"
```

Example:

| Stack Depth | Value | Minimum So Far |
| ----------- | ----- | -------------- |
| 0           | 5     | 5              |
| 1           | 2     | 2              |
| 2           | 8     | 2              |
| 3           | 1     | 1              |

Now:

```text id="jlwm32"
top minimum = current global minimum
```

Always accessible in O(1).

---

# Why Two Stacks Work

Your solution uses:

```python id="jlwm33"
self._stack
self._min_stack
```

This is the classic optimal design.

---

# Role of Each Stack

---

# Main Stack

```python id="jlwm34"
self._stack
```

Stores:

- actual values

Normal stack behavior.

---

# Min Stack

```python id="jlwm35"
self._min_stack
```

Stores:

- minimum value at corresponding depth

This is the important abstraction.

---

# Critical Invariant

This MUST always remain true:

```text id="jlwm36"
len(_stack) == len(_min_stack)
```

And:

```text id="jlwm37"
_min_stack[i]
=
minimum of _stack[0:i+1]
```

That invariant is the entire algorithm.

---

# Step 2 — High-Level Strategy

For every pushed element:

- also push current minimum

So each stack level remembers:

```text id="jlwm38"
"What was the minimum when I was added?"
```

Then when popping:

- minimum state naturally rolls back

This is beautiful because:

> stack history automatically restores previous minimum state

No recomputation needed.

---

# Step 3 — Code Reconstruction

---

# Constructor

```python id="jlwm39"
def __init__(self):
    self._stack: list[int] = []
    self._min_stack: list[int] = []
```

---

# What This Creates

Two synchronized stacks.

Example state:

| Main Stack | Min Stack |
| ---------- | --------- |
| [5,2,8]    | [5,2,2]   |

---

# Why Separate Structures?

Because:

- one stores values
- one stores historical minimum information

This separation keeps operations O(1).

---

# Push Operation

```python id="jlwm40"
def push(self, val: int) -> None:
```

This is the heart of the solution.

---

# Step 1 — Push Into Main Stack

```python id="jlwm41"
self._stack.append(val)
```

Normal stack insertion.

---

# Why Needed

Without this:

- stack functionality disappears

Min tracking alone is not enough.

---

# Step 2 — Empty Min Stack Case

```python id="jlwm42"
if not self._min_stack:
    self._min_stack.append(val)
```

---

# Why This Exists

First inserted value automatically becomes minimum.

Example:

```text id="jlwm43"
push(5)
```

No previous elements exist.

So:

```text id="jlwm44"
minimum = 5
```

---

# What Breaks Without This?

We would attempt:

```python id="jlwm45"
self._min_stack[-1]
```

on empty stack → crash.

---

# Step 3 — New Minimum Appears

```python id="jlwm46"
elif self._min_stack[-1] >= val:
    self._min_stack.append(val)
```

---

# Meaning

If new value is smaller (or equal):

```text id="jlwm47"
minimum changes
```

So store new minimum.

---

# Why `>=` Instead of `>`?

This is VERY important.

Suppose:

```text id="jlwm48"
push(2)
push(2)
```

If only `>` used:

- duplicate minimum not tracked properly

Then popping one `2` would incorrectly lose minimum state.

Using `>=` preserves correct history.

---

# Example

Push sequence:

```text id="jlwm49"
5
2
2
```

Min stack becomes:

```text id="jlwm50"
5
2
2
```

Now pop once:

```text id="jlwm51"
minimum still 2
```

Correct.

---

# Step 4 — Minimum Unchanged

```python id="jlwm52"
else:
    self._min_stack.append(self._min_stack[-1])
```

---

# This Is the Key Design Choice

Instead of storing:

- only new minima

You store:

```text id="jlwm53"
minimum snapshot at every depth
```

Example:

Push:

```text id="jlwm54"
5
2
8
```

Min stack:

```text id="jlwm55"
5
2
2
```

The `8` layer remembers:

- current minimum was still `2`

---

# Why This Is Brilliant

Now:

```python id="jlwm56"
getMin()
```

becomes trivial:

```python id="jlwm57"
return self._min_stack[-1]
```

No searching.
No recomputation.

Pure O(1).

---

# Pop Operation

```python id="jlwm58"
def pop(self) -> None:
    self._stack.pop()
    self._min_stack.pop()
```

---

# Why Both Pops Matter

The stacks represent synchronized history.

If one pops without the other:

- state becomes misaligned

Then:

- minima correspond to wrong elements

---

# Mental Model

Popping means:

```text id="jlwm59"
rewind stack state
```

That includes:

- value state
- minimum state

---

# Top Operation

```python id="jlwm60"
def top(self) -> int:
    return self._stack[-1]
```

Standard stack top access.

---

# Why O(1)?

Python list tail access:

```python id="jlwm61"
[-1]
```

is constant time.

---

# getMin Operation

```python id="jlwm62"
def getMin(self) -> int:
    return self._min_stack[-1]
```

---

# This Is the Entire Goal

Because min stack always stores:

```text id="jlwm63"
current minimum at current depth
```

Top of min stack IS the answer.

No computation needed.

---

# Step 4 — Visual Execution

Let’s trace:

```text id="jlwm64"
push(-2)
push(0)
push(-3)
```

---

# Initial State

| Stack | Min Stack |
| ----- | --------- |
| []    | []        |

---

# push(-2)

Main stack:

```text id="jlwm65"
[-2]
```

Min stack empty:

- push -2

| Stack | Min Stack |
| ----- | --------- |
| [-2]  | [-2]      |

---

# push(0)

Main stack:

```text id="jlwm66"
[-2, 0]
```

Current min:

```text id="jlwm67"
-2
```

0 is larger.

So repeat previous min:

| Stack  | Min Stack |
| ------ | --------- |
| [-2,0] | [-2,-2]   |

---

# push(-3)

Main stack:

```text id="jlwm68"
[-2,0,-3]
```

New minimum appears.

| Stack     | Min Stack  |
| --------- | ---------- |
| [-2,0,-3] | [-2,-2,-3] |

---

# getMin()

Top of min stack:

```text id="jlwm69"
-3
```

Correct.

---

# pop()

Pop both stacks.

| Stack  | Min Stack |
| ------ | --------- |
| [-2,0] | [-2,-2]   |

---

# getMin()

Top min:

```text id="jlwm70"
-2
```

Automatically restored.

That is the beauty of this design.

---

# Time Complexity

Every operation:

- push
- pop
- top
- getMin

is:

```text id="jlwm71"
O(1)
```

---

# Space Complexity

Two stacks storing same depth:

```text id="jlwm72"
O(n)
```

---

# Most Important Conceptual Leap

This problem teaches:

> stacks can store historical state snapshots

NOT just values.

That idea becomes foundational later for:

- monotonic stacks
- DFS state
- parser stacks
- undo systems
- DP optimizations

This is a major milestone problem.

---

# Pattern Extraction

# Trigger

Need:

- normal stack operations
- extra information in O(1)

---

# Pattern

Augmented Stack

---

# Structure

```text id="jlwm73"
main stack + metadata stack
```

---

# Flow

```text id="jlwm74"
push value
→ compute new minimum
→ store minimum snapshot

pop
→ rollback both value and minimum state
```

---

# Deep Insight

The min stack is NOT storing all minimum candidates.

It is storing:

```text id="jlwm75"
the minimum state at every moment in stack history
```

That distinction is extremely important.
