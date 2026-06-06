Excellent.

This is the problem where graph traversal evolves into **shortest-path thinking**.

Number of Islands taught:

```txt
DFS explores a component.
```

Clone Graph taught:

```txt
Traversal can build structures.
```

Rotting Oranges teaches:

```txt
Traversal can model time.
```

That's the new idea.

---

# Step 1 — Pattern Prediction

Before seeing the solution:

## Recognition Signals

The problem says:

```txt
Every minute...
```

```txt
Adjacent...
```

```txt
Minimum number of minutes...
```

These are massive clues.

---

## Pattern

```txt
Trigger:
minimum minutes
spread
infection
wave
levels

↓

Pattern:
BFS

↓

Structure:
Queue

↓

Traversal:
Level-by-Level
```

---

# Why DFS Is The Wrong Mental Model

Imagine:

```txt
2 1 1
1 1 1
1 1 1
```

If DFS starts at the rotten orange:

```txt
2 → 1 → 1 → 1 → ...
```

it goes deep into one branch.

But rotting happens simultaneously.

Reality:

```txt
Minute 0:
2

Minute 1:
all neighbors rot

Minute 2:
their neighbors rot

Minute 3:
...
```

This is not depth-first behavior.

It is a wave.

---

# The Core Mental Model

Think of dropping a stone into water.

```txt
Minute 0

    X
```

```txt
Minute 1

   XXX
```

```txt
Minute 2

 XXXXX
```

The wave expands outward.

BFS naturally processes nodes exactly this way.

---

# Why We Start With All Rotten Oranges

You wrote:

```python
if grid[i][j] == ROTTEN:
    queue.append((i, j))
```

This is the most important insight in the solution.

---

Instead of:

```txt
One starting node
```

we have:

```txt
Many starting nodes
```

Example:

```txt
2 1 1
1 1 2
```

Two rotten oranges start spreading at the same time.

So we place BOTH into the queue initially.

---

This pattern is called:

```txt
Multi-Source BFS
```

Very important.

---

# Why Count Fresh Oranges?

You wrote:

```python
fresh_num += 1
```

Let's understand why.

---

At the end we must answer:

```txt
Did every fresh orange rot?
```

Without tracking fresh oranges, we'd need another scan.

Instead:

```python
fresh_num -= 1
```

every time a fresh orange becomes rotten.

---

Then:

```python
fresh_num == 0
```

immediately tells us:

```txt
Mission accomplished.
```

---

# Why Return Early?

You wrote:

```python
if fresh_num == 0:
    return 0
```

Meaning:

```txt
No fresh oranges exist.
```

The answer is:

```txt
0 minutes
```

because nothing needs to happen.

---

# The Queue Meaning

At any moment:

```python
queue
```

contains:

```txt
All oranges that became rotten
during the previous minute.
```

This is crucial.

---

Suppose:

```txt
Minute 0

2 1 1
```

Queue:

```txt
[(0,0)]
```

---

After processing:

```txt
Minute 1

2 2 1
```

Queue becomes:

```txt
[(0,1)]
```

The queue now represents:

```txt
Oranges that will spread
during the NEXT minute.
```

---

# The Most Important BFS Pattern

This line:

```python
for _ in range(len(queue)):
```

is the entire BFS lesson.

---

Why?

Because:

```txt
One iteration of this loop
=
One minute
```

---

Suppose queue contains:

```txt
A B C
```

These oranges are all rotten at the same time.

So they must all spread before:

```txt
minute += 1
```

advances.

---

Without level processing:

```txt
A spreads
new orange spreads immediately
new orange spreads immediately
```

Time becomes incorrect.

---

# Visual Execution

Example:

```txt
2 1 1
1 1 0
0 1 1
```

---

Minute 0

```txt
2 1 1
1 1 0
0 1 1
```

Queue:

```txt
[(0,0)]
```

---

Minute 1

Rot:

```txt
(0,1)
(1,0)
```

Grid:

```txt
2 2 1
2 1 0
0 1 1
```

Queue:

```txt
[(0,1),(1,0)]
```

---

Minute 2

Rot:

```txt
(0,2)
(1,1)
```

Grid:

```txt
2 2 2
2 2 0
0 1 1
```

Queue:

```txt
[(0,2),(1,1)]
```

---

Minute 3

Rot:

```txt
(2,1)
```

Grid:

```txt
2 2 2
2 2 0
0 2 1
```

Queue:

```txt
[(2,1)]
```

---

Minute 4

Rot:

```txt
(2,2)
```

Grid:

```txt
2 2 2
2 2 0
0 2 2
```

Queue:

```txt
[(2,2)]
```

Fresh oranges:

```txt
0
```

Answer:

```txt
4
```

---

# Why `minutes - 1`?

Let's trace.

When the last orange rots:

```txt
Minute 4
```

it gets added to the queue.

The loop runs one more time:

```txt
Minute 5
```

processing that orange even though it spreads to nobody.

So:

```python
minutes
```

ends up one larger than the true answer.

Hence:

```python
minutes - 1
```

---

# What This Problem Adds To Your Graph Toolbox

Number of Islands taught:

```txt
Visit everything in a component.
```

Rotting Oranges teaches:

```txt
Visit everything by distance.
```

That's a major shift.

---

# Pattern Extraction

```txt
Trigger:
minimum minutes
minimum moves
minimum steps
spread
infection
wave

↓

Pattern:
BFS

↓

Structure:
Queue

↓

Special Form:
Multi-Source BFS

↓

Flow:
Put all sources into queue
        ↓
Process one level
        ↓
One level = one minute
        ↓
Expand outward
        ↓
Repeat
```

---

This exact pattern reappears in:

- Walls and Gates (286)
- 01 Matrix (542)
- As Far from Land as Possible (1162)
- Shortest Bridge (934)

When you see:

```txt
Many starting points
+
spreading over time
+
minimum steps/minutes
```

your brain should immediately jump to:

```txt
Multi-Source BFS
```
