from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        top_view = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] > 0)
        front_view = sum(max(grid[r]) for r in range(rows))
        side_view = sum(max(grid[r][c] for r in range(rows)) for c in range(cols))
        return top_view + front_view + side_view
