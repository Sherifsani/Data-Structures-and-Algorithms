class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

'''
solution explained:
1. first, we create a set from the input list to handle duplicates and allow O(1) lookups.
2. Iterate the input array and check if the current number is the start of a sequence (n - 1)
3. If it is, we count the length of the sequence by checking for consecutive numbers (n, n + 1, n + 2, ...)
4. Update the longest sequence found.
5. Return the length of the longest consecutive sequence.
'''