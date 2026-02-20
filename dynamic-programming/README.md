# Dynamic Programming Pattern

**Total Problems**: 25 (estimated)
**Solved**: 0
**Mastery Level**: 0%

---

## Pattern Overview

Dynamic Programming (DP) is an optimization technique that solves complex problems by breaking them into simpler overlapping subproblems. It's one of the most powerful patterns for optimization problems.

**Key Principle**: Store solutions to subproblems to avoid redundant computation.

This pattern is essential for:
- Optimization problems (min/max)
- Counting problems (how many ways)
- Decision problems (is it possible)
- Sequence problems (longest, shortest)

---

## Core Concepts

### 1. Overlapping Subproblems
The same subproblem is solved multiple times. DP stores these solutions to avoid recomputation.

Example: Fibonacci - fib(5) = fib(4) + fib(3), both of which compute fib(2).

### 2. Optimal Substructure
An optimal solution can be constructed from optimal solutions of its subproblems.

Example: Shortest path - the shortest path from A to C through B must use the shortest path from A to B.

### 3. Memoization vs Tabulation
- **Memoization (Top-Down)**: Recursion + caching
- **Tabulation (Bottom-Up)**: Iterative, fills table from base cases

---

## Common Techniques

1. **1D DP Array**
   - When to use: Problems with single dimension (sequence, single array)
   - Space: O(n), can often optimize to O(1)
   - Example: House Robber, Climbing Stairs

2. **2D DP Array**
   - When to use: Two sequences, grid problems, knapsack variants
   - Space: O(n*m), sometimes optimizable to O(n) or O(m)
   - Example: Longest Common Subsequence, Edit Distance

3. **State Machine DP**
   - When to use: Problems with distinct states and transitions
   - Example: Stock trading with cooldown, Paint House

4. **Knapsack Pattern**
   - When to use: Optimization with constraints (weight, capacity)
   - Types: 0/1 knapsack, unbounded knapsack, bounded knapsack
   - Example: Coin Change, Partition Equal Subset Sum

---

## DP Framework

### Step 1: Identify if it's a DP Problem
Ask yourself:
- Is there an optimal solution or count?
- Can the problem be broken into subproblems?
- Do subproblems overlap?
- Does the problem have optimal substructure?

### Step 2: Define the State
- What variables change between subproblems?
- What's the meaning of dp[i] or dp[i][j]?

### Step 3: Write the Recurrence Relation
- How do you compute dp[i] from previous states?
- What are the base cases?

### Step 4: Determine Computation Order
- Bottom-up: What order fills the table correctly?
- Top-down: Use recursion with memoization

### Step 5: Optimize Space (Optional)
- Can you use O(1) space instead of O(n)?
- Rolling array technique

---

## Template Code

### Python: Top-Down (Memoization)
```python
def dp_top_down(n):
    """
    Top-down DP with memoization.

    Time: O(n), Space: O(n) for recursion stack + memo
    """
    memo = {}

    def dp(i):
        # Base case
        if i <= 0:
            return base_value

        # Check memo
        if i in memo:
            return memo[i]

        # Recurrence relation
        memo[i] = some_function(dp(i-1), dp(i-2), ...)

        return memo[i]

    return dp(n)
```

### Python: Bottom-Up (Tabulation)
```python
def dp_bottom_up(n):
    """
    Bottom-up DP with tabulation.

    Time: O(n), Space: O(n), can optimize to O(1)
    """
    if n <= 0:
        return base_value

    # Initialize DP table
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = base_value_0
    dp[1] = base_value_1

    # Fill table using recurrence relation
    for i in range(2, n + 1):
        dp[i] = some_function(dp[i-1], dp[i-2], ...)

    return dp[n]
```

### Python: Space-Optimized
```python
def dp_space_optimized(n):
    """
    Space-optimized DP using rolling variables.

    Time: O(n), Space: O(1)
    """
    if n <= 0:
        return base_value

    # Only keep last few states
    prev2 = base_value_0
    prev1 = base_value_1

    for i in range(2, n + 1):
        current = some_function(prev1, prev2, ...)
        prev2 = prev1
        prev1 = current

    return prev1
```

---

## Problem List

### Easy
- [ ] [70. Climbing Stairs](easy/climbing-stairs.md) - Basic 1D DP
- [ ] [198. House Robber](easy/house-robber.md) - State machine DP
- [ ] [53. Maximum Subarray](easy/maximum-subarray.md) - Kadane's algorithm
- [ ] [746. Min Cost Climbing Stairs](easy/min-cost-climbing-stairs.md) - Decision DP

### Medium
- [ ] [322. Coin Change](medium/coin-change.md) - Unbounded knapsack
- [ ] [300. Longest Increasing Subsequence](medium/longest-increasing-subsequence.md) - Classic LIS
- [ ] [139. Word Break](medium/word-break.md) - String DP
- [ ] [518. Coin Change II](medium/coin-change-ii.md) - Counting DP
- [ ] [416. Partition Equal Subset Sum](medium/partition-equal-subset-sum.md) - 0/1 knapsack

### Hard
- [ ] [72. Edit Distance](hard/edit-distance.md) - 2D DP classic
- [ ] [10. Regular Expression Matching](hard/regular-expression-matching.md) - Complex 2D DP
- [ ] [312. Burst Balloons](hard/burst-balloons.md) - Interval DP
- [ ] [1000. Minimum Cost to Merge Stones](hard/merge-stones.md) - Advanced DP

---

## Key Insights

- **Recognize the pattern**: If brute force is exponential (2^n, n!), try DP
- **Define state carefully**: The state definition determines the entire solution
- **Base cases matter**: Initialize correctly or the entire solution fails
- **Space optimization is common**: Many 2D DPs can become 1D
- **Top-down is easier to write**: Bottom-up is often faster

---

## Common Pitfalls

1. **Wrong State Definition**: The state doesn't capture all necessary information
2. **Incorrect Base Cases**: Off-by-one errors or missing edge cases
3. **Wrong Iteration Order**: In bottom-up, must compute dependencies first
4. **Space Inefficiency**: Not recognizing when space can be optimized
5. **Premature Optimization**: Start with readable solution, optimize later

---

## DP Problem Types

| Type | Description | Example |
|------|-------------|---------|
| Linear DP | 1D sequence, dp[i] depends on previous elements | Climbing Stairs, House Robber |
| Grid DP | 2D grid, dp[i][j] from adjacent cells | Unique Paths, Minimum Path Sum |
| Subsequence DP | Matching/comparing sequences | LIS, LCS, Edit Distance |
| Knapsack DP | Optimization with capacity constraint | Coin Change, Subset Sum |
| Interval DP | Problems on ranges [i, j] | Burst Balloons, Matrix Chain |
| State Machine DP | Distinct states with transitions | Stock Trading, Paint House |
| Digit DP | Counting numbers with properties | Numbers at Most N Given Digit Set |

---

## Complexity Patterns

| DP Type | Time | Space | Optimization Possible? |
|---------|------|-------|------------------------|
| 1D Linear | O(n) | O(n) | Yes → O(1) |
| 2D Linear | O(n*m) | O(n*m) | Yes → O(min(n,m)) |
| Subsequence | O(n²) | O(n²) | Sometimes → O(n) |
| Knapsack | O(n*W) | O(n*W) | Yes → O(W) |

---

## Backend Engineering Applications

DP patterns are crucial for backend optimization:

**Real-world examples:**

1. **Resource Allocation**
   - Optimal server allocation for requests
   - Memory/CPU distribution across services
   - Database connection pool sizing

2. **Query Optimization**
   - Join ordering in SQL queries
   - Query plan selection
   - Index selection strategies

3. **Caching Strategies**
   - Least Frequently Used (LFU) cache
   - Optimal page replacement
   - Multi-level cache hierarchies

4. **Rate Limiting**
   - Token bucket algorithm
   - Sliding window rate limits
   - Quota management

5. **Job Scheduling**
   - Task scheduling with dependencies
   - Batch processing optimization
   - Pipeline parallelization

---

## Learning Path

1. **Start Simple**: Fibonacci, Climbing Stairs
2. **Learn 1D DP**: House Robber, Coin Change
3. **Master 2D DP**: Unique Paths, LCS
4. **Advanced Patterns**: State machines, interval DP
5. **Optimize**: Practice space optimization

---

## Resources

- [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)
- [DP Patterns by AlgoExpert](https://www.algoexpert.io/)
- [MIT OCW - Dynamic Programming](https://ocw.mit.edu/courses/introduction-to-algorithms/)

---

## Progress Tracking

- **Started**: Not started
- **Last Problem Solved**: -
- **Target Completion**: TBD
- **Status**: Not Started
