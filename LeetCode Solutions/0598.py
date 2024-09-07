from typing import List
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_row, min_col = m, n
        for ai, bi in ops:
            min_row = min(min_row, ai)
            min_col = min(min_col, bi)
        return min_row * min_col
