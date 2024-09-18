from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        sorted_freq = sorted(freq.values())
        unique_count = len(sorted_freq)
        for count in sorted_freq:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break
        return unique_count
