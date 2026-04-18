Perfect—Graph traversal is a core building block. Let’s implement **DFS** and **BFS** in clean, interview-ready C#.

---

# 🧠 Graph Representation

We’ll use an **adjacency list**:

```csharp
Dictionary<int, List<int>> graph;
```

Example:

```text
1 → [2,3]
2 → [4]
3 → []
4 → []
```

---

# 🔁 DFS (Depth-First Search)

## 💡 Idea

Go as deep as possible before backtracking.

---

## ✅ Recursive DFS

```csharp
using System;
using System.Collections.Generic;

public class GraphDFS
{
    public void DFS(Dictionary<int, List<int>> graph, int start)
    {
        var visited = new HashSet<int>();
        DFSHelper(start, graph, visited);
    }

    private void DFSHelper(int node, Dictionary<int, List<int>> graph, HashSet<int> visited)
    {
        if (visited.Contains(node))
            return;

        visited.Add(node);
        Console.WriteLine(node); // process node

        foreach (var neighbor in graph[node])
        {
            DFSHelper(neighbor, graph, visited);
        }
    }
}
```

---

## 🔁 Iterative DFS (Stack)

```csharp
public void DFSIterative(Dictionary<int, List<int>> graph, int start)
{
    var visited = new HashSet<int>();
    var stack = new Stack<int>();

    stack.Push(start);

    while (stack.Count > 0)
    {
        int node = stack.Pop();

        if (visited.Contains(node))
            continue;

        visited.Add(node);
        Console.WriteLine(node);

        foreach (var neighbor in graph[node])
        {
            stack.Push(neighbor);
        }
    }
}
```

---

# 🌊 BFS (Breadth-First Search)

## 💡 Idea

Explore level by level (closest nodes first)

---

## ✅ BFS Implementation

```csharp
using System;
using System.Collections.Generic;

public class GraphBFS
{
    public void BFS(Dictionary<int, List<int>> graph, int start)
    {
        var visited = new HashSet<int>();
        var queue = new Queue<int>();

        queue.Enqueue(start);
        visited.Add(start);

        while (queue.Count > 0)
        {
            int node = queue.Dequeue();
            Console.WriteLine(node); // process node

            foreach (var neighbor in graph[node])
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    queue.Enqueue(neighbor);
                }
            }
        }
    }
}
```

---

# 🔍 Example Usage

```csharp
var graph = new Dictionary<int, List<int>>
{
    {1, new List<int> {2, 3}},
    {2, new List<int> {4}},
    {3, new List<int> ()},
    {4, new List<int> ()}
};

var dfs = new GraphDFS();
dfs.DFS(graph, 1);

var bfs = new GraphBFS();
bfs.BFS(graph, 1);
```

---

# ⚡ Key Differences

| Feature   | DFS                  | BFS                        |
| --------- | -------------------- | -------------------------- |
| Structure | Stack / Recursion    | Queue                      |
| Traversal | Deep first           | Level by level             |
| Use cases | Backtracking, cycles | Shortest path (unweighted) |

---

# 🧠 Mental Model

* DFS:

```text
Go deep → backtrack
```

* BFS:

```text
Explore neighbors → then next layer
```

---

# 🚀 Interview Tips

* Always use:

```csharp
HashSet<int> visited
```

👉 Avoid infinite loops (cycles)

* BFS is used for:

    * Shortest path (unweighted)
    * Level-order traversal

* DFS is used for:

    * Backtracking
    * Cycle detection
    * Topological sort

---

If you want next step, we can:
👉 Apply DFS/BFS on **Grid problems (islands, flood fill)**
👉 Or move to **Cycle Detection / Topological Sort** (very important)
