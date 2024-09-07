class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        for move in range(1, maxMove + 1):
            for r in range(m):
                for c in range(n):
                    if r == 0:
                        dp[move][r][c] += 1
                    if r == m - 1:
                        dp[move][r][c] += 1
                    if c == 0:
                        dp[move][r][c] += 1
                    if c == n - 1:
                        dp[move][r][c] += 1

                    dp[move][r][c] %= MOD
                    if r > 0:
                        dp[move][r][c] += dp[move - 1][r - 1][c]
                    if r < m - 1:
                        dp[move][r][c] += dp[move - 1][r + 1][c]
                    if c > 0:
                        dp[move][r][c] += dp[move - 1][r][c - 1]
                    if c < n - 1:
                        dp[move][r][c] += dp[move - 1][r][c + 1]
                    dp[move][r][c] %= MOD
        return dp[maxMove][startRow][startColumn]

