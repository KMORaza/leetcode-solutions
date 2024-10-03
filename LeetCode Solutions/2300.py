from typing import List
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for spell in spells:
            threshold = (success + spell - 1) // spell
            index = bisect_left(potions, threshold)
            result.append(len(potions) - index)
        return result