from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        sorted_count = dict(sorted(count.items(), key=lambda x : x[1], reverse=True))
        return list(sorted_count.keys())[:k]

class Second_Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        counter = Counter(nums)
        return [key[0] for key in list(counter.most_common(k))]
    
class Third_Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count:
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        