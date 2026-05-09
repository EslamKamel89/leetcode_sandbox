# Step 1 — Pattern Prediction

This is the FIRST true:

# Pattern B — Monotonic Stack

problem.

This problem is extremely important because it introduces the core monotonic stack mental model:

> unresolved elements waiting for future resolution

This is one of the most important abstractions in interview problem solving.

---

# Why This Problem Matters So Much

Before this problem, stack usage was mostly:

- matching
- undo
- navigation
- simulation

Now the stack becomes:

```text id="a1r8vk"
a structure for deferred decisions
```

That is a major conceptual shift.

---

# The Real Problem

The problem is NOT:

```text id="b2m7xp"
find warmer temperatures
```

The real problem is:

> efficiently find the NEXT future element satisfying a condition

Specifically:

```text id="c3y9zl"
next greater element
```

This pattern appears everywhere.

---

# Why Brute Force Is Bad

Your first solution:

```python id="d4t1rm"
for i:
    for j:
```

checks future days one-by-one.

That means:

- each day scans potentially all future days

Worst case:

```text id="e5v2xn"
[100,99,98,97,96...]
```

No warmer future exists.

So every element scans almost entire remainder.

Complexity:

```text id="f6m4zk"
O(n²)
```

Too slow for large inputs.

---

# The Core Insight

When processing a new temperature:

```text id="g7r1yp"
this temperature may resolve older unresolved days
```

That is the heart of monotonic stack thinking.

---

# Mental Model

Suppose:

```text id="h8t6vm"
[73,74,75]
```

---

# Day 0 → 73

We don't know future warmer day yet.

So:

```text id="i9y3xr"
73 is unresolved
```

---

# Day 1 → 74

Now we know:

- 74 is warmer than 73

So:

```text id="j1m8zk"
73 becomes resolved
```

Answer for day 0:

```text id="k2v4tp"
1 day
```

---

# Day 2 → 75

Now:

- 75 resolves 74

Again:

- unresolved state gets resolved by future information

That is the monotonic stack abstraction.

---

# Why Stack Works

We only care about:

```text id="l3r9xn"
recent unresolved temperatures
```

Older resolved temperatures are irrelevant.

So the stack stores:

```text id="m4t2vk"
days still waiting for warmer future
```

---

# Step 2 — The Monotonic Property

Your stack is:

```python id="n5y7zp"
stack: list[list[int]] = []
```

containing:

```text id="o6m1xr"
[temp, index]
```

---

# What Makes It Monotonic?

Look at the while condition:

```python id="p7v4tk"
while stack and temp > stack[-1][0]:
```

This means:

> pop all smaller temperatures

As a result:

```text id="q8m9yc"
stack temperatures remain decreasing
```

Example stack:

```text id="r9t2xp"
75
72
69
```

from bottom → top.

That is a:

# monotonic decreasing stack

---

# Why Decreasing?

Because smaller temperatures get resolved immediately when larger temperatures arrive.

So unresolved temperatures remaining on stack must decrease.

---

# Step 3 — High-Level Algorithm

We scan left → right.

For each temperature:

---

# While Current Temp Is Warmer

Resolve previous colder days.

For every popped day:

```text id="s1v7zk"
current_day - old_day
```

gives waiting time.

---

# After Resolving

Current day itself becomes unresolved.

So push it onto stack.

---

# Important Insight

Every temperature goes through lifecycle:

```text id="t2m4yr"
unresolved
→ waits on stack
→ resolved by future warmer temperature
→ removed forever
```

This lifecycle is the essence of monotonic stacks.

---

# Step 4 — Code Reconstruction

---

# Result Initialization

```python id="u3x8vn"
result = [0] * len(temperatures)
```

---

# Why Initialize With 0?

Default meaning:

```text id="v4m2xp"
no warmer future exists
```

Only resolved days get updated.

---

# Stack Initialization

```python id="w5t9zk"
stack: list[list[int]] = []
```

---

# What Stack Stores

Each entry:

```python id="x6r3vm"
[temp, index]
```

Example:

```python id="y7m1tp"
[[75,2],[71,3],[69,4]]
```

means:

- these days are unresolved
- still waiting for warmer future

---

# Why Store Index Too?

Temperature alone is insufficient.

We must compute:

```text id="z8v4yr"
days waited
```

which requires positions.

---

# Main Loop

```python id="a9m7zk"
for i, temp in enumerate(temperatures):
```

---

# Why Sequential Processing Matters

Future temperatures resolve past days.

So:

- time order matters completely

---

# The Core While Loop

```python id="b1x3tp"
while stack and temp > stack[-1][0]:
```

This is the heart of the algorithm.

---

# What This Means

As long as current temperature is warmer than unresolved top temperature:

```text id="c2v8yr"
we can resolve that previous day
```

---

# Why Use While Instead of If?

Because one temperature may resolve MANY previous days.

Example:

```text id="d3m4zk"
[73,71,69,72]
```

When 72 arrives:

- resolves 69
- resolves 71

Possibly multiple pops.

---

# Pop Unresolved Day

```python id="e4x1tp"
stack_temp, stack_i = stack.pop()
```

---

# What Pop Means Conceptually

This day is no longer unresolved.

We finally found its warmer future.

---

# Compute Waiting Time

```python id="f5v7yr"
result[stack_i] = i - stack_i
```

---

# Why This Formula Works

Current day:

```text id="g6m2zk"
i
```

Previous unresolved day:

```text id="h7x9tp"
stack_i
```

Difference:

```text id="i8v3yr"
days waited
```

---

# Example

```text id="j9m1zk"
temps = [73,74]
```

When processing 74:

- current index = 1
- unresolved day = 0

So:

```text id="k1x4tp"
1 - 0 = 1
```

Correct.

---

# Push Current Day

```python id="l2v8yr"
stack.append([temp, i])
```

---

# Why Push?

Current temperature itself has not yet found:

- a warmer future day

So it becomes unresolved.

---

# Important Lifecycle

Every temperature:

```text id="m3m7zk"
enters stack once
leaves stack once
```

This is the key complexity insight.

---

# Step 5 — Visual Execution

Let’s trace:

```text id="n4x1tp"
[73,74,75,71,69,72,76,73]
```

---

# Initial

```python id="o5v8yr"
stack = []
result = [0,0,0,0,0,0,0,0]
```

---

# Day 0 → 73

Push unresolved.

```python id="p6m4zk"
stack = [[73,0]]
```

---

# Day 1 → 74

74 > 73

Resolve 73:

```python id="q7x9tp"
result[0] = 1
```

Stack empty.

Push 74:

```python id="r8v2yr"
[[74,1]]
```

---

# Day 2 → 75

75 > 74

Resolve:

```python id="s9m1zk"
result[1] = 1
```

Push 75:

```python id="t1x4tp"
[[75,2]]
```

---

# Day 3 → 71

71 < 75

Cannot resolve anything.

Push:

```python id="u2v8yr"
[[75,2],[71,3]]
```

Notice:

- decreasing order maintained

---

# Day 4 → 69

Push:

```python id="v3m7zk"
[[75,2],[71,3],[69,4]]
```

Still decreasing.

---

# Day 5 → 72

72 resolves:

- 69
- 71

Pop 69:

```python id="w4x1tp"
result[4] = 1
```

Pop 71:

```python id="x5v9yr"
result[3] = 2
```

75 remains unresolved.

Push 72:

```python id="y6m2zk"
[[75,2],[72,5]]
```

---

# Day 6 → 76

Resolves:

- 72
- 75

```python id="z7x4tp"
result[5] = 1
result[2] = 4
```

Push 76:

```python id="a8v1yr"
[[76,6]]
```

---

# Day 7 → 73

Push:

```python id="b9m7zk"
[[76,6],[73,7]]
```

No future warmer days.

Remain 0.

---

# Final Result

```text id="c1x8tp"
[1,1,4,2,1,1,0,0]
```

Correct.

---

# Why Time Complexity Is O(n)

At first glance:

- nested while loop looks dangerous

But key insight:

Each element:

- pushed once
- popped once

Maximum operations:

```text id="d2v4yr"
2n
```

So:

```text id="e3m9zk"
O(n)
```

This is THE critical monotonic stack complexity insight.

---

# Space Complexity

Worst case decreasing temperatures:

```text id="f4x2tp"
[100,99,98,97]
```

Nothing resolves.

Entire stack stored.

```text id="g5v8yr"
O(n)
```

---

# Pattern Extraction

# Trigger

- next greater element
- future resolution
- nearest larger value

---

# Pattern

Monotonic Decreasing Stack

---

# Structure

```text id="h6m1zk"
stack stores unresolved decreasing temperatures
```

---

# Flow

```text id="i7x4tp"
new temperature arrives
→ resolve smaller unresolved temperatures
→ compute waiting times
→ push current unresolved day
```

---

# Most Important Insight

The stack is NOT storing temperatures for lookup.

It is storing:

```text id="j8v9yr"
problems waiting to be solved by future information
```

That is the foundational mental model for monotonic stacks.
