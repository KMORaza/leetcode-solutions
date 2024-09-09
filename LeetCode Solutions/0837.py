class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        if n >= k + maxPts - 1:
            return 1.0
        dp = [0] * (n + 1)
        dp[0] = 1.0
        window_sum = dp[0]
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i >= maxPts:
                window_sum -= dp[i - maxPts]
        return sum(dp[k:])
