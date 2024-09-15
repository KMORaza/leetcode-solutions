import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm_pq = (p * q) // math.gcd(p, q)
        m = lcm_pq // p
        n = lcm_pq // q
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2
        else:
            return -1