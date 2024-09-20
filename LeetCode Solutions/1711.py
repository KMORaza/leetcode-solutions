from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)
        total_pairs = 0
        for x in count:
            for power in range(22):
                target = (1 << power) - x
                if target in count:
                    if target == x:
                        total_pairs += count[x] * (count[x] - 1) // 2
                    elif target > x:
                        total_pairs += count[x] * count[target]
        return total_pairs % (10**9 + 7)
