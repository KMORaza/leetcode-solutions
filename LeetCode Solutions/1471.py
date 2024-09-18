from typing import List
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        sorted_by_strength = sorted(arr, key=lambda x: (abs(x - median), x), reverse=True)
        return sorted_by_strength[:k]
