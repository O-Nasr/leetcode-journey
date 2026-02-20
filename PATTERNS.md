# Algorithmic Patterns Guide 🧩

This document catalogs all patterns covered in this repository, with explanations and problem mappings.

## Table of Contents
1. [Arrays & Hash Tables](#1-arrays--hash-tables)
2. [Strings](#2-strings)
3. [Linked Lists](#3-linked-lists)
4. [Trees & Binary Trees](#4-trees--binary-trees)
5. [Graphs](#5-graphs)
6. [Dynamic Programming](#6-dynamic-programming)
7. [Backtracking](#7-backtracking)
8. [Binary Search](#8-binary-search)
9. [Heaps / Priority Queues](#9-heaps--priority-queues)
10. [Sliding Window](#10-sliding-window)
11. [Stack & Queue](#11-stack--queue)
12. [Two Pointers](#12-two-pointers)
13. [Hash Tables](#13-hash-tables)

---

## 1. Arrays & Hash Tables

**Description**: Fundamental data structure operations including traversal, manipulation, and hash-based lookups.

**Key Techniques**:
- Prefix sums
- Two pointers
- Hash map for O(1) lookups
- In-place modifications
- Kadane's algorithm

**Common Problem Types**:
- Finding pairs/triplets with target sum
- Subarray problems
- Array transformations
- Frequency counting

**Problems**: [View Array Problems](arrays/)

---

## 2. Strings

**Description**: String manipulation, pattern matching, and text processing.

**Key Techniques**:
- Two pointers
- Sliding window
- String hashing
- Character frequency maps
- String builder pattern

**Common Problem Types**:
- Palindrome detection
- Anagram grouping
- Substring search
- String transformations

**Problems**: [View String Problems](strings/)

---

## 3. Linked Lists

**Description**: Pointer manipulation in linked data structures.

**Key Techniques**:
- Fast & slow pointers (Floyd's cycle detection)
- Dummy nodes
- In-place reversal
- Two-pointer traversal
- Recursive approaches

**Common Problem Types**:
- Reversal
- Cycle detection
- Merging lists
- Finding middle/nth node

**Problems**: [View Linked List Problems](linked-lists/)

---

## 4. Trees & Binary Trees

**Description**: Hierarchical data structure traversal and manipulation.

**Key Techniques**:
- DFS (Inorder, Preorder, Postorder)
- BFS (Level-order traversal)
- Recursion
- Parent pointers
- Balanced tree properties

**Common Problem Types**:
- Tree traversal
- Path problems
- Tree construction
- BST operations
- Tree validation

**Problems**: [View Tree Problems](trees/)

---

## 5. Graphs

**Description**: Graph traversal, path finding, and connectivity problems.

**Key Techniques**:
- DFS (Depth-First Search)
- BFS (Breadth-First Search)
- Topological sort
- Union-Find (Disjoint Set)
- Dijkstra's algorithm
- Cycle detection

**Common Problem Types**:
- Connected components
- Shortest path
- Cycle detection
- Topological ordering
- Graph coloring

**Problems**: [View Graph Problems](graphs/)

---

## 6. Dynamic Programming

**Description**: Optimization problems solved by breaking into overlapping subproblems.

**Key Techniques**:
- Memoization (Top-down)
- Tabulation (Bottom-up)
- State machines
- Space optimization
- Problem reduction

**Common Problem Types**:
- Knapsack variants
- Sequence problems (LIS, LCS)
- Path counting
- Optimization problems
- String matching

**Problems**: [View DP Problems](dynamic-programming/)

---

## 7. Backtracking

**Description**: Systematic exploration of all possible solutions with pruning.

**Key Techniques**:
- Recursive exploration
- State management
- Pruning
- Constraint satisfaction
- Choice/explore/unchoose pattern

**Common Problem Types**:
- Permutations & combinations
- Subset generation
- Constraint satisfaction (N-Queens, Sudoku)
- Path finding with constraints

**Problems**: [View Backtracking Problems](backtracking/)

---

## 8. Binary Search

**Description**: Efficient search in sorted or monotonic search spaces.

**Key Techniques**:
- Standard binary search
- Search space reduction
- Finding boundaries
- Binary search on answer
- Rotated array search

**Common Problem Types**:
- Find target in sorted array
- Find first/last occurrence
- Search in rotated array
- Minimize/maximize with constraints

**Problems**: [View Binary Search Problems](binary-search/)

---

## 9. Heaps / Priority Queues

**Description**: Maintaining sorted order with efficient insertions.

**Key Techniques**:
- Min heap / Max heap
- K-way merge
- Top K elements
- Heap sort
- Running median

**Common Problem Types**:
- Top K elements
- Merge K sorted lists
- Scheduling problems
- Streaming data problems

**Problems**: [View Heap Problems](heaps/)

---

## 10. Sliding Window

**Description**: Optimize subarray/substring problems using a moving window.

**Key Techniques**:
- Fixed-size window
- Dynamic-size window
- Two pointers
- Hash map for character tracking
- Window expansion/contraction

**Common Problem Types**:
- Maximum/minimum in subarrays
- Longest substring with constraints
- Subarray sum problems
- Anagram problems

**Problems**: [View Sliding Window Problems](sliding-window/)

---

## 11. Stack & Queue

**Description**: LIFO and FIFO data structure applications.

**Key Techniques**:
- Monotonic stack
- Stack for validation
- Queue for BFS
- Deque for sliding window
- Stack for recursion simulation

**Common Problem Types**:
- Parentheses validation
- Next greater element
- Expression evaluation
- Level-order traversal

**Problems**: [View Stack & Queue Problems](stack-queue/)

---

## 12. Two Pointers

**Description**: Use two pointers to reduce time complexity in array/list problems.

**Key Techniques**:
- Opposite direction pointers
- Same direction pointers
- Fast & slow pointers
- Partition technique

**Common Problem Types**:
- Pair finding
- Palindrome checking
- Partitioning
- Removing duplicates

**Problems**: [View Two Pointers Problems](two-pointers/)

---

## 13. Hash Tables

**Description**: O(1) lookup for counting, grouping, and detection.

**Key Techniques**:
- Frequency counting
- Grouping elements
- Fast lookups
- Hash functions
- Collision handling

**Common Problem Types**:
- Duplicate detection
- Grouping anagrams
- Two sum variants
- Frequency analysis

**Problems**: [View Hash Table Problems](hash-tables/)

---

## Pattern Selection Guide

When approaching a new problem:

1. **Read carefully** - Identify input/output types and constraints
2. **Identify the pattern** - Does it involve:
   - Pairs/triplets? → Two Pointers or Hash Tables
   - Subarrays/substrings? → Sliding Window or Prefix Sums
   - Paths in trees/graphs? → DFS/BFS
   - Optimal solution? → Dynamic Programming
   - All possibilities? → Backtracking
   - Sorted data? → Binary Search
   - K-th element? → Heaps
3. **Start simple** - Brute force first, then optimize
4. **Draw examples** - Visualize the pattern
5. **Code & test** - Implement and verify with edge cases

---

## Backend Engineering Relevance

Many LeetCode patterns directly apply to backend systems:

- **Hash Tables**: Caching, rate limiting, session management
- **Trees**: Database indexes (B-trees), routing tables
- **Graphs**: Service dependency graphs, distributed tracing
- **Dynamic Programming**: Resource optimization, query optimization
- **Heaps**: Job scheduling, task prioritization
- **Sliding Window**: Log analysis, metrics aggregation
- **Binary Search**: Database queries, version resolution

Understanding these patterns improves system design, debugging, and optimization skills.
