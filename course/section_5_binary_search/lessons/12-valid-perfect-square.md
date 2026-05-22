# Step 1 — Pattern Prediction

This is another:

```txt id="vps001"
Binary Search on Monotonic Function
```

problem.

It is extremely closely related to:

```txt id="vps002"
sqrt(x)
```

In fact:

```txt id="vps003"
this is essentially the boolean version of sqrt(x)
```

That relationship is important to recognize.

---

# The Real Problem

We need to determine:

```txt id="vps004"
Does there exist an integer m
such that:
```

m^2 = num

---

# The Deep Insight

We are NOT searching inside an array.

We are searching among:

```txt id="vps005"
possible integer answers
```

The search space is:

```txt id="vps006"
0 → num
```

because the square root can never exceed the number itself.

---

# Why Binary Search Works

Because squares grow monotonically.

As `m` increases:

m^2

also increases.

That creates ordered behavior.

---

# Example

Suppose:

```txt id="vps007"
num = 16
```

Evaluate:

```txt id="vps008"
0² = 0
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

Now notice:

```txt id="vps009"
values increase steadily
```

That monotonic structure enables Binary Search.

---

# Important Difference From sqrt(x)

In `sqrt(x)`:

```txt id="vps010"
we searched for largest valid integer
```

using condition:

m^2 \le x

Here:

```txt id="vps011"
we search for EXACT equality
```

using condition:

m^2 = num

That is the key distinction.

---

# Recognition Signals

Look for phrases like:

| Phrase              | Meaning                 |
| ------------------- | ----------------------- |
| perfect square      | exact square match      |
| integer square root | monotonic math          |
| no sqrt allowed     | numerical binary search |

---

# Step 2 — Understanding Your Solution

Your solution is clean and correct.

This is now closer to:

```txt id="vps012"
classic binary search
```

than `sqrt(x)` was.

Why?

Because:

```txt id="vps013"
we CAN terminate on equality
```

If:

m^2 = num

then we are done immediately.

No boundary search needed.

---

# Step 3 — Reconstruct The Algorithm Slowly

---

# Step 3.1 — Define Search Space

```python id="vps014"
left, right = 0, num
```

---

# Why?

Possible square roots must lie inside:

```txt id="vps015"
[0 → num]
```

Example:

```txt id="vps016"
sqrt(16) <= 16
sqrt(100) <= 100
```

---

# Step 3.2 — Binary Search Loop

```python id="vps017"
while left <= right:
```

Standard shrinking interval.

---

# Step 3.3 — Middle Candidate

```python id="vps018"
m = (left + right) // 2
```

Candidate square root.

---

# Step 3.4 — Compute Square

```python id="vps019"
sqr = m * m
```

We evaluate the monotonic function:

f(m)=m^2

---

# Step 3.5 — Exact Match

```python id="vps020"
if sqr == num:
    return True
```

Meaning:

```txt id="vps021"
we found an integer square root
```

So number is a perfect square.

---

# Step 3.6 — Too Large

```python id="vps022"
if sqr > num:
```

Meaning:

```txt id="vps023"
m is too large
```

And because squares increase monotonically:

```txt id="vps024"
everything RIGHT of m
is also too large
```

So:

```python id="vps025"
right = m - 1
```

---

# Step 3.7 — Too Small

Else:

```txt id="vps026"
m² < num
```

Meaning:

```txt id="vps027"
m too small
```

So search right:

```python id="vps028"
left = m + 1
```

---

# Step 3.8 — No Match Found

If loop ends:

```txt id="vps029"
no integer square root exists
```

Return:

```python id="vps030"
False
```

---

# Final Clean Solution

```python id="vps031"
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 0, num

        while left <= right:

            m = (left + right) // 2

            sqr = m * m

            if sqr == num:
                return True

            if sqr > num:
                right = m - 1

            else:
                left = m + 1

        return False
```

---

# Small Improvement

Prefer:

```python id="vps032"
m * m
```

instead of:

```python id="vps033"
m ** 2
```

because multiplication is more direct.

---

# Step 4 — Visual Execution

Input:

```txt id="vps034"
num = 16
```

---

# Iteration 1

```txt id="vps035"
left = 0
right = 16
m = 8
```

Evaluate:

8^2 = 64

```txt id="vps036"
64 > 16
```

Too large.

Move left.

```txt id="vps037"
right = 7
```

---

# Iteration 2

```txt id="vps038"
left = 0
right = 7
m = 3
```

Evaluate:

3^2 = 9

```txt id="vps039"
9 < 16
```

Too small.

Move right.

```txt id="vps040"
left = 4
```

---

# Iteration 3

```txt id="vps041"
left = 4
right = 7
m = 5
```

Evaluate:

5^2 = 25

Too large.

```txt id="vps042"
right = 4
```

---

# Iteration 4

```txt id="vps043"
left = 4
right = 4
m = 4
```

Evaluate:

4^2 = 16

Exact match.

Return:

```txt id="vps044"
True
```

---

# Complexity Analysis

At every step:

```txt id="vps045"
half search space eliminated
```

So:

```txt id="vps046"
O(log num)
```

---

# Space Complexity

```txt id="vps047"
O(1)
```

---

# Pattern Extraction

| Component          | Meaning                             |
| ------------------ | ----------------------------------- |
| Trigger            | integer mathematical search         |
| Pattern            | Binary Search on Monotonic Function |
| Search Space       | possible roots                      |
| Monotonic Function | m²                                  |
| Search Goal        | exact equality                      |
| Key Insight        | numerical space can be searched     |
| Complexity         | O(log num)                          |

---

# Deepest Insight From This Problem

This problem reinforces the major Binary Search abstraction:

```txt id="vps048"
Binary Search works on ANY ordered space.
```

Not just arrays.

Here the ordered space is:

```txt id="vps049"
possible integer roots
```

That mental model is the foundation for advanced optimization problems later.
