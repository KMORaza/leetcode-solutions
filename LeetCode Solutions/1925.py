import math
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a * a + b * b
                c = int(math.sqrt(c_squared))
                if c * c == c_squared and c <= n:
                    count += 1
        return count
