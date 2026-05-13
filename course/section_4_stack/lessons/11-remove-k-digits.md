# Step 1 — Pattern Prediction

This is an extremely important hybrid problem.

It combines:

# Pattern B — Monotonic Stack

with:

# Greedy Optimization

This is one of the most valuable monotonic-stack interview problems because it teaches:

> stack-based local optimization

instead of:

- nearest greater
- waiting times
- boundary tracking

This is a major evolution in stack thinking.

---

# The Real Problem

The problem is NOT:

```text id="rkd1"
remove k digits
```

The real problem is:

> construct the lexicographically smallest possible number

That is the true optimization goal.

---

# Critical Greedy Insight

Smaller digits are more valuable when they appear earlier.

Example:

```text id="rkd2"
12345
```

is much smaller than:

```text id="rkd3"
21345
```

because:

- earlier positions dominate numeric magnitude

This is the key greedy observation.

---

# Core Question

Suppose:

```text id="rkd4"
1432219
```

and current digit = `4`

Then next digit = `3`

Question:

```text id="rkd5"
Should 4 remain before 3?
```

Answer:

- NO

Because:

```text id="rkd6"
34xxxx
```

is always smaller than:

```text id="rkd7"
43xxxx
```

So:

- remove 4

That is the entire greedy principle.

---

# The Big Monotonic Insight

Whenever:

```text id="rkd8"
previous digit > current digit
```

we should remove the previous larger digit if possible.

That naturally creates:

# a monotonic increasing stack

---

# Why Increasing?

We want digits arranged:

```text id="rkd9"
small → large
```

from left to right whenever possible.

Example desired structure:

```text id="rkd10"
1 2 2 9
```

NOT:

```text id="rkd11"
4 3 2 1
```

So whenever a smaller digit arrives:

- larger previous digits become undesirable

and get popped.

---

# Mental Model

The stack represents:

```text id="rkd12"
the best smallest-number prefix built so far
```

Every new digit asks:

```text id="rkd13"
"Should previous larger digits stay before me?"
```

If not:

- remove them greedily

---

# Step 2 — Why Greedy Works

This is the most important proof idea.

Suppose:

```text id="rkd14"
...53...
```

and we can remove one digit.

Which removal creates smaller number?

Remove:

- 5 → `3...`
  OR
- 3 → `5...`

Clearly:

```text id="rkd15"
3...
```

is smaller.

Therefore:

> removing larger earlier digits is always optimal

That is why local greedy decisions work globally.

---

# Step 3 — High-Level Algorithm

Process digits left → right.

For each digit:

---

# While Previous Digit Is Larger

And removals remain:

```text id="rkd16"
remove previous digit
```

because:

- current smaller digit should move leftward

---

# After Processing

Push current digit into stack.

---

# Final Cleanup

If removals still remain:

- remove from END

Why?

Because remaining digits are already increasing.

Largest impact now comes from:

- removing largest trailing digits

---

# Step 4 — Code Reconstruction

---

# Early Edge Case

```python id="rkd17"
if len(num) <= k:
    return "0"
```

---

# Meaning

If removing:

- all digits
  OR more

smallest result is:

```text id="rkd18"
0
```

---

# Stack Initialization

```python id="rkd19"
stack = []
```

---

# What Stack Stores

Digits of:

- current optimal smallest number prefix

---

# Main Loop

```python id="rkd20"
for c in num:
```

---

# Why Sequential Processing Matters

Earlier digits have:

- larger numeric impact

So left-to-right greedy optimization is essential.

---

# Core While Loop

```python id="rkd21"
while k > 0 and stack and stack[-1] > c:
```

This is the heart of the algorithm.

---

# Condition 1 — `k > 0`

Still allowed to remove digits.

Without removals remaining:

- optimization stops

---

# Condition 2 — `stack`

Need previous digit to compare against.

---

# Condition 3 — `stack[-1] > c`

Critical greedy condition.

Meaning:

```text id="rkd22"
previous digit is harming minimality
```

because current digit is smaller.

---

# Why Pop Is Correct

Suppose:

```text id="rkd23"
stack = [1,4]
current = 3
```

Keeping:

```text id="rkd24"
143...
```

is worse than:

```text id="rkd25"
13...
```

So 4 must go.

---

# Pop Larger Digit

```python id="rkd26"
stack.pop()
```

---

# Conceptual Meaning

We are:

```text id="rkd27"
undoing a bad earlier choice
```

This is monotonic-stack greedy optimization.

---

# Consume One Removal

```python id="rkd28"
k -= 1
```

---

# Why Important

Every pop uses:

- one allowed deletion

---

# Push Current Digit

```python id="rkd29"
stack.append(c)
```

---

# Meaning

Current digit now becomes part of:

- best known minimal prefix

---

# Important Observation

After loop:

- stack tends toward increasing order

Example:

```text id="rkd30"
1 2 2 9
```

This is why:

- monotonic increasing stack

---

# Remaining k Case

```python id="rkd31"
stack = stack[: len(stack) - k]
```

---

# Why Can k Remain?

Example:

```text id="rkd32"
123456
```

No digit causes popping because:

- already increasing

But we still must remove digits.

---

# Why Remove From End?

In increasing sequence:

```text id="rkd33"
123456
```

largest digits are:

- furthest right

Removing trailing digits minimizes number.

Example:

```text id="rkd34"
1234
```

is smaller than:

```text id="rkd35"
1345
```

---

# Remove Leading Zeros

```python id="rkd36"
while stack and stack[0] == "0":
    stack.pop(0)
```

---

# Why Needed?

Example:

```text id="rkd37"
10200
```

Remove 1:

```text id="rkd38"
0200
```

Canonical integer form should be:

```text id="rkd39"
200
```

---

# IMPORTANT OPTIMIZATION NOTE

This line:

```python id="rkd40"
stack.pop(0)
```

is NOT O(1).

Python lists remove-from-front in:

```text id="rkd41"
O(n)
```

because shifting occurs.

---

# Better Alternative

Much better:

```python id="rkd42"
res = "".join(stack).lstrip("0")
```

Cleaner and faster.

---

# Final Result

```python id="rkd43"
res = "".join(stack)
return res if res else "0"
```

---

# Why Empty Result Returns 0

Example:

```text id="rkd44"
num = "10"
k = 2
```

All digits removed.

Empty string should become:

```text id="rkd45"
"0"
```

---

# Cleaner Optimized Version

```python id="rkd46"
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # remove remaining digits from end
        stack = stack[:len(stack) - k]

        # remove leading zeros
        result = "".join(stack).lstrip("0")

        return result if result else "0"
```

---

# Step 5 — Visual Execution

Let’s trace:

```text id="rkd47"
1432219
k = 3
```

---

# Start

```python id="rkd48"
stack = []
```

---

# Read 1

Push:

```text id="rkd49"
[1]
```

---

# Read 4

4 > 1

Push:

```text id="rkd50"
[1,4]
```

---

# Read 3

3 < 4

Pop 4.

k becomes 2.

Stack:

```text id="rkd51"
[1]
```

Push 3:

```text id="rkd52"
[1,3]
```

---

# Read 2

2 < 3

Pop 3.

k becomes 1.

Push 2:

```text id="rkd53"
[1,2]
```

---

# Read 2

Equal.

Push:

```text id="rkd54"
[1,2,2]
```

---

# Read 1

1 < 2

Pop one 2.

k becomes 0.

Push 1:

```text id="rkd55"
[1,2,1]
```

---

# Remaining Digits

Push freely:

```text id="rkd56"
[1,2,1,9]
```

Result:

```text id="rkd57"
1219
```

Correct.

---

# Why Time Complexity Is O(n)

Each digit:

- pushed once
- popped at most once

Total:

```text id="rkd58"
O(n)
```

---

# Space Complexity

Stack stores digits:

```text id="rkd59"
O(n)
```

---

# Deep Conceptual Insight

Daily Temperatures stack stored:

```text id="rkd60"
unresolved future questions
```

Online Stock Span stored:

```text id="rkd61"
compressed dominance regions
```

This problem stores:

```text id="rkd62"
the current optimal greedy construction
```

That is another major evolution of stack usage.

---

# Pattern Extraction

# Trigger

- remove digits/elements
- build smallest/largest sequence
- local ordering optimization

---

# Pattern

Monotonic Increasing Stack + Greedy

---

# Structure

```text id="rkd63"
stack maintains smallest lexicographic prefix
```

---

# Flow

```text id="rkd64"
smaller digit arrives
→ remove larger previous digits
→ improve left-side minimality
→ build increasing structure
```

---

# Most Important Insight

The stack is NOT storing unresolved elements anymore.

It is storing:

```text id="rkd65"
the best greedy answer constructed so far
```

That shift from:

- future-resolution
  → greedy-construction

is a major milestone in monotonic stack mastery.
