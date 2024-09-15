class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [float('inf')] * m
        for j in range(m):
            dp[j] = grid[0][j]
        for i in range(1, n):
            min1, min2 = float('inf'), float('inf')
            min1_idx = -1
            for j in range(m):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    min1_idx = j
                elif dp[j] < min2:
                    min2 = dp[j]
            new_dp = [float('inf')] * m
            for j in range(m):
                if j == min1_idx:
                    new_dp[j] = grid[i][j] + min2
                else:
                    new_dp[j] = grid[i][j] + min1
            dp = new_dp
        return min(dp)
