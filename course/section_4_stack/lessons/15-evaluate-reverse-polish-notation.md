# Step 1 — Pattern Prediction

This is a core:

# Pattern D — Expression / Recursive Evaluation

problem.

This is one of the canonical stack parser/evaluator problems.

It teaches:

# Deferred Operator Execution

and

# Expression Reduction

This is foundational for understanding:

- compilers
- interpreters
- expression trees
- recursive evaluation

---

# Why This Problem Is Important

This problem introduces a very deep idea:

> operands arrive before operators

That completely changes evaluation strategy.

---

# What Is Reverse Polish Notation (RPN)?

Normal arithmetic:

```text id="rpn1"
(2 + 1) * 3
```

is:

```text id="rpn2"
infix notation
```

because:

- operator sits BETWEEN operands

---

# Reverse Polish Notation

Same expression becomes:

```text id="rpn3"
2 1 + 3 *
```

Operator comes AFTER operands.

That is:

```text id="rpn4"
postfix notation
```

---

# Why RPN Is Powerful

Normal infix expressions require:

- parentheses
- precedence rules

RPN avoids all of that.

Evaluation order becomes:

- completely unambiguous

---

# Core Insight

When operator appears:

```text id="rpn5"
its operands are immediately before it
```

So stack naturally works because:

- latest computed values sit on top

This is fundamentally:

- reduction-based evaluation

---

# Mental Model

The stack stores:

```text id="rpn6"
partially evaluated expressions
```

NOT:

- unresolved future questions
- parser states
- survivors

This is a new stack abstraction.

---

# Example

Expression:

```text id="rpn7"
2 1 + 3 *
```

Process:

```text id="rpn8"
2
→ push

1
→ push

+
→ combine top two values
→ push result

3
→ push

*
→ combine top two values
→ push result
```

This creates progressive expression reduction.

---

# The Deep Conceptual Idea

Operators collapse:

```text id="rpn9"
multiple stack values
→ into one reduced value
```

That is the core evaluator pattern.

---

# Step 2 — High-Level Strategy

Process tokens left → right.

---

# If Token Is Number

Push onto stack.

Meaning:

- operand waiting for future operator

---

# If Token Is Operator

Pop:

- top two operands

Apply operator.

Push result back.

This creates:

- smaller reduced expression

---

# Why Push Result Back?

Because computed result itself may become:

- operand for larger expression

Example:

```text id="rpn10"
2 1 + 3 *
```

After:

```text id="rpn11"
2 1 +
```

result becomes:

```text id="rpn12"
3
```

Then:

```text id="rpn13"
3 * 3
```

must continue evaluation.

So reduced results re-enter stack.

---

# Step 3 — Code Reconstruction

---

# Helper Function

```python id="rpn14"
def round_to_zero(self, n: float) -> int:
```

---

# Why This Exists

Problem specifies:

```text id="rpn15"
division truncates toward zero
```

Python behavior differs.

---

# Important Python Detail

Python integer division:

```python id="rpn16"
-3 // 2
```

gives:

```text id="rpn17"
-2
```

because Python floors downward.

But problem wants:

```text id="rpn18"
-1
```

(truncate toward zero)

---

# Your Solution

```python id="rpn19"
if n >= 0:
    return floor(n)
return ceil(n)
```

This correctly truncates toward zero.

Good handling.

---

# Stack Initialization

```python id="rpn20"
stack = []
```

---

# What Stack Stores

Partially evaluated operand values.

Example:

```python id="rpn21"
[2,3]
```

means:

- these values are waiting for future operators

---

# Main Loop

```python id="rpn22"
for token in tokens:
```

Sequential expression evaluation.

---

# Case 1 — Operand

```python id="rpn23"
if token not in ["+", "-", "*", "/"]:
    stack.append(int(token))
```

---

# Meaning

Operand cannot yet be evaluated.

So:

- defer computation

Push into stack.

---

# Why Convert to int?

Input tokens are strings.

Arithmetic requires numeric values.

---

# Case 2 — Operator

```python id="rpn24"
else:
```

This triggers:

- expression reduction

---

# Pop Operands

```python id="rpn25"
num2 = int(stack.pop())
num1 = int(stack.pop())
```

---

# IMPORTANT ORDERING DETAIL

This is EXTREMELY important.

Suppose expression:

```text id="rpn26"
4 2 -
```

Means:

```text id="rpn27"
4 - 2
```

NOT:

```text id="rpn28"
2 - 4
```

Because:

- second popped value is LEFT operand

Stack order matters critically.

---

# Why LIFO Works Perfectly

Latest operands belong to:

- most recent unfinished expression

Exactly what operator needs.

---

# Addition

```python id="rpn29"
stack.append(num1 + num2)
```

---

# Meaning

Reduce:

```text id="rpn30"
num1 + num2
```

into:

- single computed value

---

# Subtraction

```python id="rpn31"
stack.append(num1 - num2)
```

Order critically matters.

---

# Multiplication

```python id="rpn32"
stack.append(num1 * num2)
```

---

# Division

```python id="rpn33"
stack.append(self.round_to_zero(num1 / num2))
```

---

# Why Push Back?

Computed result becomes:

- operand for larger future expressions

This recursive reduction idea is the heart of evaluator stacks.

---

# Final Result

```python id="rpn34"
return stack[0]
```

---

# Why Single Remaining Value?

Entire expression progressively collapses into:

- one final evaluated result

---

# Important Invariant

After every operator:

```text id="rpn35"
two operands removed
one reduced value added
```

Stack size shrinks by:

```text id="rpn36"
1
```

Eventually:

- one value remains

---

# Step 4 — Visual Execution

Let’s trace:

```text id="rpn37"
["2","1","+","3","*"]
```

---

# Read 2

Push:

```python id="rpn38"
[2]
```

---

# Read 1

Push:

```python id="rpn39"
[2,1]
```

---

# Read +

Pop:

- num2 = 1
- num1 = 2

Compute:

```text id="rpn40"
2 + 1 = 3
```

Push:

```python id="rpn41"
[3]
```

Notice:

- subexpression reduced

---

# Read 3

Push:

```python id="rpn42"
[3,3]
```

---

# Read \*

Pop:

- 3
- 3

Compute:

```text id="rpn43"
3 * 3 = 9
```

Push:

```python id="rpn44"
[9]
```

Final result:

```text id="rpn45"
9
```

Correct.

---

# Harder Example

```text id="rpn46"
4 13 5 / +
```

---

# Push 4

```python id="rpn47"
[4]
```

---

# Push 13

```python id="rpn48"
[4,13]
```

---

# Push 5

```python id="rpn49"
[4,13,5]
```

---

# Read /

Compute:

```text id="rpn50"
13 / 5 = 2
```

Push:

```python id="rpn51"
[4,2]
```

---

# Read +

Compute:

```text id="rpn52"
4 + 2 = 6
```

Final:

```python id="rpn53"
[6]
```

Correct.

---

# Time Complexity

Each token:

- pushed once
- popped at most once

Total:

```text id="rpn54"
O(n)
```

---

# Space Complexity

Worst case:

- many operands before operators

```text id="rpn55"
O(n)
```

---

# Deep Conceptual Insight

Previous stack problems stored:

- unresolved future elements
- navigation history
- parser contexts
- survivors

This problem stores:

```text id="rpn56"
partially reduced computations
```

This is the foundational abstraction behind:

- interpreters
- calculators
- virtual machines
- compilers

---

# Pattern Extraction

# Trigger

- postfix expressions
- deferred operators
- nested reductions
- expression evaluation

---

# Pattern

Stack-Based Expression Reduction

---

# Structure

```text id="rpn57"
stack stores partially evaluated operands/results
```

---

# Flow

```text id="rpn58"
operand
→ push

operator
→ pop operands
→ evaluate
→ push reduced result
```

---

# Most Important Insight

The stack is NOT storing:

- unresolved questions
- structural boundaries
- ordering constraints

It is storing:

```text id="rpn59"
intermediate computational state
```

Each operator progressively reduces:

- multiple values
  → into one simpler value

until the entire expression collapses into a final result.
