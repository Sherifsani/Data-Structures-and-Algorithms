class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_a = int(a, 2)
        bin_b = int(b, 2)
        return bin(bin_a + bin_b)[2:]