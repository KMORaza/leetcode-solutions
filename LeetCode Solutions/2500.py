class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)

        result = 0
        m, n = len(grid), len(grid[0])

        for col in range(n):
            max_in_col = 0
            for row in range(m):
                max_in_col = max(max_in_col, grid[row][col])
            result += max_in_col

        return result