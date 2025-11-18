from typing import List

class Solution:
    #1. Mathematical Sum Approach
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        for i in nums:
            total-= i
        return total
    
    #2. XOR Approach
    