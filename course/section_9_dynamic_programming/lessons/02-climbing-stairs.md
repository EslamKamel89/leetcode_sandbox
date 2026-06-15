Perfect. Since we're following your system, we do **not** start by reviewing the code.

We start with:

# Step 1 — Pattern Prediction

Before seeing any solution, the reasoning should be:

### Recognition Signals

The problem asks:

```txt
How many ways?
```

Not:

```txt
minimum
maximum
shortest
best
```

So this is a **counting problem**.

---

Also notice:

```txt
To reach stair n
I can come from:
    n-1
    n-2
```

The current answer depends on previous positions.

That is the strongest signal for:

```txt
1D Dynamic Programming
```

---

### State

The most natural state is:

```txt
dp[i]
=
number of ways to reach stair i
```

Every DP problem begins with defining the state.

Without a good state, there is no DP.

---

### Transition

To reach stair `i`:

```txt
last move was 1 step
```

or

```txt
last move was 2 steps
```

Therefore:

```txt
dp[i]
=
dp[i-1]
+
dp[i-2]
```

---

### Base Cases

```txt
dp[1] = 1
dp[2] = 2
```

because:

```txt
stair 1:
    [1]

stair 2:
    [1+1]
    [2]
```

---

# Step 2 — Your Solution Review

Your code:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        tab = [0] * (n + 1)

        tab[1] = 1
        tab[2] = 2

        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]

        return tab[n]
```

is completely correct.

Time complexity:

```txt
O(n)
```

Space complexity:

```txt
O(n)
```

---

# Step 3 — Why Does The Transition Work?

This is the important part.

Many people memorize:

```python
dp[i] = dp[i-1] + dp[i-2]
```

without understanding it.

Let's derive it.

---

Suppose:

```txt
n = 5
```

We want:

```txt
ways(5)
```

How can a path end?

Only two possibilities.

### Case 1

The last move was:

```txt
+1
```

Then we must have been at:

```txt
4
```

before that.

Number of possibilities:

```txt
ways(4)
```

---

### Case 2

The last move was:

```txt
+2
```

Then we must have been at:

```txt
3
```

before that.

Number of possibilities:

```txt
ways(3)
```

---

These two groups do not overlap.

Therefore:

```txt
ways(5)
=
ways(4)
+
ways(3)
```

Generalizing:

```txt
ways(i)
=
ways(i-1)
+
ways(i-2)
```

This is the DP transition.

---

# Step 4 — Visual Execution

Let's run:

```txt
n = 5
```

Initial:

```txt
dp[1] = 1
dp[2] = 2
```

Array:

```txt
index: 0 1 2 3 4 5
dp:    0 1 2 ? ? ?
```

---

### i = 3

```txt
dp[3]
=
dp[2] + dp[1]
=
2 + 1
=
3
```

Array:

```txt
0 1 2 3 ? ?
```

---

### i = 4

```txt
dp[4]
=
dp[3] + dp[2]
=
3 + 2
=
5
```

Array:

```txt
0 1 2 3 5 ?
```

---

### i = 5

```txt
dp[5]
=
dp[4] + dp[3]
=
5 + 3
=
8
```

Array:

```txt
0 1 2 3 5 8
```

Answer:

```txt
8
```

---

# Step 5 — Important Observation

Look carefully at:

```python
tab[i] = tab[i - 1] + tab[i - 2]
```

When computing:

```txt
tab[i]
```

we only use:

```txt
tab[i-1]
tab[i-2]
```

Nothing else.

That means the entire array is unnecessary.

We don't actually need:

```txt
O(n)
```

memory.

We only need:

```txt
previous two answers
```

which gives:

```txt
O(1)
```

space.

This is called:

```txt
Space Optimization
```

and is extremely common in DP.

---

# Pattern Extraction

### Trigger

```txt
Count number of ways
Current position depends on previous positions
```

### Pattern

```txt
1D Dynamic Programming
(Fibonacci-style DP)
```

### Structure

```txt
dp[i]
=
number of ways to reach i
```

### Transition

```txt
dp[i]
=
dp[i-1] + dp[i-2]
```

### Flow

```txt
Base Cases
    ↓
Build smaller answers
    ↓
Reuse them
    ↓
Reach dp[n]
```

---

This problem is the foundation of the entire DP section because it teaches the three ideas that appear in almost every DP problem:

```txt
State
    ↓
Transition
    ↓
Base Cases
```

Before moving to the next problem, can you answer this without coding:

> In Climbing Stairs, why does `dp[i]` represent "ways to reach stair i" instead of "ways to reach the top from stair i"? What would change if we chose the second state definition?
