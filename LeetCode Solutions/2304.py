class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('inf')] * n for _ in range(m)]
        
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        for i in range(1, m):
            for j in range(n):
                for prev_j in range(n):
                    value = grid[i-1][prev_j]
                    cost = dp[i-1][prev_j] + moveCost[value][j] + grid[i][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        return min(dp[m-1])
