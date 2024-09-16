from typing import List
from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def normalize(row):
            flipped = [1 - x for x in row]
            return tuple(min(row, flipped))
        pattern_count = defaultdict(int)
        for row in matrix:
            pattern = normalize(row)
            pattern_count[pattern] += 1
        return max(pattern_count.values())
