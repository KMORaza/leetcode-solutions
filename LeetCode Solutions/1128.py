from typing import List
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for a, b in dominoes:
            normalized = (min(a, b), max(a, b))
            count[normalized] += 1
        pairs = 0
        for value in count.values():
            pairs += value * (value - 1) // 2
        return pairs
