class Solution:
    def lastRemaining(self, n: int) -> int:
        def largest_power_of_2(x):
            power = 1
            while power <= x:
                power <<= 1
            return power >> 1
        largest_power = largest_power_of_2(n)
        return 2 * (n - largest_power) + 1
