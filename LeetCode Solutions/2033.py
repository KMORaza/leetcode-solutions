from typing import List
from collections import Counter
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [num for row in grid for num in row]
        remainder = [num % x for num in flat_grid]
        if len(set(remainder)) > 1:
            return -1
        target = sorted(flat_grid)[len(flat_grid) // 2]
        operations = sum(abs(num - target) // x for num in flat_grid)
        return operations
