// Integer to Roman
// Difficulty: Medium
// Topic: Hash-Table
// URL: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = []
        for value, symbol in value_map:
            # While the current value can be subtracted from num
            while num >= value:
                num -= value
                result.append(symbol)
            if num == 0:
                break
        return "".join(result)