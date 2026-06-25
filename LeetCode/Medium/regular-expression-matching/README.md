# Regular Expression Matching

**Difficulty:** Medium

**URL:** [LeetCode Problem](https://leetcode.com/problems/regular-expression-matching/)

## Problem Statement
Problem List
Debugging...
Submit
2
2Streaks
Extend Your Streak!
00:00:00
Prasanjit137
Access all features with our Premium subscription!
My Lists
Notebook
Progress
Points
Try New Features
Orders
My Playgrounds
Settings
Appearance
Sign Out
Premium
Description
Description
Accepted
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Testcase
Test Result
All Submissions
Accepted
354 / 354 testcases passed
Prasanjit137
submitted at Jun 25, 2026 22:39
Analysis
Solution
Runtime
5
ms
Beats
67.57%
Memory
20.35
MB
Beats
33.04%
49ms
1036ms
2024ms
3011ms
3999ms
4986ms
5974ms
6961ms
0%
50%
100%
49ms
1036ms
2024ms
3011ms
3999ms
4986ms
5974ms
6961ms
Code
Python3
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        memo = {}
4        def dfs(i, j):
5            if (i, j) in memo:
6                return memo[(i, j)]
7            if j == len(p):
8                return i == len(s)
9
10            first_match = (i < len(s) and (p[j] == '.' or p[j] == s[i]))
11
12            if j + 1 < len(p) and p[j+1] == '*':
13                # zero occurrences or one/more
14                res = (dfs(i, j+2) or (first_match and dfs(i+1, j)))
15            else:
16                res = first_match and dfs(i+1, j+1)
17
18            memo[(i, j)] = res
19            return res
20
21        return dfs(0, 0)
View more
0/5
Python3
Auto
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
class Solution:
def isMatch(self, s: str, p: str) -> bool:
memo = {}
def dfs(i, j):
if (i, j) in memo:
return memo[(i, j)]
if j == len(p):
return i == len(s)
first_match = (i < len(s) and (p[j] == '.' or p[j] == s[i]))
if j + 1 < len(p) and p[j+1] == '*':
# zero occurrences or one/more
res = (dfs(i, j+2) or (first_match and dfs(i+1, j)))
else:
res = first_match and dfs(i+1, j+1)
memo[(i, j)] = res
return res
Saved
Ln 1, Col 1
You must run your code first
🚀 Push to GitHub


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
