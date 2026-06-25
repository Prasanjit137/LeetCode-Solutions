# Regular Expression Matching

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/regular-expression-matching/)

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Constraints:**

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

## Solution Code
```python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            
            first_match = (i < len(s) and (p[j] == '.' or p[j] == s[i]))
            
            if j + 1 < len(p) and p[j+1] == '*':
                # zero occurrences or one/more
                res = (dfs(i, j+2) or (first_match and dfs(i+1, j)))
            else:
                res = first_match and dfs(i+1, j+1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
```
