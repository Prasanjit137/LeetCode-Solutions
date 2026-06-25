# Regular Expression Matching

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/regular-expression-matching/)

## Problem Statement
No description provided.

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
