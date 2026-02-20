# Arrays & Hash Tables Pattern

**Total Problems**: 30 (estimated)
**Solved**: 0
**Mastery Level**: 0%

---

## Pattern Overview

Arrays are the most fundamental data structure, providing contiguous memory storage with O(1) random access. Combined with hash tables, they form the foundation for solving a wide range of algorithmic problems efficiently.

This pattern focuses on:
- Efficient array traversal and manipulation
- Using hash tables for O(1) lookups
- In-place modifications to optimize space
- Prefix sums and sliding windows
- Two-pointer techniques

---

## Core Concepts

### 1. Hash Tables for O(1) Lookup
Hash tables (dictionaries in Python, HashMap in Java) provide constant-time access, making them ideal for tracking seen elements, counting frequencies, or storing computed results.

### 2. Two Pointers
Use two pointers moving from opposite ends or same direction to reduce time complexity from O(n²) to O(n) in many problems.

### 3. Prefix Sums
Precompute cumulative sums to answer range queries in O(1) time after O(n) preprocessing.

### 4. In-Place Modifications
Modify arrays without using extra space by swapping elements or using array indices cleverly.

---

## Common Techniques

1. **Hash Map for Pair Finding**
   - When to use: Finding pairs/triplets with target sum
   - Time complexity: O(n)
   - Example: Two Sum, Three Sum

2. **Two Pointers (Opposite Direction)**
   - When to use: Sorted arrays, palindrome checking
   - Time complexity: O(n)
   - Example: Container With Most Water, Two Sum II

3. **Prefix Sum Array**
   - When to use: Range sum queries, subarray problems
   - Time complexity: O(n) preprocessing, O(1) query
   - Example: Subarray Sum Equals K

4. **Kadane's Algorithm**
   - When to use: Maximum subarray sum problems
   - Time complexity: O(n)
   - Example: Maximum Subarray

5. **In-Place Array Manipulation**
   - When to use: Space optimization required
   - Time complexity: O(n)
   - Example: Remove Duplicates, Move Zeroes

---

## Template Code

### Python: Hash Map for Pair Finding
```python
def two_sum(nums, target):
    """
    Find two numbers that add up to target.

    Time: O(n), Space: O(n)
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

### Python: Two Pointers
```python
def two_pointer_template(arr):
    """
    Template for two-pointer technique.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Process current pair
        if condition:
            # Move pointers based on condition
            left += 1
        else:
            right -= 1

    return result
```

### Python: Prefix Sum
```python
def prefix_sum_template(nums):
    """
    Build prefix sum array for range queries.

    Time: O(n), Space: O(n)
    """
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Range sum [i, j] = prefix[j + 1] - prefix[i]
    return prefix
```

---

## Problem List

### Easy
- [ ] [1. Two Sum](easy/two-sum.md) - Hash map for O(n) pair finding
- [ ] [121. Best Time to Buy and Sell Stock](easy/best-time-to-buy-stock.md) - Single pass tracking
- [ ] [217. Contains Duplicate](easy/contains-duplicate.md) - Hash set for duplicates
- [ ] [242. Valid Anagram](easy/valid-anagram.md) - Frequency counting
- [ ] [448. Find All Numbers Disappeared](easy/find-disappeared-numbers.md) - In-place marking

### Medium
- [ ] [238. Product of Array Except Self](medium/product-except-self.md) - Prefix/suffix products
- [ ] [15. 3Sum](medium/3sum.md) - Two pointers with sorting
- [ ] [11. Container With Most Water](medium/container-with-most-water.md) - Greedy two pointers
- [ ] [560. Subarray Sum Equals K](medium/subarray-sum-k.md) - Prefix sum with hash map
- [ ] [128. Longest Consecutive Sequence](medium/longest-consecutive.md) - Hash set for O(n)

### Hard
- [ ] [42. Trapping Rain Water](hard/trapping-rain-water.md) - Two pointers or stack
- [ ] [41. First Missing Positive](hard/first-missing-positive.md) - In-place marking
- [ ] [239. Sliding Window Maximum](hard/sliding-window-maximum.md) - Monotonic deque

---

## Key Insights

- **Hash tables trade space for time**: Convert O(n²) nested loops to O(n) with O(n) space
- **Two pointers work on sorted arrays**: Sort first if needed (O(n log n))
- **In-place algorithms reuse input array**: Use indices as markers or swap strategically
- **Prefix sums enable O(1) range queries**: Useful for cumulative operations

---

## Common Pitfalls

1. **Integer Overflow**: Be careful with large sums in prefix sum problems
2. **Hash Collisions**: While rare, understand that hash operations are amortized O(1)
3. **Modifying While Iterating**: Use separate pointers or iterate backwards when modifying
4. **Off-by-One Errors**: Carefully handle array boundaries with two pointers

---

## Complexity Analysis Guide

| Technique | Time Complexity | Space Complexity | When to Use |
|-----------|----------------|------------------|-------------|
| Hash Map Lookup | O(n) | O(n) | Need fast lookups, counting |
| Two Pointers | O(n) | O(1) | Sorted array, pair finding |
| Prefix Sum | O(n) | O(n) | Multiple range queries |
| Sorting + Two Pointers | O(n log n) | O(1) | Finding triplets, deduplication |

---

## Related Patterns

- **Sliding Window**: Fixed or variable window over arrays
- **Two Pointers**: Core technique for arrays
- **Hash Tables**: Complement to arrays for fast lookups
- **Dynamic Programming**: Often uses arrays for memoization

---

## Backend Engineering Applications

Arrays and hash tables are fundamental to backend systems:

**Real-world examples:**

1. **Caching & Memoization**
   - LRU cache uses hash map + doubly linked list
   - Redis stores key-value pairs (hash table)
   - Application-level caching for database queries

2. **Rate Limiting**
   - Track request counts per user (hash map)
   - Sliding window rate limiters
   - Token bucket algorithms

3. **Session Management**
   - Session ID → session data (hash table)
   - O(1) lookup for authentication

4. **Database Indexing**
   - Hash indexes for equality lookups
   - B-tree indexes use array-like structures
   - Covering indexes optimize query performance

5. **Load Balancing**
   - Consistent hashing (hash table + array)
   - Round-robin using circular arrays
   - Weighted distribution algorithms

---

## Resources

- [LeetCode Array Problems](https://leetcode.com/tag/array/)
- [Hash Table Problems](https://leetcode.com/tag/hash-table/)
- [NeetCode Arrays Playlist](https://neetcode.io/practice)

---

## Progress Tracking

- **Started**: Not started
- **Last Problem Solved**: -
- **Target Completion**: TBD
- **Status**: Not Started
