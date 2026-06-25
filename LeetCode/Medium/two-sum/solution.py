// Two Sum
// Difficulty: Medium
// URL: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the required complement to reach the target
            complement = target - num
            
            # If the complement is already in our map, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the current number and its index in the map
            num_to_index[num] = index