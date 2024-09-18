class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_result = 0
        for i in range(n):
            xor_result ^= start + 2 * i
        return xor_result
