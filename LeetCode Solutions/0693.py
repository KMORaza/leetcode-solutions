class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shifted_n = n >> 1
        xor_result = n ^ shifted_n
        return (xor_result & (xor_result + 1)) == 0
