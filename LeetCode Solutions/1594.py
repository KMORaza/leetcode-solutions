class Solution:
    def maxProductPath(self, grid):
        rows, cols = len(grid), len(grid[0])
        min_product = [[0] * cols for _ in range(rows)]
        max_product = [[0] * cols for _ in range(rows)]
        min_product[0][0] = max_product[0][0] = grid[0][0]
        for r in range(1, rows):
            min_product[r][0] = max_product[r][0] = min_product[r - 1][0] * grid[r][0]
        for c in range(1, cols):
            min_product[0][c] = max_product[0][c] = min_product[0][c - 1] * grid[0][c]
        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] < 0:
                    min_product[r][c] = max(max_product[r - 1][c], max_product[r][c - 1]) * grid[r][c]
                    max_product[r][c] = min(min_product[r - 1][c], min_product[r][c - 1]) * grid[r][c]
                else:
                    min_product[r][c] = min(min_product[r - 1][c], min_product[r][c - 1]) * grid[r][c]
                    max_product[r][c] = max(max_product[r - 1][c], max_product[r][c - 1]) * grid[r][c]
        max_result = max(min_product[rows - 1][cols - 1], max_product[rows - 1][cols - 1])
        return -1 if max_result < 0 else max_result % (10**9+7)
