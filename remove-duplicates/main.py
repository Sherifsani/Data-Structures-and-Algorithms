class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = i + 1
        k = 0

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i+=1
                k+=1
            j+=1
            
        return k + 1
                
        