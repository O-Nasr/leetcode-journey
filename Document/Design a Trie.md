Perfect—this is a classic and very important implementation. I’ll give you a **clean, production-quality C# Trie** with:

* `Insert`
* `Search`
* `StartsWith`

Then I’ll briefly explain key parts like an engineer would.

---

# ✅ Full C# Implementation — Design a Trie

```csharp
using System;
using System.Collections.Generic;

public class TrieNode
{
    public Dictionary<char, TrieNode> Children;
    public bool IsWord;

    public TrieNode()
    {
        Children = new Dictionary<char, TrieNode>();
        IsWord = false;
    }
}

public class Trie
{
    private readonly TrieNode root;

    public Trie()
    {
        root = new TrieNode();
    }

    // Insert a word into the trie
    public void Insert(string word)
    {
        TrieNode node = root;

        foreach (char c in word)
        {
            if (!node.Children.ContainsKey(c))
            {
                node.Children[c] = new TrieNode();
            }

            node = node.Children[c];
        }

        node.IsWord = true;
    }

    // Returns true if the word exists in the trie
    public bool Search(string word)
    {
        TrieNode node = Traverse(word);
        return node != null && node.IsWord;
    }

    // Returns true if there is any word in the trie that starts with the given prefix
    public bool StartsWith(string prefix)
    {
        return Traverse(prefix) != null;
    }

    // Helper function to walk through the trie
    private TrieNode Traverse(string str)
    {
        TrieNode node = root;

        foreach (char c in str)
        {
            if (!node.Children.ContainsKey(c))
            {
                return null;
            }

            node = node.Children[c];
        }

        return node;
    }
}
```

---

# 🧪 Example Usage

```csharp
public class Program
{
    public static void Main()
    {
        Trie trie = new Trie();

        trie.Insert("apple");

        Console.WriteLine(trie.Search("apple"));   // true
        Console.WriteLine(trie.Search("app"));     // false
        Console.WriteLine(trie.StartsWith("app")); // true

        trie.Insert("app");
        Console.WriteLine(trie.Search("app"));     // true
    }
}
```

---

# 🧠 Engineering Breakdown

## 1️⃣ Why `Traverse` helper?

Instead of duplicating logic:

```csharp
Search()
StartsWith()
```

We centralize traversal:

```csharp
private TrieNode Traverse(string str)
```

👉 Clean
👉 Reusable
👉 Less bugs

---

## 2️⃣ Key invariant

At any point:

```csharp
node = node.Children[c];
```

means:

> “Move to the node representing prefix so far”

---

## 3️⃣ Time Complexity

| Operation  | Complexity |
| ---------- | ---------- |
| Insert     | O(n)       |
| Search     | O(n)       |
| StartsWith | O(n)       |

`n = length of word`

---

## 4️⃣ Why Dictionary here?

As we discussed:

```csharp
Dictionary<char, TrieNode>
```

✔ Flexible
✔ Memory-efficient for sparse nodes
✔ Clean code

---

# 🔥 Interview Tips (important)

### Common follow-ups:

1. Replace Dictionary with array (optimize speed)
2. Add delete operation
3. Count words with prefix
4. Return all words with prefix (autocomplete)

---

# 🚀 Optional: Optimized Version (Array)

If interviewer pushes performance:

```csharp
public class TrieNode
{
    public TrieNode[] Children = new TrieNode[26];
    public bool IsWord;
}
```

---

# 🧩 Final takeaway

This implementation is:

* ✅ Clean
* ✅ Scalable
* ✅ Interview-ready

---

--------------------------------------------------------------

Great question—this is where Trie gets **really interesting** and closer to real interview problems.

When you introduce **wildcards like `.`**, normal Trie search is not enough anymore.

---

# 🧠 Problem Understanding

Wildcard:

```text
'.' = matches ANY single character
```

Examples:

```text
"b.." → matches: bad, bag, bat
".an" → matches: ban, can, fan
```

---

# ❗ Why normal search fails

Normal search:

```csharp
node = node.Children[c];
```

But with `.`:

👉 You **don’t know which child to go to**
👉 You must try **ALL possible children**

---

# 💡 Solution: DFS / Backtracking on Trie

Instead of one path, we explore **multiple paths**.

---

# ✅ Full C# Implementation (with wildcard search)

This is a classic design called **WordDictionary**

```csharp
using System;
using System.Collections.Generic;

public class TrieNode
{
    public Dictionary<char, TrieNode> Children = new Dictionary<char, TrieNode>();
    public bool IsWord = false;
}

public class WordDictionary
{
    private readonly TrieNode root;

    public WordDictionary()
    {
        root = new TrieNode();
    }

    public void AddWord(string word)
    {
        TrieNode node = root;

        foreach (char c in word)
        {
            if (!node.Children.ContainsKey(c))
            {
                node.Children[c] = new TrieNode();
            }

            node = node.Children[c];
        }

        node.IsWord = true;
    }

    public bool Search(string word)
    {
        return DFS(word, 0, root);
    }

    private bool DFS(string word, int index, TrieNode node)
    {
        // reached end of pattern
        if (index == word.Length)
        {
            return node.IsWord;
        }

        char c = word[index];

        // Case 1: normal character
        if (c != '.')
        {
            if (!node.Children.ContainsKey(c))
                return false;

            return DFS(word, index + 1, node.Children[c]);
        }

        // Case 2: wildcard '.'
        foreach (var child in node.Children.Values)
        {
            if (DFS(word, index + 1, child))
                return true;
        }

        return false;
    }
}
```

---

# 🧪 Example Usage

```csharp
var dict = new WordDictionary();

dict.AddWord("bad");
dict.AddWord("dad");
dict.AddWord("mad");

Console.WriteLine(dict.Search("pad")); // false
Console.WriteLine(dict.Search("bad")); // true
Console.WriteLine(dict.Search(".ad")); // true
Console.WriteLine(dict.Search("b..")); // true
```

---

# 🔍 Step-by-step intuition

## Example: `"b.."`

```text
Step 1: 'b' → go to 'b' node
Step 2: '.' → try ALL children
Step 3: '.' → again try ALL children
Step 4: check IsWord
```

---

## Example: `".an"`

```text
Step 1: '.' → try all root children (b, c, f...)
Step 2: 'a' → filter paths
Step 3: 'n' → check match
```

---

# ⚡ Complexity

Let:

* `n = word length`
* `k = branching factor (children count)`

Worst case:

```text
O(k^n)
```

👉 But in practice, much faster because:

* Trie limits branching
* Early pruning happens

---

# 🔥 Key Insight (important)

When you see:

```text
“multiple possibilities”
```

👉 Think:

> **Backtracking / DFS**

---

# 🧩 Mental Model

* Normal Trie → **single path**
* Wildcard Trie → **tree exploration**

---

# 🚀 Interview Tip

This exact pattern appears in:

* “Design Add and Search Words Data Structure” (LeetCode)
* Regex-like matching problems
* Search engines / autocomplete with patterns

---

# 💡 Final takeaway

* `.` turns your Trie from **deterministic → branching**
* You must:

    * Explore all children
    * Stop early when match is found

---
