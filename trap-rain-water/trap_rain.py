from typing import List

class Solution:

    #solution 1: 2 pointer
    def trap_1(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = 0
        maxLeft = height[left]
        maxRight = height[right]
        res = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
        return res
    
    #solution 2: prefix
    def trap_2(self, height: List[int]) -> int:
        if not height:
            return 0

        maxPrefix = []
        temp = 0
        for i in range(len(height)):
            temp = max(temp, height[i])
            maxPrefix.append(temp)
        
        temp = 0
        maxSuffix = []
        for i in range(len(height)-1,-1,-1):
            temp = max(temp, height[i])
            maxSuffix.append(temp)
        res = 0
        for i in range(len(height)):
            res += min(maxSuffix[i], maxPrefix[i]) - height[i]
        return res

