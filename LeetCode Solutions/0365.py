import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = gcd(x, y)
        return target % g == 0
