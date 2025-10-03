class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            is_match = True
            for k in range(len(needle)):
                if haystack[k+i] != needle[k]:
                    is_match = False
            if is_match:
                return i
        return -1

