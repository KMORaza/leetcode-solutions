import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        def lcm(x: int, y: int) -> int:
            return (x * y) // math.gcd(x, y)
        def count_magical_up_to(x: int) -> int:
            return (x // a) + (x // b) - (x // lcm(a, b))
        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if count_magical_up_to(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left % MOD
