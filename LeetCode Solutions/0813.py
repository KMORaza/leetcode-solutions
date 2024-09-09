class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        def average(l, r):
            return (prefix_sum[r + 1] - prefix_sum[l]) / (r - l + 1)
        dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for l in range(i):
                    dp[i][j] = max(dp[i][j], dp[l][j - 1] + average(l, i - 1))
        return dp[n][k]
