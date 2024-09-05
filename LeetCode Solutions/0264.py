class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        return n == 1
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        ugly_numbers = [1] * n
        i2 = i3 = i5 = 0
        next_ugly = 1
        for i in range(1, n):
            next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
            ugly_numbers[i] = next_ugly
            if next_ugly == ugly_numbers[i2] * 2:
                i2 += 1
            if next_ugly == ugly_numbers[i3] * 3:
                i3 += 1
            if next_ugly == ugly_numbers[i5] * 5:
                i5 += 1
        return ugly_numbers[-1]
