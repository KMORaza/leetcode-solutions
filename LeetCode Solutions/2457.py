class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        original_n = n
        power = 1

        while digit_sum(n) > target:
            rounding_base = 10 ** power
            next_rounded = ((n // rounding_base) + 1) * rounding_base
            n = next_rounded
            power += 1

        return n - original_n