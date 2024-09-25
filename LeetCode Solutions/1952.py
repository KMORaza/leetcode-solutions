import math
class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        root = int(math.isqrt(n))
        if root * root == n:
            if root < 2:
                return False
            for i in range(2, int(math.sqrt(root)) + 1):
                if root % i == 0:
                    return False
            return True
        return False