from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            if grid[r][0] == 0:
                grid[r] = [1 - x for x in grid[r]]
        for c in range(1, cols):
            count_ones = sum(grid[r][c] for r in range(rows))
            if count_ones < rows / 2:
                for r in range(rows):
                    grid[r][c] = 1 - grid[r][c]
        score = 0
        for r in range(rows):
            row_value = 0
            for c in range(cols):
                row_value = row_value * 2 + grid[r][c]
            score += row_value
        return score
