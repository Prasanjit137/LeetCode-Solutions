# Median of Two Sorted Arrays

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

## Solution Code
```python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2 

        low, high = 0, m
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = total_left - cut1
            left1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < m else float('inf')
            left2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        raise ValueError("Input arrays are not sorted or invalid.")
```
