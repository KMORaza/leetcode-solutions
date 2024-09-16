from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> None:
            grid[x][y] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    dfs(nx, ny)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0:
                dfs(m-1, j)
        closed_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    closed_islands += 1
        return closed_islands
