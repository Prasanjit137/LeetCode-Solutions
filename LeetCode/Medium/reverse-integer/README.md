# Reverse Integer

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/reverse-integer/)

## Problem Statement
Given a signed 32-bit integer `x`, return `x`*with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

```
Input: x = 123
Output: 321
```

**Example 2:**

```
Input: x = -123
Output: -321
```

**Example 3:**

```
Input: x = 120
Output: 21
```

**Constraints:**

- `-231 <= x <= 231 - 1`

## Solution Code
```python3
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = 1 if x >= 0 else -1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if (reversed_num > INT_MAX // 10) or \
               (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            reversed_num = reversed_num * 10 + digit
        reversed_num *= sign
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num
```
