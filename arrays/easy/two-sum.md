# 1. Two Sum

**Difficulty**: Easy
**LeetCode Link**: https://leetcode.com/problems/two-sum/
**Pattern**: Arrays & Hash Tables
**Date Solved**: [To be filled when solved]

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

---

## Initial Thoughts

This is a classic problem that introduces the power of hash tables for optimization.

- What pattern does this remind me of? **Hash map for O(1) lookups**
- What are the key insights? We can check for the complement in constant time using a hash map
- What edge cases should I consider?
  - Duplicate numbers (but different indices)
  - Negative numbers
  - Zero in the array
  - The answer being at the start/end of array

---

## Approach 1: Brute Force

### Intuition
Check every possible pair of numbers to see if they sum to the target. For each number, iterate through the rest of the array to find its complement.

### Algorithm
1. Loop through each element `i` in the array
2. For each `i`, loop through elements from `i+1` to end
3. Check if `nums[i] + nums[j] == target`
4. If yes, return `[i, j]`

### Complexity Analysis
- **Time Complexity**: O(n²) - nested loops
- **Space Complexity**: O(1) - no extra space needed

### Code
```python
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Why This Doesn't Work / Can Be Improved
The nested loop gives us O(n²) time complexity. For large arrays (n = 10,000), this means 100 million operations. We're repeatedly searching for the complement, which is inefficient.

**Key bottleneck**: Linear search for the complement in the inner loop.

---

## Approach 2: Optimized Solution (Hash Map)

### Intuition
Instead of searching for the complement in O(n) time, we can use a hash map to store previously seen numbers and their indices. This allows us to check if the complement exists in O(1) time.

**Key insight**: For each number `num`, we need `target - num`. If we've seen it before, we found our pair!

### Algorithm
1. Create an empty hash map `seen` to store {value: index}
2. Iterate through the array with index `i` and value `num`
3. Calculate `complement = target - num`
4. If `complement` exists in `seen`, return `[seen[complement], i]`
5. Otherwise, store `num` in `seen` with its index
6. Continue to next element

### Complexity Analysis
- **Time Complexity**: O(n) - single pass through array, O(1) hash lookups
- **Space Complexity**: O(n) - hash map stores up to n elements

### Code
```python
def two_sum(nums, target):
    """
    Find two indices where nums[i] + nums[j] = target.

    Args:
        nums: List[int] - array of integers
        target: int - target sum

    Returns:
        List[int] - indices [i, j] where nums[i] + nums[j] = target
    """
    seen = {}  # value -> index mapping

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement exists in our hash map
        if complement in seen:
            return [seen[complement], i]

        # Store current number with its index
        seen[num] = i

    return []  # No solution found (shouldn't happen per constraints)
```

**Alternative Language (Java):**
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // HashMap to store value -> index
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // Check if complement exists
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }

            // Store current number with its index
            seen.put(nums[i], i);
        }

        return new int[] {}; // No solution
    }
}
```

---

## Edge Cases & Testing

### Edge Cases Considered
- [x] Duplicate numbers (e.g., [3,3], target=6)
- [x] Negative numbers (e.g., [-1,-2,-3,-4], target=-6)
- [x] Zero in array (e.g., [0,4,3,0], target=0)
- [x] Large numbers close to 10^9
- [x] Minimum array size (2 elements)
- [x] Answer at beginning vs end of array

### Test Cases
```python
def test_two_sum():
    # Test case 1: Normal case
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test case 2: Duplicates
    assert two_sum([3, 3], 6) == [0, 1]

    # Test case 3: Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Test case 4: Zero in array
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

    # Test case 5: Answer at end
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]

    print("All tests passed!")

test_two_sum()
```

---

## Key Takeaways

- **Pattern Recognition**: Hash map for O(1) complement lookup
- **Key Insight**: Trading space (O(n)) for time (O(n) instead of O(n²))
- **Common Pitfall**: Accidentally using the same element twice (prevented by checking `seen` before storing)
- **Similar Problems**:
  - 167. Two Sum II - Input Array Is Sorted
  - 15. 3Sum
  - 18. 4Sum
  - 454. 4Sum II

---

## Follow-up Questions

1. **What if the array is sorted?**
   - Use two-pointer approach: O(n) time, O(1) space
   - Better space complexity than hash map

2. **What if we need to find all pairs (not just one)?**
   - Continue iterating after finding a match
   - Store all valid pairs in a result list

3. **What if we can't use extra space?**
   - Sort array (O(n log n)) + two pointers (O(n)) = O(n log n) total
   - Or use brute force O(n²) with O(1) space

---

## Backend Engineering Context

**Real-world applications of this pattern:**

1. **Load Balancing**
   - Find two servers with combined capacity matching request load
   - Hash map tracks available capacity per server

2. **Cache Pair Queries**
   - Check if two resources together satisfy a requirement
   - Example: CDN edge servers with cached assets

3. **Database Query Optimization**
   - Hash join algorithm uses similar concept
   - Build hash table on smaller relation, probe with larger

4. **API Rate Limiting**
   - Track request pairs from same IP within time window
   - Hash map stores timestamps for quick lookups

5. **Microservices Communication**
   - Service discovery: find two services that together provide capability
   - Hash map of service endpoints with capabilities

---

## Revision Notes

**First Attempt**: [Date] - Initial solution, understood the pattern immediately
**Second Attempt**: [Date] - Focused on explaining the space-time tradeoff
**Third Attempt**: [Date] - Can code in under 2 minutes, pattern fully internalized

---

## Tags
`#arrays` `#hash-table` `#easy` `#two-sum` `#blind-75` `#must-know`
