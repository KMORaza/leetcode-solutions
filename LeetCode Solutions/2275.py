from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for i in range(32):
            count = sum((candidate >> i) & 1 for candidate in candidates)
            max_count = max(max_count, count)
        return max_count