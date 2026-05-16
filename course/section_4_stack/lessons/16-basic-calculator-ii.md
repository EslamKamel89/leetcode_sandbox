# Step 1 — Pattern Prediction

This is one of the most important:

# Pattern D — Expression / Recursive Evaluation

problems.

But unlike Reverse Polish Notation, this problem introduces:

# Operator Precedence Handling

This is a huge conceptual upgrade.

---

# Why This Problem Matters

RPN was easy because:

```text id="bc21"
evaluation order was explicit
```

No ambiguity existed.

But now we return to:

# infix notation

Example:

```text id="bc22"
3 + 2 * 2
```

Now evaluation order matters.

---

# The Real Problem

The problem is NOT:

```text id="bc23"
parse operators
```

The real challenge is:

> correctly delay low-priority operations while immediately resolving high-priority ones

That is the entire algorithmic idea.

---

# Core Mathematical Insight

Operators have different priorities.

---

# Low Priority

```text id="bc24"
+
-
```

can wait.

---

# High Priority

```text id="bc25"
*
/
```

must happen immediately before surrounding additions/subtractions.

---

# Why Immediate Multiplication Matters

Example:

```text id="bc26"
3 + 2 * 2
```

Correct evaluation:

```text id="bc27"
3 + (2*2)
= 7
```

NOT:

```text id="bc28"
(3+2)*2
= 10
```

So multiplication must collapse early.

---

# The Core Trick of This Solution

This is the key insight:

> The stack stores additive terms only.

This is EXTREMELY important.

---

# What Does That Mean?

Instead of evaluating everything immediately:

```text id="bc29"
addition/subtraction gets deferred
```

while:

```text id="bc30"
multiplication/division gets resolved instantly
```

That elegantly handles precedence.

---

# Mental Model

Think of the stack as:

```text id="bc31"
pieces waiting to be summed later
```

Example:

```text id="bc32"
3 + 2 * 2
```

becomes:

```text id="bc33"
3 + 4
```

Stack stores:

```python id="bc34"
[3,4]
```

Then:

- final sum resolves low-precedence operations.

---

# Why This Is Brilliant

Because:

- multiplication/division already collapsed
- remaining operations are only additions/subtractions

So:

```text id="bc35"
sum(stack)
```

becomes valid final evaluation.

---

# Step 2 — High-Level Strategy

Process expression left → right.

---

# Build Numbers Digit-by-Digit

Need support for:

```text id="bc36"
123
4567
```

not just single digits.

---

# When Operator Appears

We now know:

- previous number fully completed

So evaluate using:

- PREVIOUS operator

This is VERY important.

---

# Why Previous Operator?

Suppose:

```text id="bc37"
3+2
```

When reading `+`:

- current number = 3
- operator BEFORE 3 determines how 3 enters expression

That subtle idea is critical.

---

# Operator Rules

---

# '+'

Push positive number.

---

# '-'

Push negative number.

---

# '\*'

Immediately multiply with previous stack term.

---

# '/'

Immediately divide previous stack term.

---

# Final Step

All multiplication/division already resolved.

So:

```text id="bc38"
sum(stack)
```

gives final answer.

---

# Step 3 — Code Reconstruction

---

# Empty Check

```python id="bc39"
if not s:
    return 0
```

Defensive guard.

Not strictly necessary given constraints.

---

# Cleanup

```python id="bc40"
s = s.strip()
s = s.replace(' ', '') + '+'
```

---

# Why Remove Spaces?

Spaces:

- irrelevant syntactic noise

Simplifies parsing logic.

---

# IMPORTANT SENTINEL TRICK

```python id="bc41"
+ '+'
```

This is VERY clever.

---

# Why Add Extra Operator?

Normally:

```text id="bc42"
last number never gets processed
```

because processing occurs when:

- operator encountered

Example:

```text id="bc43"
3+2
```

Without extra operator:

- final `2` never triggers evaluation.

Appending dummy `+` forces:

- final flush.

This is a classic parser trick.

---

# Initialization

```python id="bc44"
stack, current_num, operator = [], 0, "+"
```

---

# What Each Variable Means

---

# stack

Stores:

- additive terms

---

# current_num

Number currently being built.

---

# operator

Operation to apply to current_num.

Important:

- applies AFTER number finishes parsing.

---

# Operator Set

```python id="bc45"
all_operators = {"+", "-", "*", "/"}
```

Unused variable.

Can safely remove.

---

# Main Loop

```python id="bc46"
for i, token in enumerate(s):
```

Sequential parsing.

---

# Digit Parsing

```python id="bc47"
if token.isdigit():
    current_num = current_num * 10 + int(token)
```

---

# Why Multiply By 10?

Suppose reading:

```text id="bc48"
123
```

Process:

- 1
- 12
- 123

Formula:

```text id="bc49"
old_digits_shift_left
```

Example:

```python id="bc50"
12 * 10 + 3 = 123
```

---

# This Is Core Number Parsing Logic

Extremely important parser concept.

---

# Operator Encountered

```python id="bc51"
else:
```

Meaning:

- current number fully parsed

Now apply PREVIOUS operator.

---

# Addition

```python id="bc52"
if operator == "+":
    stack.append(current_num)
```

---

# Meaning

Positive additive term.

Deferred until final sum.

---

# Subtraction

```python id="bc53"
elif operator == "-":
    stack.append(-current_num)
```

---

# Why Negative Push?

Very elegant trick.

Instead of storing:

- subtraction operation

store:

- signed additive term

Then:

```text id="bc54"
sum(stack)
```

handles subtraction naturally.

---

# Multiplication

```python id="bc55"
elif operator == "*":
    stack.append(stack.pop() * current_num)
```

---

# Why Immediate Evaluation?

Multiplication has:

- higher precedence

So it must collapse NOW before future additions.

---

# Important Insight

Top of stack contains:

- previous additive term

We replace it with:

```text id="bc56"
(previous term * current_num)
```

---

# Example

```text id="bc57"
3 + 2 * 2
```

Before multiplication:

```python id="bc58"
[3,2]
```

Current num:

```text id="bc59"
2
```

Collapse:

```python id="bc60"
[3,4]
```

Perfect precedence handling.

---

# Division

```python id="bc61"
elif operator == "/":
    stack.append(int(stack.pop()/current_num))
```

---

# Why `int(a/b)` Works Here

Python:

```python id="bc62"
int(-3/2)
```

gives:

```text id="bc63"
-1
```

which truncates toward zero.

Correct for problem requirements.

---

# Reset Number

```python id="bc64"
current_num = 0
```

---

# Why Needed?

Finished processing previous number.

Must start fresh for next number.

---

# Update Operator

```python id="bc65"
operator = token
```

---

# Why AFTER Processing?

Current operator applies to:

- NEXT number

Very important parser sequencing detail.

---

# Final Result

```python id="bc66"
return sum(stack)
```

---

# Why This Works

All:

- multiplication
- division

already collapsed.

Remaining stack contains only:

```text id="bc67"
signed additive terms
```

So summation completes evaluation.

---

# Step 4 — Visual Execution

Let’s trace:

```text id="bc68"
3+2*2
```

After preprocessing:

```text id="bc69"
3+2*2+
```

---

# Start

```python id="bc70"
stack = []
current_num = 0
operator = '+'
```

---

# Read 3

```python id="bc71"
current_num = 3
```

---

# Read +

Apply previous operator:

```text id="bc72"
+
```

Push:

```python id="bc73"
[3]
```

Set:

```text id="bc74"
operator = '+'
```

Reset:

```text id="bc75"
current_num = 0
```

---

# Read 2

```python id="bc76"
current_num = 2
```

---

# Read \*

Apply previous operator:

```text id="bc77"
+
```

Push:

```python id="bc78"
[3,2]
```

Set:

```text id="bc79"
operator='*'
```

---

# Read 2

```python id="bc80"
current_num=2
```

---

# Read Sentinel +

Apply previous operator:

```text id="bc81"
*
```

Collapse:

```python id="bc82"
[3,4]
```

Final sum:

```text id="bc83"
7
```

Correct.

---

# Harder Example

```text id="bc84"
14-3/2
```

---

# After Parsing

Stack evolution:

```python id="bc85"
[14]
[14,-1]
```

because:

```text id="bc86"
3/2 = 1
```

Final:

```text id="bc87"
14 + (-1) = 13
```

Correct.

---

# Time Complexity

Each character processed once.

Stack operations:

- O(1)

Total:

```text id="bc88"
O(n)
```

---

# Space Complexity

Worst case:

```text id="bc89"
1+2+3+4+5...
```

Every term stored.

```text id="bc90"
O(n)
```

---

# Deep Conceptual Insight

Reverse Polish Notation stored:

```text id="bc91"
partially reduced postfix computations
```

This problem stores:

```text id="bc92"
partially evaluated infix expression terms with precedence already resolved
```

This is a significant parser/evaluator abstraction upgrade.

---

# Pattern Extraction

# Trigger

- infix expression parsing
- operator precedence
- delayed low-precedence evaluation

---

# Pattern

Stack-Based Precedence Evaluation

---

# Structure

```text id="bc93"
stack stores additive terms
high-precedence ops collapse immediately
```

---

# Flow

```text id="bc94"
build number
→ encounter operator
→ apply PREVIOUS operator
→ immediately resolve * and /
→ defer + and -
→ sum remaining terms
```

---

# Most Important Insight

The stack is NOT storing:

- unresolved future values
- nested contexts
- raw operands

It is storing:

```text id="bc95"
partially evaluated expression terms
```

where:

- multiplication/division already resolved
- addition/subtraction deferred for final aggregation

That is the key parser/evaluator mental model.
