class Solution:
    def countBits(self, n: int):
        count_ones = [0] * (n + 1)
        for i in range(1, n + 1):
            count_ones[i] = count_ones[i >> 1] + (i & 1)
        return count_ones