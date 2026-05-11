# Step 1 — Pattern Prediction

This is a very important:

# Pattern B — Monotonic Stack

problem.

But it introduces a major upgrade over Daily Temperatures and Next Greater Element.

This problem teaches:

# State Compression

and

# Aggregated Monotonic Information

This is a critical abstraction leap.

---

# Why This Problem Is Special

In earlier monotonic stack problems:

- stack stored unresolved elements
- future elements resolved them individually

But here:

> we compress historical information together

That is the major new idea.

---

# The Real Problem

The problem is NOT:

```text id="oss1"
count consecutive days
```

The real problem is:

> efficiently collapse consecutive smaller-or-equal history

This is fundamentally:

```text id="oss2"
previous greater element
```

reasoning.

---

# Important Recognition Signal

The phrase:

```text id="oss3"
consecutive previous elements satisfying a condition
```

is a huge monotonic-stack signal.

Especially when:

- nearest larger boundary matters

---

# Brute Force Perspective

Suppose prices:

```text id="oss4"
[100,80,60,70,60,75,85]
```

When processing 85:

You could scan backward:

```text id="oss5"
75 <= 85
60 <= 85
70 <= 85
60 <= 85
80 <= 85
100 > 85 stop
```

Span = 6.

But repeated backward scans become:

```text id="oss6"
O(n²)
```

---

# Core Insight

Suppose current price = 85.

Once you know:

```text id="oss7"
75 already represents span 4
```

you do NOT need to:

- revisit all 4 days individually

You can absorb them instantly.

That is the heart of the optimization.

---

# Mental Model

Each stack entry represents:

```text id="oss8"
a compressed block of dominance
```

NOT:

- a single unresolved question

This is the key conceptual leap.

---

# Why Your Stack Is Brilliant

You store:

```python id="oss9"
[price, span]
```

This is extremely important.

The stack is no longer storing just:

- values
- indices

It stores:

```text id="oss10"
aggregated historical information
```

That is advanced monotonic-stack reasoning.

---

# Step 2 — Understanding the Span

Span means:

```text id="oss11"
how far backward can current price dominate?
```

Specifically:

```text id="oss12"
count consecutive previous prices <= current price
```

Until:

- larger previous price blocks expansion

---

# Key Boundary Insight

A larger previous price acts like:

```text id="oss13"
a stopping wall
```

Everything smaller/equal gets absorbed into current span.

---

# Why Monotonic Stack Works

The stack maintains:

# strictly decreasing prices

Example:

```text id="oss14"
[
 [100,1],
 [80,1],
 [75,4]
]
```

Notice:

```text id="oss15"
100 > 80 > 75
```

This is a monotonic decreasing stack.

---

# Why Decreasing?

Because:

- smaller/equal prices get absorbed immediately

So unresolved dominant boundaries remaining on stack must decrease.

---

# Step 3 — High-Level Algorithm

When new price arrives:

---

# Initial Span

```text id="oss16"
span = 1
```

Every day counts itself.

---

# While Previous Prices <= Current

Current price dominates them.

So:

- absorb their spans
- pop them

---

# Why Add Stored Spans?

Critical insight:

Each popped entry already compressed:

- multiple days

So instead of recounting:

- we reuse aggregated information

That creates O(n).

---

# Step 4 — Code Reconstruction

---

# Constructor

```python id="oss17"
def __init__(self):
    self.stack: list[list[int]] = []
```

---

# What Stack Stores

Each entry:

```python id="oss18"
[price, span]
```

Example:

```python id="oss19"
[
 [100,1],
 [80,1],
 [75,4]
]
```

means:

- 75 dominates previous 4 consecutive days

---

# Why Store Span?

This is the critical optimization.

Without stored spans:

- backward rescanning required

With spans:

- history gets compressed

---

# Start New Query

```python id="oss20"
new_span = 1
```

---

# Why Start With 1?

Current day always contributes:

- itself

Even if:

- no previous prices absorbed

---

# Fast Path

```python id="oss21"
if not self.stack or price < self.stack[-1][0]:
```

---

# Meaning

If current price is smaller:

- cannot absorb previous days

So span remains:

```text id="oss22"
1
```

---

# Example

Stack top:

```text id="oss23"
80
```

Current:

```text id="oss24"
60
```

60 cannot dominate 80.

Stop immediately.

---

# Push New Independent Block

```python id="oss25"
self.stack.append([price, 1])
```

---

# Meaning

Current price starts:

- its own isolated dominance block

---

# Core While Loop

```python id="oss26"
while self.stack and self.stack[-1][0] <= price:
```

This is the heart of the algorithm.

---

# Meaning

As long as previous prices are:

- smaller
  OR
- equal

current price dominates them.

So:

- absorb them

---

# Critical Line

```python id="oss27"
new_span += self.stack[-1][1]
```

This is the most important line in the entire problem.

---

# Why Add Entire Span?

Suppose stack top:

```python id="oss28"
[75,4]
```

This means:

```text id="oss29"
75 already dominates previous 4 days
```

If current price = 85:

Then 85 dominates:

- 75
  AND
- all 4 days behind it

So we can absorb entire block instantly.

---

# This Is State Compression

Instead of storing:

```text id="oss30"
individual historical days
```

we store:

```text id="oss31"
compressed dominance regions
```

This is advanced monotonic-stack optimization.

---

# Pop Absorbed Block

```python id="oss32"
self.stack.pop()
```

---

# Why Pop?

Those smaller prices:

- are permanently dominated now

They can never affect future spans again.

---

# Push Compressed Result

```python id="oss33"
self.stack.append([price, new_span])
```

---

# Meaning

Current price now represents:

- a new compressed dominance region

---

# Return Span

```python id="oss34"
return new_span
```

---

# Step 5 — Visual Execution

Let’s trace:

```text id="oss35"
[100,80,60,70,60,75,85]
```

---

# Day 1 → 100

Start:

```text id="oss36"
span = 1
```

Push:

```python id="oss37"
[[100,1]]
```

Return:

```text id="oss38"
1
```

---

# Day 2 → 80

80 < 100

Cannot absorb.

Push:

```python id="oss39"
[[100,1],[80,1]]
```

Return:

```text id="oss40"
1
```

---

# Day 3 → 60

Push:

```python id="oss41"
[[100,1],[80,1],[60,1]]
```

Return:

```text id="oss42"
1
```

---

# Day 4 → 70

70 absorbs 60.

Pop:

```python id="oss43"
[60,1]
```

New span:

```text id="oss44"
1 + 1 = 2
```

Push:

```python id="oss45"
[[100,1],[80,1],[70,2]]
```

Return:

```text id="oss46"
2
```

---

# Day 5 → 60

Push:

```python id="oss47"
[[100,1],[80,1],[70,2],[60,1]]
```

Return:

```text id="oss48"
1
```

---

# Day 6 → 75

Absorbs:

- 60(span1)
- 70(span2)

New span:

```text id="oss49"
1 + 1 + 2 = 4
```

Push:

```python id="oss50"
[[100,1],[80,1],[75,4]]
```

Return:

```text id="oss51"
4
```

---

# Day 7 → 85

Absorbs:

- 75(span4)
- 80(span1)

Total:

```text id="oss52"
1 + 4 + 1 = 6
```

Push:

```python id="oss53"
[[100,1],[85,6]]
```

Return:

```text id="oss54"
6
```

Correct.

---

# Why Time Complexity Is O(n)

Even though while-loop exists:

Each entry:

- pushed once
- popped once

Maximum operations:

```text id="oss55"
2n
```

So total:

```text id="oss56"
O(n)
```

---

# Space Complexity

Worst case decreasing prices:

```text id="oss57"
[100,90,80,70]
```

Nothing absorbed.

Entire stack stored.

```text id="oss58"
O(n)
```

---

# Deep Conceptual Leap

This problem teaches something VERY important:

Earlier monotonic stacks stored:

```text id="oss59"
unresolved elements
```

This problem stores:

```text id="oss60"
compressed historical regions
```

That is a much more advanced abstraction.

---

# Pattern Extraction

# Trigger

- consecutive dominance
- previous greater boundary
- backward expansion

---

# Pattern

Monotonic Decreasing Stack with Aggregation

---

# Structure

```text id="oss61"
stack stores [price, compressed_span]
```

---

# Flow

```text id="oss62"
new price arrives
→ absorb dominated regions
→ merge spans
→ create larger compressed region
```

---

# Most Important Insight

The stack is NOT storing individual days anymore.

It is storing:

```text id="oss63"
compressed dominance history
```

That transition from:

- raw elements
  → aggregated structure

is a major milestone in monotonic stack mastery.
