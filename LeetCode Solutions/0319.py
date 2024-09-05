import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n < 0:
            return 0
        return int(math.sqrt(n))