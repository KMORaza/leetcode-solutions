class Solution:
    def countPaths(self, grid):
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            count = 1

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    count = (count + dfs(ni, nj)) % MOD

            memo[i][j] = count
            return count

        total = 0
        for i in range(m):
            for j in range(n):
                total = (total + dfs(i, j)) % MOD

        return total