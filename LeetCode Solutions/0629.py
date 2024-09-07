class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            prefix_sum = [0] * (k + 1)
            prefix_sum[0] = dp[i-1][0]
            for j in range(1, k + 1):
                prefix_sum[j] = (prefix_sum[j-1] + dp[i-1][j]) % MOD
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = prefix_sum[j]
                else:
                    dp[i][j] = (prefix_sum[j] - (prefix_sum[j-i] if j >= i else 0) + MOD) % MOD
        return dp[n][k]
