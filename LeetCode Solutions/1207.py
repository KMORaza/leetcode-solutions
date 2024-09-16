from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurrences = list(counts.values())
        return len(occurrences) == len(set(occurrences))
