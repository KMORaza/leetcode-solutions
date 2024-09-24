from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * (right - left + 1)
        for start, end in ranges:
            for i in range(max(start, left), min(end, right) + 1):
                covered[i - left] = True
        return all(covered)
