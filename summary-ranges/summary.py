from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
            res = []
            range_arr = []
            for num in nums:
                if range_arr and num - range_arr[-1] > 1:
                    if len(range_arr) > 1:
                        res.append(f"{range_arr[0]}->{range_arr[-1]}")
                    else:
                        res.append(f"{range_arr[0]}")
                    range_arr = []
                range_arr.append(num)
            if range_arr:
                if len(range_arr) > 1:
                    res.append(f"{range_arr[0]}->{range_arr[-1]}")
                else:
                    res.append(f"{range_arr[0]}")
            return res
    
'''
TODO: improve the solution later (probably using two pointers)
'''