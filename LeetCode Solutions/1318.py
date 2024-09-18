class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                if bit_a == 1:
                    flips += 1
                if bit_b == 1:
                    flips += 1
        return flips