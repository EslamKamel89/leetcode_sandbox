Excellent choice.

This is one of the most important graph problems because it teaches a new idea:

> In Number of Islands, traversal was the goal.
>
> In Clone Graph, traversal is just a tool.
>
> The real goal is graph construction.

---

# Step 1 — Pattern Prediction

Before looking at code, the pattern should be:

```txt
Trigger:
clone
copy
deep copy
graph object

↓

Pattern:
Graph Traversal + Graph Construction

↓

Structure:
Original → Clone Mapping

↓

Traversal:
DFS or BFS
```

---

# Why This Is NOT a Traversal Problem

In Number of Islands:

```txt
Visit node
↓
Mark visited
↓
Done
```

The result was:

```txt
count
```

In Clone Graph:

```txt
Visit node
↓
Create new node
↓
Connect neighbors
↓
Return new graph
```

The result is:

```txt
a completely new graph
```

Traversal merely allows us to reach every node.

---

# The Core Difficulty

Suppose we have:

```txt
1 -- 2
|    |
4 -- 3
```

and start cloning node 1.

We create:

```txt
1'
```

Now we need neighbors:

```txt
2'
4'
```

But those clones may not exist yet.

This creates the central challenge:

> How do we remember which clone belongs to which original node?

---

# The Key Data Structure

This line is the heart of the problem:

```python
o_to_n = {}
```

Mental model:

```txt
Original Node
      ↓
Cloned Node
```

Example:

```txt
1 -> 1'
2 -> 2'
3 -> 3'
4 -> 4'
```

Without this mapping:

```txt
You cannot connect cloned neighbors.
```

---

# Comparing to Number of Islands

Number of Islands used:

```python
visited.add(node)
```

because we only cared about:

```txt
Have I seen this node?
```

Clone Graph needs more.

We care about:

```txt
What clone corresponds to this node?
```

So:

```python
visited
```

becomes

```python
old_to_new
```

This is one of the most important graph lessons.

---

# Looking At Your DFS

You wrote:

```python
visited.add(node)
o_to_n[node] = Node(node.val)
```

Meaning:

```txt
I discovered this node.
↓
Create its clone.
↓
Store the relationship.
```

Very good.

---

# Why Create The Clone Immediately?

Suppose we delay:

```python
Node(node.val)
```

until later.

Consider a cycle:

```txt
1 -> 2
↑    ↓
4 <- 3
```

While exploring:

```txt
1
↓
2
↓
3
↓
4
↓
1
```

Eventually we need:

```txt
clone(1)
```

again.

If it wasn't already created:

```txt
duplicate clones appear
```

which breaks the graph.

Creating immediately guarantees:

```txt
every original node
has exactly one clone
```

---

# What Your DFS Really Does

Your DFS performs:

```txt
Discover all nodes
Create all clones
Build mapping
```

but does NOT connect edges yet.

After DFS:

```txt
1 -> 1'
2 -> 2'
3 -> 3'
4 -> 4'
```

exists.

---

# Second Pass

You then do:

```python
for old, new in o_to_n.items():
```

This means:

```txt
For every original node
find its clone
```

---

Then:

```python
for nei in old.neighbors:
```

For example:

```txt
old = 1

neighbors:
2
4
```

---

Then:

```python
new.neighbors.append(o_to_n[nei])
```

Meaning:

```txt
neighbor original
      ↓
neighbor clone
```

Example:

```txt
1.neighbors = [2,4]

↓

1'.neighbors = [2',4']
```

This reconstructs the graph structure.

---

# Visual Execution

Original graph:

```txt
1 -- 2
|    |
4 -- 3
```

---

## DFS Phase

Visit:

```txt
1
2
3
4
```

Create:

```txt
1'
2'
3'
4'
```

Mapping:

```txt
{
 1:1'
 2:2'
 3:3'
 4:4'
}
```

No edges yet.

---

## Reconstruction Phase

Process:

```txt
1
```

Neighbors:

```txt
2
4
```

Add:

```txt
1' -> 2'
1' -> 4'
```

---

Process:

```txt
2
```

Neighbors:

```txt
1
3
```

Add:

```txt
2' -> 1'
2' -> 3'
```

Continue.

Result:

```txt
1' -- 2'
|      |
4' -- 3'
```

Perfect clone.

---

# Interesting Observation About Your Solution

You have:

```python
visited = set()
```

and

```python
o_to_n = {}
```

Both track discovery.

Because:

```python
o_to_n[node]
```

already means:

```txt
node was visited
```

you can actually eliminate:

```python
visited
```

and use:

```python
if node in o_to_n:
```

instead.

Many optimal solutions do exactly that.

The mapping becomes both:

```txt
visited structure
+
clone lookup structure
```

---

# A More Graph-Oriented Mental Model

Don't think:

```txt
DFS copies graph
```

Think:

```txt
DFS discovers graph

Dictionary remembers clones

Dictionary prevents cycles

Dictionary allows edge reconstruction
```

The dictionary is the real solution.

DFS is merely the vehicle that reaches every node.

---

# Pattern Extraction

```txt
Trigger:
clone
deep copy
copy graph
duplicate structure

↓

Pattern:
Graph Traversal + Graph Construction

↓

Structure:
original_node -> cloned_node

↓

Flow:
Visit node
    ↓
Create clone
    ↓
Store mapping
    ↓
Visit neighbors
    ↓
Connect cloned neighbors

↓

Key Insight:
Visited becomes a dictionary,
not just a set.
```

---

One question before moving on:

Suppose we remove `o_to_n` entirely and only keep a `visited` set.

After DFS finishes, what information do we no longer have that makes cloning impossible?
