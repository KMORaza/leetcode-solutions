from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for row in grid:
            if row[0] < 0:
                count += n
            else:
                left, right = 0, n
                while left < right:
                    mid = (left + right) // 2
                    if row[mid] < 0:
                        right = mid
                    else:
                        left = mid + 1
                count += n - left
        return count
