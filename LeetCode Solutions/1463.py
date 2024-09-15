class Solution:
    def cherryPickup(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        return self.collectCherries(grid, 0, 0, cols - 1, dp)
    def collectCherries(self, grid, r, c1, c2, dp):
        if r == len(grid):
            return 0
        if c1 < 0 or c1 >= len(grid[0]) or c2 < 0 or c2 >= len(grid[0]):
            return 0
        if dp[r][c1][c2] != -1:
            return dp[r][c1][c2]
        cherriesInRow = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
        maxCherries = 0
        for move1 in (-1, 0, 1):
            for move2 in (-1, 0, 1):
                maxCherries = max(maxCherries, cherriesInRow + self.collectCherries(grid, r + 1, c1 + move1, c2 + move2, dp))
        dp[r][c1][c2] = maxCherries
        return maxCherries
