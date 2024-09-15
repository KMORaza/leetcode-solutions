from typing import List
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_surface_area = 0
        for r in range(rows):
            for c in range(cols):
                height = grid[r][c]
                if height > 0:
                    total_surface_area += 2
                    if c == 0:
                        total_surface_area += height
                    else:
                        total_surface_area += max(0, height - grid[r][c-1])
                    if c == cols - 1:
                        total_surface_area += height
                    else:
                        total_surface_area += max(0, height - grid[r][c+1])
                    if r == 0:
                        total_surface_area += height
                    else:
                        total_surface_area += max(0, height - grid[r-1][c])
                    if r == rows - 1:
                        total_surface_area += height
                    else:
                        total_surface_area += max(0, height - grid[r+1][c])
        return total_surface_area
