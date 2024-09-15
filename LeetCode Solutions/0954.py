from collections import Counter
from typing import List
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True
