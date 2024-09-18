from typing import List
import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_divisors(n: int) -> List[int]:
            root = int(math.sqrt(n))
            for i in range(root, 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return []
        div1 = find_divisors(num + 1)
        div2 = find_divisors(num + 2)
        if abs(div1[0] - div1[1]) <= abs(div2[0] - div2[1]):
            return div1
        else:
            return div2
