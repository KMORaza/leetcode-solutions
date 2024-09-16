class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = -1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n-1] == 1:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m-1][j] == 1:
                dfs(m-1, j)
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    enclave_count += 1
        return enclave_count
