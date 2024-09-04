class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power_of_5 = 5
        while n >= power_of_5:
            count += n // power_of_5
            power_of_5 *= 5
        return count