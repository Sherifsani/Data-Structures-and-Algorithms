class Solution:
    def encode(strs):
        res = ""
        for s in strs:
            res += str(len(s)) +"#" + s
        return res
    
    def decode(str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1: length + j + 1])
            i = 1 + j + length
        return res
