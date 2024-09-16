from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        flattened = []
        for row in grid:
            flattened.extend(row)
        total_elements = rows * cols
        k = k % total_elements
        shifted = flattened[-k:] + flattened[:-k]
        new_grid = []
        for i in range(rows):
            new_grid.append(shifted[i * cols:(i + 1) * cols])
        return new_grid
