class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 0, 0, 0]
        mod = 10**9 + 7
        for _ in range(1, n + 1):
            new_dp = [0] * 4
            new_dp[0] = (dp[0] + dp[1] + dp[2] + dp[3]) % mod
            new_dp[1] = (dp[2] + dp[3]) % mod
            new_dp[2] = (dp[1] + dp[3]) % mod
            new_dp[3] = dp[0]
            dp = new_dp
        return dp[0]
