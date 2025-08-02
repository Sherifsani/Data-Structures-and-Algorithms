class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        return prefix
            
'''
my approach:
1. if the array is empty just return an empty string
2. Iterate through the array from the second item ,(we use the first item as the initial prefix)
3. if the prefix is not equal to a the string (to the same length), the reduce the prefix by a character
4. return prefix if empty
'''