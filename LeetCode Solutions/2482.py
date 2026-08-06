class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ones_row = row_ones[i]
                zeros_row = n - ones_row
                ones_col = col_ones[j]
                zeros_col = m - ones_col

                result[i][j] = ones_row + ones_col - zeros_row - zeros_col

        return result