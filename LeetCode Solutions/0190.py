class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        for _ in range(32):
            reversed_bits <<= 1
            reversed_bits |= n & 1
            n >>= 1
        return reversed_bits
