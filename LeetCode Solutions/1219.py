from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < m and 0 <= y < n and grid[x][y] > 0):
                return 0
            gold = grid[x][y]
            grid[x][y] = 0
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                max_gold = max(max_gold, dfs(nx, ny))
            grid[x][y] = gold
            return gold + max_gold
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold
