# Longest Palindromic Substring

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem Statement
Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Solution Code
```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - left - 1

        for i in range(len(s)):
            l1, len1 = expand_around_center(i, i)
            l2, len2 = expand_around_center(i, i + 1)
            if len1 > max_len:
                start = l1
                max_len = len1
            if len2 > max_len:
                start = l2
                max_len = len2

        return s[start:start + max_len]
```
