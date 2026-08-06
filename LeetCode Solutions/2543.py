class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(targetX, targetY)

        return (g & (g - 1)) == 0