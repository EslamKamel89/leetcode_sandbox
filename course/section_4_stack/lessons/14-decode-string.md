# Step 1 — Pattern Prediction

This is primarily:

# Pattern D — Expression / Recursive Evaluation

with overlap from:

- Stack Simulation

This is one of the most important stack parsing problems because it introduces:

# Nested Context Resolution

and

# Deferred Expression Expansion

This is a major conceptual leap.

---

# Why This Problem Is Different

Earlier stack problems mostly handled:

- matching
- collisions
- monotonic ordering
- simulation

This problem handles:

```text id="ds1"
nested structure evaluation
```

That is fundamentally parser behavior.

---

# The Real Problem

The problem is NOT:

```text id="ds2"
repeat strings
```

The real problem is:

> evaluate nested encoded expressions in correct order

The nesting is the entire challenge.

---

# Why Nesting Changes Everything

Consider:

```text id="ds3"
3[a2[c]]
```

You CANNOT evaluate:

- outer `3[...]`

until:

- inner `2[c]`
  is fully resolved first.

That means:

```text id="ds4"
inner context must finish before outer context
```

That is naturally:

- stack behavior

---

# Core Stack Insight

The stack stores:

```text id="ds5"
unfinished outer contexts
```

while inner expressions are being processed.

This is the same deep idea behind:

- recursion
- compilers
- expression parsers
- DFS call stacks

---

# Mental Model

Think of:

```text id="ds6"
[
```

as:

```text id="ds7"
"start new nested context"
```

and:

```text id="ds8"
]
```

as:

```text id="ds9"
"resolve current nested context"
```

This is a parser mindset.

---

# Important Conceptual Shift

This problem is NOT about:

- unresolved future values

Instead the stack stores:

```text id="ds10"
partially constructed nested expressions
```

Very important distinction.

---

# Step 2 — High-Level Strategy

We process characters left → right.

---

# Normal Characters

Just push into current construction state.

---

# When We See `]`

This signals:

```text id="ds11"
current nested expression is complete
```

Now:

1. extract inner string
2. extract multiplier
3. expand expression
4. push expanded result back

This creates:

- bottom-up evaluation

---

# Why Bottom-Up Evaluation Works

Nested expressions must resolve:

- innermost first

Example:

```text id="ds12"
3[a2[c]]
```

Evaluation order:

```text id="ds13"
2[c]
→ cc

a + cc
→ acc

3[acc]
→ accaccacc
```

This is naturally stack-driven.

---

# Step 3 — Code Reconstruction

---

# Stack Initialization

```python id="ds14"
stack = []
```

---

# What Stack Stores

Mixed parser state:

- letters
- digits
- brackets
- partially expanded strings

This is essentially:

- parser memory

---

# Main Loop

```python id="ds15"
for char in s:
```

Sequential parsing.

---

# Case 1 — Not Closing Bracket

```python id="ds16"
if char != ']':
    stack.append(char)
```

---

# Why Push Everything?

Until we encounter:

```text id="ds17"
]
```

we do not yet know:

- full expression boundary

So:

- defer evaluation

This deferred-state idea is fundamental.

---

# Case 2 — Closing Bracket

```python id="ds18"
else:
```

This is where evaluation happens.

---

# Step A — Extract Encoded String

```python id="ds19"
temp = []
```

---

# Why Temp Exists

We must reconstruct:

```text id="ds20"
encoded_string
```

inside brackets.

---

# Core Loop

```python id="ds21"
while stack and stack[-1] != '[':
```

---

# Meaning

Pop until matching opening bracket.

This extracts:

- current nested context

---

# Example

Suppose stack contains:

```text id="ds22"
3 [ a 2 [ c
```

At `]`:

- pop `c`
  until `[`

Inner expression becomes:

```text id="ds23"
"c"
```

---

# Important Ordering Issue

```python id="ds24"
popped = stack.pop()
temp.insert(0, popped)
```

---

# Why insert(0)?

Stack pops:

- reverse order

But strings must preserve:

- original left→right order

Example:

Stack top:

```text id="ds25"
a b c
```

Popping gives:

```text id="ds26"
c b a
```

So front insertion reverses again.

---

# IMPORTANT OPTIMIZATION NOTE

`insert(0)` on Python list is:

```text id="ds27"
O(n)
```

Cleaner/faster approach:

```python id="ds28"
temp.append(stack.pop())
```

then:

```python id="ds29"
temp.reverse()
```

Better complexity.

---

# Remove Opening Bracket

```python id="ds30"
stack.pop()
```

---

# Why Needed?

We already consumed:

- this nested context

`[` is parser structure only.
Not output content.

---

# Step B — Extract Multiplier

```python id="ds31"
multiplier = ''
```

---

# Why String?

Multiplier may contain:

- multiple digits

Example:

```text id="ds32"
12[a]
```

Need:

```text id="ds33"
"12"
```

not:

```text id="ds34"
1
```

---

# Digit Extraction Loop

```python id="ds35"
while stack and stack[-1] in '0123456789':
```

---

# Why Loop?

Numbers may have multiple digits.

---

# Important Reverse Construction

```python id="ds36"
multiplier = popped + multiplier
```

---

# Why Build Backward?

Digits pop in reverse order.

Example stack:

```text id="ds37"
1 2
```

Pop order:

```text id="ds38"
2 then 1
```

Need final number:

```text id="ds39"
12
```

So prepend each digit.

---

# Step C — Expand Expression

```python id="ds40"
stack += temp * int(multiplier)
```

This is the core evaluation step.

---

# What Happens Here?

Suppose:

```text id="ds41"
multiplier = 3
temp = ['a','c','c']
```

Then:

```python id="ds42"
temp * 3
```

becomes:

```text id="ds43"
accaccacc
```

---

# Why Push Back Into Stack?

Because expanded result may belong to:

- larger outer expression

Example:

```text id="ds44"
3[a2[c]]
```

Inner result:

```text id="ds45"
cc
```

must continue participating inside:

```text id="ds46"
a cc
```

So evaluated results re-enter parser state.

---

# Final Result

```python id="ds47"
return ''.join(stack)
```

At end:

- stack contains fully decoded expression

---

# Step 4 — Visual Execution

Let’s trace:

```text id="ds48"
3[a2[c]]
```

---

# Read `3`

```python id="ds49"
['3']
```

---

# Read `[`

```python id="ds50"
['3','[']
```

---

# Read `a`

```python id="ds51"
['3','[','a']
```

---

# Read `2`

```python id="ds52"
['3','[','a','2']
```

---

# Read `[`

```python id="ds53"
['3','[','a','2','[']
```

---

# Read `c`

```python id="ds54"
['3','[','a','2','[','c']
```

---

# Read `]`

Extract:

- temp = `c`
- multiplier = 2

Expand:

```text id="ds55"
cc
```

Stack becomes:

```python id="ds56"
['3','[','a','c','c']
```

Notice:

- inner expression resolved

---

# Read Final `]`

Extract:

```text id="ds57"
acc
```

Multiplier:

```text id="ds58"
3
```

Expand:

```text id="ds59"
accaccacc
```

Final stack:

```python id="ds60"
['a','c','c','a','c','c','a','c','c']
```

Join:

```text id="ds61"
accaccacc
```

Correct.

---

# Time Complexity

Each character:

- pushed/popped bounded times

Overall roughly:

```text id="ds62"
O(output size)
```

because expansion dominates.

---

# Space Complexity

Stack + output:

```text id="ds63"
O(output size)
```

---

# Deep Conceptual Insight

Previous stack problems stored:

- unresolved values
- survivors
- greedy constructions
- navigation history

This problem stores:

```text id="ds64"
nested evaluation contexts
```

That is a huge conceptual jump toward:

- compilers
- parsers
- recursion simulation

---

# Pattern Extraction

# Trigger

- nested expressions
- bracketed recursive structure
- delayed evaluation

---

# Pattern

Stack-Based Recursive Evaluation

---

# Structure

```text id="ds65"
stack stores unfinished nested parser state
```

---

# Flow

```text id="ds66"
read characters
→ defer nested contexts
→ on ']'
    resolve innermost expression
→ expand
→ return expanded result to outer context
```

---

# Most Important Insight

The stack is NOT storing:

- ordering
- monotonic structure
- unresolved future answers

It is storing:

```text id="ds67"
partially evaluated recursive contexts
```

That is the foundational parser/evaluator stack abstraction.
