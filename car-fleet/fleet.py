from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack .append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
'''
my approach
-----------
1. create pairs of position and speed to simplify the process and reduce loops
2. use a stack to store the fleets(time)
3. sort the pairs and then loop through them in reverse order
4. calculate the time taken for each car to reach the target and push it onto the stack
5. if the current car's time is greater than the previous car's time, pop from the stack
6. return the length of the stack as the number of fleets
'''