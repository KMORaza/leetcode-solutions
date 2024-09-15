class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                for p in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])
        return dp[n][k]

