class Solution:
    def romanToInt(self, s: str) -> int:
        keys = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        int = 0
        for i in range(len(s)-1, -1, -1):
            if i < len(s) - 1 and keys.get(s[i]) < keys.get(s[i+1]):
                int = int - keys.get(s[i])
            else:
                int += keys.get(s[i])
        return int

# How I solved this problem:
    
# 1. I created a dictionary to map Roman numerals to their integer values.
# 2. I created a variable `int` to store the total integer value.
# 3. Iterate through the str in a reverse order because roman numerals are usually written from largest to smallest.
# 4. If the current numeral is less than the next numeral, subtract its value from the total.
# 5. Otherwise, add its value to the total.
# 6. Return the total integer value.