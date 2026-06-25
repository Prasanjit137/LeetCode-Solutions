// String to Integer (atoi)
// Difficulty: Medium
// URL: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1

        result *= sign
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result