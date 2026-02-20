# Trees & Binary Trees Pattern

**Total Problems**: 25 (estimated)
**Solved**: 0
**Mastery Level**: 0%

---

## Pattern Overview

Trees are hierarchical data structures with a root node and children forming a parent-child relationship. Binary trees (each node has at most 2 children) are the most common type in coding interviews.

Trees are fundamental to:
- Database indexes (B-trees, B+ trees)
- File systems (directory structure)
- Abstract syntax trees (compilers)
- DOM (web browsers)
- Decision trees (ML)

---

## Core Concepts

### 1. Tree Terminology
- **Root**: Top node with no parent
- **Leaf**: Node with no children
- **Height**: Longest path from node to leaf
- **Depth**: Distance from root to node
- **Balanced**: Height difference ≤ 1 (AVL, Red-Black)

### 2. Binary Search Tree (BST)
- Left subtree < node < Right subtree
- Enables O(log n) search, insert, delete (when balanced)
- Degenerates to O(n) if unbalanced

### 3. Tree Traversals
- **Inorder** (Left, Root, Right): Gives sorted order for BST
- **Preorder** (Root, Left, Right): Copy tree, prefix expressions
- **Postorder** (Left, Right, Root): Delete tree, postfix expressions
- **Level-order** (BFS): Level by level traversal

---

## Common Techniques

1. **Recursive DFS**
   - When to use: Most tree problems (natural fit for recursion)
   - Time: O(n) to visit all nodes
   - Space: O(h) for recursion stack (h = height)

2. **Iterative DFS with Stack**
   - When to use: Need to avoid recursion or track parent nodes
   - Time: O(n), Space: O(h)

3. **BFS with Queue (Level-order)**
   - When to use: Level-based problems, shortest path
   - Time: O(n), Space: O(w) where w = max width

4. **Tree Construction**
   - When to use: Build tree from traversals or other data
   - Technique: Use preorder/postorder with inorder

5. **Lowest Common Ancestor (LCA)**
   - When to use: Find common parent of two nodes
   - Technique: Bottom-up recursion or parent pointers

---

## Template Code

### Python: Tree Node Definition
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Python: Recursive DFS Template
```python
def dfs_recursive(root):
    """
    Recursive DFS traversal template.

    Time: O(n), Space: O(h) for recursion stack
    """
    # Base case: empty node
    if not root:
        return base_value

    # Process current node (preorder position)
    # ...

    # Recurse on children
    left_result = dfs_recursive(root.left)
    right_result = dfs_recursive(root.right)

    # Process current node (postorder position)
    # Combine results from children
    return combined_result
```

### Python: Iterative DFS with Stack
```python
def dfs_iterative(root):
    """
    Iterative DFS using explicit stack.

    Time: O(n), Space: O(h)
    """
    if not root:
        return base_value

    stack = [root]
    result = []

    while stack:
        node = stack.pop()

        # Process node
        result.append(node.val)

        # Add children (right first for left-to-right order)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### Python: BFS Template (Level-order)
```python
from collections import deque

def bfs_level_order(root):
    """
    Level-order traversal using queue.

    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### Python: BST Search Template
```python
def search_bst(root, target):
    """
    Search in Binary Search Tree.

    Time: O(h), Space: O(1) iterative or O(h) recursive
    """
    # Iterative approach
    current = root
    while current:
        if target == current.val:
            return current
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return None
```

---

## Problem List

### Easy
- [ ] [104. Maximum Depth of Binary Tree](easy/maximum-depth.md) - Basic recursion
- [ ] [100. Same Tree](easy/same-tree.md) - Tree comparison
- [ ] [226. Invert Binary Tree](easy/invert-tree.md) - Tree transformation
- [ ] [101. Symmetric Tree](easy/symmetric-tree.md) - Mirror comparison
- [ ] [108. Convert Sorted Array to BST](easy/sorted-array-to-bst.md) - BST construction

### Medium
- [ ] [98. Validate Binary Search Tree](medium/validate-bst.md) - BST property checking
- [ ] [236. Lowest Common Ancestor](medium/lowest-common-ancestor.md) - LCA pattern
- [ ] [102. Binary Tree Level Order Traversal](medium/level-order-traversal.md) - BFS
- [ ] [105. Construct Binary Tree from Preorder and Inorder](medium/construct-tree.md) - Tree construction
- [ ] [230. Kth Smallest Element in BST](medium/kth-smallest-bst.md) - Inorder traversal

### Hard
- [ ] [124. Binary Tree Maximum Path Sum](hard/max-path-sum.md) - Path problems
- [ ] [297. Serialize and Deserialize Binary Tree](hard/serialize-deserialize.md) - Tree encoding
- [ ] [273. Binary Tree Maximum Path Sum](hard/max-path-sum-ii.md) - Advanced path problems

---

## Key Insights

- **Recursion is natural**: Tree structure is inherently recursive
- **Choose traversal wisely**: Inorder for BST, level-order for levels, postorder for bottom-up
- **Track information up/down**: Pass data down via parameters, return data up via return values
- **BST property**: Inorder traversal gives sorted sequence
- **Height matters**: Balanced trees ensure O(log n) operations

---

## Common Pitfalls

1. **Null Pointer Issues**: Always check `if not root` first
2. **Wrong Traversal**: Using preorder when postorder is needed
3. **BST Violations**: Forgetting that BST property applies to entire subtrees, not just immediate children
4. **Off-by-One in Height**: Confusion between height and depth
5. **Missing Edge Cases**: Single node, empty tree, skewed tree

---

## Tree Problem Patterns

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Simple Recursion | Single path exploration | Max Depth, Count Nodes |
| Bottom-Up Recursion | Need info from children | Is Balanced, Diameter |
| Top-Down Recursion | Pass info from parent | Path Sum, Binary Tree Paths |
| Level-order BFS | Level-based logic | Right Side View, Zigzag |
| Inorder Traversal | BST problems, sorted output | Validate BST, Kth Smallest |
| Path Problems | Track path root-to-leaf | Path Sum, Sum Root to Leaf |
| Tree Construction | Build from traversals | Construct from Pre+In |
| Serialize/Deserialize | Tree encoding | Codec problems |

---

## Complexity Guide

| Operation | BST (Balanced) | BST (Skewed) | Binary Tree |
|-----------|----------------|--------------|-------------|
| Search | O(log n) | O(n) | O(n) |
| Insert | O(log n) | O(n) | - |
| Delete | O(log n) | O(n) | - |
| Traversal | O(n) | O(n) | O(n) |

**Space Complexity:**
- Recursive: O(h) for call stack
- Iterative: O(h) for stack/queue
- BFS: O(w) where w = max width

---

## Backend Engineering Applications

Trees are everywhere in backend systems:

**Real-world examples:**

1. **Database Indexing**
   - B-trees for range queries (MySQL, PostgreSQL)
   - B+ trees for efficient disk access
   - LSM trees for write-optimized storage (Cassandra, RocksDB)

2. **File Systems**
   - Directory structure is a tree
   - File path traversal uses tree algorithms
   - inode structures

3. **Routing & Load Balancing**
   - Trie for URL routing (prefix matching)
   - Decision trees for request routing
   - Hierarchical load balancing

4. **Parsing & Compilation**
   - Abstract Syntax Trees (AST)
   - Expression evaluation
   - JSON/XML parsing

5. **Distributed Systems**
   - Merkle trees for data verification (Git, Blockchain)
   - Segment trees for range queries
   - Fenwick trees for cumulative frequency

---

## Learning Path

1. **Master basics**: Max depth, invert tree, same tree
2. **Understand traversals**: Inorder, preorder, postorder, level-order
3. **Practice BST**: Validate, search, insert
4. **Learn LCA**: Lowest common ancestor pattern
5. **Advanced**: Serialize, path problems, tree DP

---

## Resources

- [LeetCode Tree Problems](https://leetcode.com/tag/tree/)
- [Visualgo Tree Visualizer](https://visualgo.net/en/bst)
- [Binary Tree Bootcamp](https://leetcode.com/explore/learn/card/data-structure-tree/)

---

## Progress Tracking

- **Started**: Not started
- **Last Problem Solved**: -
- **Target Completion**: TBD
- **Status**: Not Started
