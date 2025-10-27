from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = count = 0
        for num in nums:
            if num != 1:
                count = 0
                continue
            count += 1
            longest = max(longest, count)
        return longest

'''
my approach:
------------
1. 
'''