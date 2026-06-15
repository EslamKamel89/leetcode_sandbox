Excellent. You've now crossed from **Grid DP** into **String DP**.

This is one of the biggest transitions in Dynamic Programming.

Up until now:

```txt
Climbing Stairs
House Robber
Unique Paths
Minimum Path Sum
```

all had a physical interpretation:

```txt
stair
house
grid cell
grid cell
```

Edit Distance is different.

There is no physical movement.

The state is now:

```txt
position in word1
position in word2
```

This is the beginning of **sequence matching DP**.

---

# Step 1 — Pattern Prediction

Before coding, the signals are:

### Signal 1

Two strings

```txt
word1
word2
```

Whenever a DP problem contains:

```txt
two strings
two sequences
compare strings
transform strings
```

you should immediately think:

```txt
2D String DP
```

---

### Signal 2

We need the minimum number of operations.

Keywords:

```txt
minimum
transform
convert
edit
```

usually indicate:

```txt
Optimization DP
```

---

# Step 2 — State Definition

This is the most important part.

What does:

```txt
dp[r][c]
```

mean?

Your solution uses:

```txt
r -> characters consumed from word2
c -> characters consumed from word1
```

So:

```txt
dp[r][c]
=
minimum operations needed
to convert

word1[:c]

into

word2[:r]
```

Example:

```txt
word1 = horse
word2 = ros
```

Then:

```txt
dp[2][3]
```

means:

```txt
convert

"hor"

into

"ro"
```

using the fewest edits.

---

# Why This State Is Powerful

Notice something.

Instead of asking:

```txt
convert "horse" into "ros"
```

we ask smaller questions:

```txt
convert "h" into "r"

convert "ho" into "ro"

convert "hor" into "ro"
```

These smaller answers get reused.

That's exactly DP.

---

# Step 3 — Understanding the Base Cases

These are extremely important.

---

## First Row

```python
for c in range(len(word1) + 1):
    dp[0][c] = c
```

What does:

```txt
dp[0][c]
```

mean?

It means:

```txt
convert

word1[:c]

into

""
```

(empty string)

The only way:

```txt
delete everything
```

So:

```txt
dp[0][c] = c
```

---

Example:

```txt
"horse" -> ""

needs

5 deletions
```

---

## First Column

```python
for r in range(len(word2) + 1):
    dp[r][0] = r
```

This means:

```txt
convert

""

into

word2[:r]
```

Only possible by:

```txt
inserting characters
```

So:

```txt
dp[r][0] = r
```

---

Example:

```txt
"" -> "ros"

needs

3 insertions
```

---

# Step 4 — Deriving the Transition

This is the heart of Edit Distance.

---

Suppose we're computing:

```txt
dp[r][c]
```

Look at:

```python
word2[r-1]
word1[c-1]
```

the current characters.

---

## Case 1: Characters Match

Example:

```txt
horse
   ^
ros
  ^
```

Suppose both characters are:

```txt
o
```

Then:

```txt
no operation needed
```

The last characters already match.

So:

```txt
dp[r][c]
=
dp[r-1][c-1]
```

Exactly your code:

```python
if word2[r - 1] == word1[c - 1]:
    dp[r][c] = dp[r - 1][c - 1]
```

---

## Case 2: Characters Differ

Example:

```txt
horse
^
ros
^
```

```txt
h != r
```

Now we must perform an operation.

Which one?

---

### Replace

Replace:

```txt
h -> r
```

Then solve the remaining problem.

Cost:

```txt
dp[r-1][c-1] + 1
```

---

### Delete

Delete a character from word1.

Cost:

```txt
dp[r][c-1] + 1
```

---

### Insert

Insert a needed character.

Cost:

```txt
dp[r-1][c] + 1
```

---

Choose the cheapest.

Therefore:

```txt
dp[r][c]
=
1 +
min(
    replace,
    delete,
    insert
)
```

Exactly your recurrence:

```python
dp[r][c] = min(
    dp[r - 1][c],
    dp[r][c - 1],
    dp[r - 1][c - 1]
) + 1
```

---

# Visual Execution

Let's use:

```txt
word1 = "ab"
word2 = "ac"
```

---

Initial table:

```txt
      ""  a   b

""    0   1   2

a     1

c     2
```

---

### Cell (1,1)

Comparing:

```txt
a
a
```

Match.

```txt
dp[1][1]
=
dp[0][0]
=
0
```

Table:

```txt
      ""  a   b

""    0   1   2

a     1   0

c     2
```

---

### Cell (1,2)

Comparing:

```txt
a
b
```

Mismatch.

Choose best operation.

Result:

```txt
1
```

---

### Cell (2,1)

Comparing:

```txt
c
a
```

Mismatch.

Result:

```txt
1
```

---

### Cell (2,2)

Comparing:

```txt
c
b
```

Mismatch.

Best option:

```txt
replace b -> c
```

Result:

```txt
1
```

Final answer:

```txt
1
```

---

# Reviewing Your Solution

Your implementation is the canonical bottom-up Edit Distance solution.

```python
if word2[r - 1] == word1[c - 1]:
    dp[r][c] = dp[r - 1][c - 1]
```

means:

```txt
matching characters contribute zero cost
```

---

```python
dp[r][c] = min(
    dp[r - 1][c],
    dp[r][c - 1],
    dp[r - 1][c - 1]
) + 1
```

means:

```txt
insert
delete
replace

choose cheapest
```

---

Complexity:

```txt
Time:  O(m × n)
Space: O(m × n)
```

where:

```txt
m = len(word1)
n = len(word2)
```

---

# Pattern Extraction

### Trigger

```txt
Two strings
Transform one into another
Minimum operations
```

---

### Pattern

```txt
2D String DP
(Edit Distance Pattern)
```

---

### State

```txt
dp[r][c]

=
minimum edits required

to convert

word1[:c]

into

word2[:r]
```

---

### Transition

If characters match:

```txt
dp[r][c]
=
dp[r-1][c-1]
```

If characters differ:

```txt
dp[r][c]
=
1 + min(
    insert,
    delete,
    replace
)
```

---

### Flow

```txt
Compare current characters
        ↓
Match?
   ↙         ↘
yes          no
 ↓            ↓
Diagonal    Best edit
```

---

This is the first problem in your DP journey where the transition is not:

```txt
sum previous states
```

or

```txt
take/skip
```

Instead it is:

```txt
choose among multiple operations
```

That makes Edit Distance one of the foundational String DP patterns.
