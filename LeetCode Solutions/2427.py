class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        import math
        gcd_val = math.gcd(a, b)
        count = 0
        for i in range(1, int(gcd_val**0.5) + 1):
            if gcd_val % i == 0:
                if i * i == gcd_val:
                    count += 1
                else:
                    count += 2
        return count