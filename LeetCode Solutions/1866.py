class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        if k == 0:
            return 1 if n == 0 else 0
        if n < k:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1)) % (10**9 + 7)
        return dp[n][k]
