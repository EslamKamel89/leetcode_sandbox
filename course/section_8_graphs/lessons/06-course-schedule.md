This is the most important graph problem in your graph curriculum.

Why?

Because it introduces the first genuinely new graph concept since DFS/BFS:

```txt
Directed Cycle Detection
```

Everything before this was:

```txt
Can I reach nodes?
Can I count components?
Can I spread through a graph?
```

Course Schedule asks:

```txt
Can these dependencies be satisfied?
```

which is really:

```txt
Does a cycle exist?
```

---

# Step 1 — Pattern Prediction

Before coding, translate the problem.

---

## What Does The Problem Actually Say?

Input:

```txt
[1,0]
```

means:

```txt
0 → 1
```

because:

```txt
Take 0 first
then take 1
```

---

Another example:

```txt
[2,1]
```

means:

```txt
1 → 2
```

---

The graph is:

```txt
prerequisite
      ↓
course
```

or equivalently:

```txt
course depends on prerequisite
```

---

# Recognition Signals

When you see:

```txt
prerequisite
dependency
must take before
order
schedule
```

you should immediately think:

```txt
Directed Graph
```

and often:

```txt
Topological Sort
Cycle Detection
```

---

# The Core Insight

Suppose:

```txt
0 → 1
1 → 2
```

You can take:

```txt
0
↓
1
↓
2
```

Everything is fine.

---

Now suppose:

```txt
0 → 1
1 → 0
```

To take 0:

```txt
need 1
```

To take 1:

```txt
need 0
```

Impossible.

---

The entire problem becomes:

```txt
Can a dependency cycle exist?
```

If yes:

```txt
False
```

If no:

```txt
True
```

---

# Why Graph Valid Tree's Parent Trick Doesn't Work

In Graph Valid Tree:

```txt
0 -- 1
```

When node 1 sees node 0 again:

```txt
that's expected
```

because the graph is undirected.

---

Course Schedule is different.

Graph:

```txt
0 → 1
```

Node 1 does NOT point back to 0.

So:

```txt
Seeing a node again
means something different.
```

We need a new cycle detection method.

---

# The New Mental Model

Instead of asking:

```txt
Have I ever visited this node?
```

we ask:

```txt
Is this node currently
being explored?
```

That distinction is everything.

---

# Why Two States Are Not Enough

Suppose we use:

```txt
UNVISITED
VISITED
```

only.

---

Graph:

```txt
0 → 1
0 → 2
1 → 3
2 → 3
```

When we reach:

```txt
3
```

from node 2,

it was already visited through node 1.

That's completely legal.

No cycle exists.

---

So:

```txt
visited again
≠
cycle
```

in a directed graph.

This is why we need three states.

---

# The Three-State System

You wrote:

```python
UNVISITED = 0
VISITING = 1
VISITED = 2
```

This is the key idea.

---

## UNVISITED

```txt
Never explored.
```

---

## VISITING

```txt
Currently on DFS path.
```

Think:

```txt
call stack
```

---

## VISITED

```txt
Finished completely.
```

No future work remains.

---

# The Most Important Insight

Cycle detection is really:

```txt
Did I encounter a node
already on my current DFS path?
```

That's exactly what:

```python
VISITING
```

represents.

---

# Understanding Your DFS

Start:

```python
state = states[crs]
```

Retrieve current status.

---

## Case 1

```python
if state == VISITED:
    return True
```

Meaning:

```txt
I already verified this subtree.
```

Safe.

No need to explore again.

---

Example:

```txt
0 → 1 → 3
 \
  → 2 → 3
```

After exploring:

```txt
3
```

once,

future visits are safe.

---

## Case 2

```python
if state == VISITING:
    return False
```

This is the cycle check.

---

Why?

Because:

```txt
VISITING
```

means:

```txt
This node is already
on my recursion stack.
```

---

Example:

```txt
0 → 1 → 2
     ↑   ↓
     └───┘
```

DFS:

```txt
0
↓
1
↓
2
```

Now:

```txt
2 → 1
```

---

Node 1 is:

```txt
VISITING
```

which means:

```txt
I found a path
back into my current path.
```

That is a cycle.

---

# Mark As VISITING

You do:

```python
states[crs] = VISITING
```

before exploring neighbors.

Meaning:

```txt
This node is now
on the active DFS path.
```

---

# Explore Dependencies

```python
for nei in adj[crs]:
```

Interpretation:

```txt
Before taking course,
can I complete prerequisites?
```

---

If any prerequisite fails:

```python
if not dfs(nei):
    return False
```

then:

```txt
whole schedule fails
```

---

# Mark As VISITED

After all prerequisites succeed:

```python
states[crs] = VISITED
```

Meaning:

```txt
I completely validated
this course and everything below it.
```

---

This node leaves the recursion stack.

---

# Visual Execution

Example:

```txt
0 ← 1
↑   ↓
└── 2
```

Equivalent dependencies:

```txt
0 depends on 1
1 depends on 2
2 depends on 0
```

Cycle exists.

---

Start:

```txt
dfs(0)
```

States:

```txt
0 = VISITING
```

---

Go to:

```txt
1
```

States:

```txt
0 = VISITING
1 = VISITING
```

---

Go to:

```txt
2
```

States:

```txt
0 = VISITING
1 = VISITING
2 = VISITING
```

---

Go to:

```txt
0
```

State:

```txt
VISITING
```

Immediately:

```txt
cycle found
```

Return:

```txt
False
```

---

# Why The Outer Loop Exists

You wrote:

```python
for i in range(numCourses):
```

This is important.

---

Graph may be:

```txt
0 → 1

2 → 3
```

Two disconnected components.

If we start only from:

```txt
0
```

we never inspect:

```txt
2
3
```

The outer loop guarantees:

```txt
Every component is checked.
```

---

# Complexity

Each course:

```txt
UNVISITED
↓
VISITING
↓
VISITED
```

only once.

---

Time:

```txt
O(V + E)
```

---

Space:

```txt
O(V)
```

for recursion stack and states.

---

# Relationship To Topological Sort

This is important.

Course Schedule is often taught as:

```txt
Topological Sort
```

But the deeper pattern is:

```txt
Directed Cycle Detection
```

because:

```txt
A topological ordering exists
iff
the graph has no cycle.
```

This problem only asks:

```txt
Does a valid ordering exist?
```

So detecting cycles is enough.

Course Schedule II will ask:

```txt
What is the ordering?
```

and that's where full Topological Sort becomes necessary.

---

# Pattern Extraction

```txt
Trigger:
prerequisites
dependencies
must happen before
course schedule

↓

Pattern:
Directed Cycle Detection

↓

Structure:
3-State DFS

↓

States:
UNVISITED
VISITING
VISITED

↓

Cycle Rule:
Reach VISITING node
→ cycle

↓

Flow:
Start DFS
    ↓
Mark VISITING
    ↓
Explore dependencies
    ↓
Reach VISITING again?
    cycle
    ↓
Finish exploration
    ↓
Mark VISITED
```

---

Notice how the graph curriculum is building:

```txt
Number of Islands
    ↓
Connected Components

Graph Valid Tree
    ↓
Cycle Detection (Undirected)

Course Schedule
    ↓
Cycle Detection (Directed)
```

That's exactly the progression you want: each problem introduces one major new graph idea while reusing the traversal foundation.
