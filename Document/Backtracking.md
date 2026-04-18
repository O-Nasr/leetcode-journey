# 🧠 A Clear & Simple Backtracking Recipe

Forget long theory. Use this **4-step loop every time**:

---

## ✅ Step 1: Define the GOAL

> What does a complete solution look like?

Examples:

* N-Queens → placed N queens
* Subsets → any combination
* Permutations → length == n

---

## ✅ Step 2: Define the STATE

> What do I carry while building the solution?

Examples:

* N-Queens → current `row` + board
* Subsets → current list
* Permutations → current list + used[]

---

## ✅ Step 3: Define CHOICES

> What can I try next?

Examples:

* N-Queens → choose a column
* Subsets → pick next number
* Permutations → pick unused number

---

## ✅ Step 4: Write the Pattern

Always this:

```csharp
void Backtrack(state)
{
    if (goal reached)
    {
        save result;
        return;
    }

    foreach (choice)
    {
        if (invalid) continue;   // ⭐ pruning

        make choice;

        Backtrack(new state);

        undo choice;
    }
}
```

👉 This is the **entire backtracking framework**

---

# 🔥 Now: What does “pruning reduces a LOT” mean?

This is VERY important.

---

## 🌳 Without pruning (bad)

Imagine N = 4:

At each row:

```text
4 choices → 4 choices → 4 choices → 4 choices
```

Total possibilities:

```text
4^4 = 256
```

👉 You explore **everything**, even invalid boards ❌

---

## ✂️ With pruning (good)

You stop early:

```csharp
if (column used OR diagonal used)
    continue;
```

Now:

* Many branches die early
* You don’t go deeper into invalid paths

---

## 🔍 Example (visual)

### Without pruning:

```text
Row 0 → col 0
    Row 1 → col 0 ❌ (same column)
        Row 2 → ...
        Row 3 → ...
```

👉 You waste time exploring garbage

---

### With pruning:

```text
Row 0 → col 0
    Row 1 → col 0 ❌ → STOP immediately
```

👉 Whole subtree is skipped

---

# 💥 Why this is HUGE

Because pruning cuts entire subtrees.

---

## 🌳 Think in tree size

Without pruning:

```text
Huge tree (explore everything)
```

With pruning:

```text
Small tree (only valid paths)
```

---

## 🔢 Real impact (intuition)

For N-Queens:

* Theoretical: `O(N!)`
* With pruning: **much smaller in practice**

Because:

* Most placements are invalid early

---

# 🧠 Key Insight

> Pruning = “Don’t go deeper if this path is already wrong”

---

# 🔥 Another Example (Super Clear)

## Problem: Sum to target = 7

Numbers: `[2, 3, 6, 7]`

---

### ❌ Without pruning

```text
Try all combinations → even sum = 50 😩
```

---

### ✂️ With pruning

```csharp
if (currentSum > target)
    return;
```

---

### Effect:

```text
2 + 3 + 6 = 11 ❌ → STOP immediately
```

👉 You skip EVERYTHING after that

---

# 🧩 Final Mental Model

## Backtracking:

```text
Explore all paths
```

## Pruning:

```text
Cut bad paths early
```

---

# 💡 One-liner to remember

> Backtracking explores the tree, pruning shrinks the tree.

---

# 🚀 Even simpler rule (use this in interviews)

Whenever you write:

```csharp
if (invalid) continue;
```

👉 You are pruning

---

If you want next level clarity, I can:

* Show you **before vs after pruning tree sizes visually**
* Or give you **3 patterns of pruning used in interviews** (very powerful)
