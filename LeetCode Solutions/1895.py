from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_size = 0
        row_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        col_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                row_sum[i][j] = row_sum[i][j - 1] + grid[i - 1][j - 1]
                col_sum[i][j] = col_sum[i - 1][j] + grid[i - 1][j - 1]
        for size in range(1, min(rows, cols) + 1):
            for i in range(size - 1, rows):
                for j in range(size - 1, cols):
                    if self.isMagicSquare(grid, i - size + 1, j - size + 1, size):
                        max_size = max(max_size, size)
        return max_size
    def isMagicSquare(self, grid: List[List[int]], start_row: int, start_col: int, size: int) -> bool:
        target_sum = sum(grid[start_row][start_col:start_col + size])
        for i in range(size):
            if sum(grid[start_row + i][start_col:start_col + size]) != target_sum:
                return False
        for j in range(size):
            if sum(grid[start_row + i][start_col + j] for i in range(size)) != target_sum:
                return False
        if sum(grid[start_row + i][start_col + i] for i in range(size)) != target_sum:
            return False
        if sum(grid[start_row + i][start_col + size - 1 - i] for i in range(size)) != target_sum:
            return False
        return True