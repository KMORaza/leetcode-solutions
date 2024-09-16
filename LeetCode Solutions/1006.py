class Solution:
    def clumsy(self, n: int) -> int:
        precomputed = {1: 1, 2: 2, 3: 6, 4: 7}
        if n in precomputed:
            return precomputed[n]
        remainder = n % 4
        if remainder == 1 or remainder == 2:
            return n + 2
        elif remainder == 3:
            return n - 1
        else:
            return n + 1
