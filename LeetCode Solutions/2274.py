from typing import List
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_consecutive = 0
        if special:
            max_consecutive = max(max_consecutive, special[0] - bottom)
        for i in range(1, len(special)):
            gap = special[i] - special[i - 1] - 1
            max_consecutive = max(max_consecutive, gap)
        if special:
            max_consecutive = max(max_consecutive, top - special[-1])
        else:
            max_consecutive = top - bottom + 1
        return max_consecutive
