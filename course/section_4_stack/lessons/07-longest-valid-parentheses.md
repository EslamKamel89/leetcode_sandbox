For someone at your stage (you've finished stacks, trees, graphs, and are entering DP), the **most intuitive solution is actually the Stack solution**, not the DP solution.

Why?

Because this problem is fundamentally asking:

> "For every `)` can I find the matching `(`, and what is the longest continuous valid region?"

That's exactly what a stack is good at: tracking unmatched parentheses.

---

# Mental Model

Imagine we're scanning:

```txt
)()())
```

Whenever we see:

```txt
(
```

we don't know where it ends yet.

So we store its index.

Whenever we see:

```txt
)
```

we try to match the most recent `(`.

This is exactly the same idea as Valid Parentheses.

The new challenge is:

> After matching, how do we know the length of the valid substring?

---

# Key Insight

Store **indices**, not characters.

Example:

```txt
Index: 0 1 2 3 4 5
Chars: ) ( ) ( ) )
```

Stack:

```txt
[-1]
```

Why `-1`?

Because we need a "boundary" before the string starts.

Think of it as:

```txt
| ) ( ) ( ) )
-1
```

---

# Algorithm

For every character:

### Case 1: '('

Push its index.

```python
stack.append(i)
```

---

### Case 2: ')'

Pop.

```python
stack.pop()
```

This attempts to match a previous `'('`.

---

After popping:

### Stack became empty

Example:

```txt
)
```

No matching opening bracket exists.

This position becomes a new boundary.

```python
stack.append(i)
```

---

### Stack not empty

Then:

```python
length = i - stack[-1]
```

Why?

Because:

```txt
stack[-1]
```

is now the position before the current valid region.

So:

```txt
current_index - boundary
```

gives the valid length.

---

# Example Walkthrough

```txt
s = "()()"
```

Initialize:

```txt
stack = [-1]
max_len = 0
```

---

Index 0:

```txt
(
```

Push:

```txt
[-1,0]
```

---

Index 1:

```txt
)
```

Pop:

```txt
[-1]
```

Length:

```txt
1 - (-1) = 2
```

```txt
max_len = 2
```

---

Index 2:

```txt
(
```

Push:

```txt
[-1,2]
```

---

Index 3:

```txt
)
```

Pop:

```txt
[-1]
```

Length:

```txt
3 - (-1) = 4
```

```txt
max_len = 4
```

Answer:

```txt
4
```

---

# Why Does This Work?

The stack always contains:

```txt
indices of unmatched '('
```

plus

```txt
the most recent invalid boundary
```

When a match is completed:

```txt
current_index - boundary
```

immediately gives the size of the valid region.

No DP table.

No recursion.

No complicated state transitions.

---

# Code

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
```

---

# Complexity

Time:

```txt
O(n)
```

Each index is pushed and popped at most once.

Space:

```txt
O(n)
```

In the worst case:

```txt
((((((((
```

all indices stay in the stack.

---

# From a Pattern Perspective

This is **not really a DP problem** even though LeetCode lists a DP solution.

Recognition signals:

```txt
matching pairs
balanced symbols
nearest unresolved opening
parentheses
brackets
```

These are classic **Stack Pattern** signals from Section 4.

If I were teaching this in your curriculum, I would place it under:

```txt
SECTION 4 — Stack
    ↓
Advanced Stack
    ↓
Track indices instead of values
```

and only show the DP solution afterward as an alternative formulation.

Let's use a classic tricky example:

```txt
s = ")()())()(()())"
```

Index map:

```txt
Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Char :  ) ( ) ( ) ) ( ) ( (  )  (  )  )  )
```

We'll track:

```python
stack = [-1]
max_len = 0
```

Remember:

- stack contains unmatched `'('` indices
- plus the most recent invalid boundary
- when we match a pair:

```python
length = i - stack[-1]
```

---

# Start

```txt
stack = [-1]
max_len = 0
```

---

# i = 0, ch = ')'

Pop:

```txt
stack = []
```

Empty stack means:

```txt
This ')' cannot be matched.
```

New boundary:

```txt
stack = [0]
```

Visualization:

```txt
) ( ) ( ) ) ( ) ( ( ) ( ) ) )
^
invalid boundary
```

---

# i = 1, ch = '('

Push:

```txt
stack = [0,1]
```

---

# i = 2, ch = ')'

Pop:

```txt
stack = [0]
```

Now stack isn't empty.

Length:

```txt
2 - 0 = 2
```

Valid substring:

```txt
()
```

Update:

```txt
max_len = 2
```

---

# i = 3, ch = '('

Push:

```txt
stack = [0,3]
```

---

# i = 4, ch = ')'

Pop:

```txt
stack = [0]
```

Length:

```txt
4 - 0 = 4
```

Substring:

```txt
()()
```

Update:

```txt
max_len = 4
```

---

# i = 5, ch = ')'

Pop:

```txt
stack = []
```

No matching '('.

New boundary:

```txt
stack = [5]
```

Visualization:

```txt
)()())
     ^
 boundary
```

Everything before index 5 is now separated from future valid regions.

---

# i = 6, ch = '('

Push:

```txt
stack = [5,6]
```

---

# i = 7, ch = ')'

Pop:

```txt
stack = [5]
```

Length:

```txt
7 - 5 = 2
```

```txt
max_len = 4
```

(no change)

---

# i = 8, ch = '('

Push:

```txt
stack = [5,8]
```

---

# i = 9, ch = '('

Push:

```txt
stack = [5,8,9]
```

---

# i = 10, ch = ')'

Pop:

```txt
stack = [5,8]
```

Length:

```txt
10 - 8 = 2
```

This corresponds to:

```txt
()
```

---

# i = 11, ch = '('

Push:

```txt
stack = [5,8,11]
```

---

# i = 12, ch = ')'

Pop:

```txt
stack = [5,8]
```

Length:

```txt
12 - 8 = 4
```

Substring:

```txt
()()
```

---

# i = 13, ch = ')'

Pop:

```txt
stack = [5]
```

Length:

```txt
13 - 5 = 8
```

This is the crucial step.

Look at indices:

```txt
6 7 8 9 10 11 12 13
( ) ( (  )  (  )  )
```

which is:

```txt
()(()())
```

Length:

```txt
8
```

Update:

```txt
max_len = 8
```

---

# i = 14, ch = ')'

Pop:

```txt
stack = []
```

No matching '('.

New boundary:

```txt
stack = [14]
```

Done.

---

# Final Answer

```txt
max_len = 8
```

---

# The Deep Insight

Most people understand the pushes and pops.

The confusing part is usually:

```python
length = i - stack[-1]
```

Why does that work?

Let's zoom in on the important moment:

Before processing index 13:

```txt
stack = [5,8]
```

After popping:

```txt
stack = [5]
```

Now:

```txt
stack[-1] = 5
```

What does 5 represent?

```txt
Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
Char : ) ( ) ( ) ) ( ) ( (  )  (  )  )
                ^
```

Index 5 is the last place where validity broke.

Everything after index 5 up to index 13 is valid.

So:

```txt
boundary + 1 = 6
current index = 13
```

Length:

```txt
13 - 5 = 8
```

Notice we're not measuring from the matching `'('`.

We're measuring from the nearest position that prevents extension to the left.

That's the entire trick of the algorithm.

The stack is simultaneously storing:

1. Unmatched `'('`
2. The boundary of the current valid region

Once that clicks, the solution becomes very natural.
