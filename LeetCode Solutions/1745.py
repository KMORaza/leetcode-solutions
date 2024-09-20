class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length == 2 or dp[start + 1][end - 1]:
                        dp[start][end] = True
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if dp[0][i] and dp[i + 1][j] and dp[j + 1][n - 1]:
                    return True
        return False
