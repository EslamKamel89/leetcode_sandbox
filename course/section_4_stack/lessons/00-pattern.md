Excellent. SECTION 4 — Stack is one of the most important transitions in pattern-based problem solving because it introduces:

- **state persistence**
- **deferred decisions**
- **processing order constraints**
- **“unresolved elements” thinking**

This section is where many problems stop being “scan and compute” and start becoming:

> “I cannot decide this yet… I need to remember it until future information arrives.”

That is the core mental shift.

Your learning system for this section is exactly correct. We’ll treat Stack as a **family of recognition patterns**, not isolated tricks.

---

# SECTION 4 — STACK

# PHASE 0 — PATTERN FOUNDATION

Before touching problems, we need to build the mental models.

---

# PART 1 — What a Stack REALLY Is

Most beginners learn:

> “Stack = LIFO”

That definition is technically correct but not useful enough for interviews.

The real definition is:

> A stack stores unfinished or unresolved work in the exact order it must be revisited.

That is why stacks appear everywhere:

- parsing
- expression evaluation
- nested structures
- monotonic processing
- undo systems
- DFS traversal
- recursive execution

A stack is fundamentally about:

> “I need to pause this thing and come back later.”

---

# Core Mental Model

Imagine reading code execution:

```python
a(b(c()))
```

You cannot finish `a()` immediately.

You must:

- pause `a`
- go deeper into `b`
- pause `b`
- go deeper into `c`
- finish `c`
- resume `b`
- resume `a`

That pause/resume behavior is a stack.

---

# Recognition Signals for Stack Problems

A problem often wants a stack if you see:

### Signal 1 — Nested Structure

Examples:

- parentheses
- expressions
- XML/HTML tags
- recursive grouping

Because:

- newest opening must close first

That is pure LIFO.

---

### Signal 2 — “Nearest Previous/Next”

Examples:

- next greater element
- previous smaller element
- daily temperatures

These are classic monotonic stack problems.

The key phrase is:

> “Find the nearest thing satisfying a condition.”

---

### Signal 3 — Deferred Decisions

You cannot compute answer immediately.

You must wait for future data.

Example:

- “When will a warmer day appear?”
- “What is next greater number?”

You temporarily store unresolved elements.

---

### Signal 4 — Backtracking / Undo

Examples:

- browser history
- path simplification
- recursive traversal

You need:

- push current state
- pop when reverting

---

# PART 2 — The Major Stack Patterns

SECTION 4 is not one pattern.

It is multiple sub-patterns.

---

# Pattern A — Basic Stack / Matching

---

## What Problem Does It Solve?

Maintains correct ordering of nested or paired structures.

---

## Core Idea

The latest opening item must be closed first.

Example:

```text
({[]})
```

When reading:

- `(` → store it
- `{` → store it
- `[` → store it

Then:

- `]` must match `[`
- `}` must match `{`
- `)` must match `(`

This is impossible to verify correctly without remembering order.

The stack remembers that order.

---

## Recognition Signals

Look for:

- parentheses
- brackets
- nesting
- recursive grouping
- validation problems

Keywords:

- valid
- balanced
- nested
- matching

---

## Typical Problems

- Valid Parentheses
- Min Stack
- Baseball Game
- Backspace String Compare (variation)

---

## Why Stack Works

Because:

- most recent opener is the only valid closer

Older openings are blocked until newer ones resolve.

That is exactly LIFO behavior.

---

# Pattern B — Monotonic Stack

This is the most important stack pattern for interviews.

---

# The Big Idea

A monotonic stack maintains elements in sorted order while scanning.

Usually:

- decreasing stack
  OR
- increasing stack

This lets us efficiently answer:

> “When will this element finally be resolved?”

---

# What Problem Does It Solve?

Nearest greater/smaller relationships.

Without monotonic stack:

- many problems become O(n²)

With monotonic stack:

- O(n)

---

# Mental Model

Suppose:

```text
temps = [73,74,75,71,69,72,76]
```

When at `73`:

- you don't know next warmer day yet
- unresolved

At `74`:

- now `73` is resolved

At `75`:

- now `74` is resolved

The stack stores unresolved temperatures.

Future elements resolve past elements.

That is the key insight.

---

# Why “Monotonic”?

Because the stack maintains order.

Example:
decreasing stack:

```text
75
74
71
69
```

When `72` appears:

- pop `69`
- pop `71`

Because `72` resolves them.

---

# Recognition Signals

Look for:

### “Next greater”

### “Previous smaller”

### “Nearest larger”

### “How many until”

### “First bigger element”

Especially:

- arrays
- linear scans
- nearest relationships

---

# Typical Problems

- Daily Temperatures
- Next Greater Element
- Stock Span
- Largest Rectangle in Histogram
- Trapping Rain Water (advanced variant)

---

# Why It Works

Each element:

- enters stack once
- leaves stack once

So total operations:

```text
O(2n) = O(n)
```

This is one of the most important complexity insights in interviews.

---

# Pattern C — Stack Simulation

---

## What Problem Does It Solve?

Simulating processes with strict ordering.

Examples:

- undo operations
- collisions
- path simplification
- expression evaluation

---

## Mental Model

The stack becomes a “live state history”.

Example:
Asteroid Collision

When a new asteroid arrives:

- it interacts only with recent unresolved asteroids

Again:

- newest unresolved state matters most

That naturally becomes stack behavior.

---

# Pattern D — Expression / Recursive Evaluation

More advanced.

Examples:

- Reverse Polish Notation
- calculators
- parsing expressions

---

## Mental Model

Operators wait until operands become available.

Example:

```text
2 3 +
```

Push:

- 2
- 3

Then:

- `+` consumes both

Stack models partial computation state.

---

# PART 3 — The Deep Unifying Principle

Almost every stack problem can be reframed as:

> “Some information is unresolved and must wait for future events.”

The stack stores those unresolved states.

That is the deep abstraction.

---

# PART 4 — Stack vs Other Patterns

This matters a lot for recognition speed.

---

# Stack vs Two Pointers

Two pointers:

- active simultaneous movement

Stack:

- deferred processing over time

---

# Stack vs Sliding Window

Sliding window:

- contiguous active region

Stack:

- historical unresolved elements

---

# Stack vs HashMap

HashMap:

- direct lookup

Stack:

- ordering and dependency resolution

---

# Stack vs Queue

Queue:

- oldest processed first

Stack:

- newest processed first

---

# PART 5 — The Most Important Stack Insight

The hardest part for beginners is this:

> “Why not just use loops?”

Because loops alone lose unresolved context.

The stack preserves:

- ordering
- dependency
- pending work

Without repeatedly rescanning.

That is why stacks reduce many O(n²) problems to O(n).

---

# PART 6 — SECTION 4 Pattern Map

Here is the conceptual map for this section.

---

# STACK PATTERN MAP

## 1. Basic Stack

### Purpose

Track nested/unresolved structure.

### Recognition

- matching
- balanced
- nesting

### Core Mechanism

push/pop matching states

---

## 2. Monotonic Stack

### Purpose

Nearest greater/smaller relationships.

### Recognition

- next greater
- previous smaller
- nearest larger

### Core Mechanism

maintain increasing/decreasing order

---

## 3. Simulation Stack

### Purpose

Process sequential interactions.

### Recognition

- collisions
- undo
- simplification

### Core Mechanism

recent unresolved state interacts first

---

## 4. Expression Stack

### Purpose

Evaluate deferred computations.

### Recognition

- operators
- parsing
- calculators

### Core Mechanism

operands accumulate until operator resolves

---

# PHASE 1 — PROBLEM SELECTION

Now we define the actual topic/tag coverage for SECTION 4.

---

# Exact LeetCode Tags / Topics

Use these when collecting candidate problems.

---

# Primary Tags

- Stack
- Monotonic Stack

---

# Secondary Tags

These often overlap with stack patterns:

- Design
- String
- Array
- Simulation
- Recursion

---

# Important Subcategories

---

## A. Basic Stack

Topics:

- parentheses
- validation
- stack design

Examples:

- Valid Parentheses
- Min Stack

---

## B. Monotonic Stack

Topics:

- next greater element
- previous smaller element
- histogram
- temperature/wait problems

Examples:

- Daily Temperatures
- Largest Rectangle in Histogram

---

## C. Stack Simulation

Topics:

- collisions
- path normalization
- undo behavior

Examples:

- Asteroid Collision
- Simplify Path

---

## D. Expression Evaluation

Topics:

- postfix
- calculators
- parsing

Examples:

- Evaluate Reverse Polish Notation
- Basic Calculator II

---

# Your Next Step (PHASE 1 — Step 2)

Now you should collect candidate problems using:

- LeetCode Stack tag
- LeetCode Monotonic Stack tag

Try to gather:

- easy
- medium
- a few hard

Do NOT curate yet.

Just gather candidates.

Once you send the candidate list, I will:

- remove low-ROI problems
- organize by pattern progression
- create gradual difficulty flow
- isolate core variations
- build the final SECTION 4 curriculum

This aligns perfectly with your mastery-based progression system.
