class Solution:
    def productExceptSelf(self, nums):
        product = 1
        res = []
        zero_count = 0
        for i in nums:
            if i == 0:  
                zero_count += 1
                continue
            product *= i
        for i in range(len(nums)):
            if zero_count == 0:
                res.append(product // nums[i])
            elif zero_count == 1:
                if nums[i] != 0:
                    res.append(0)
                    continue
                res.append(product)
            else:
                res.append(0)
        return res

class Solution_without_divison:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res