class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        if (target + total_sum) % 2 != 0 or (target + total_sum) < 0:
            return 0
        P = (target + total_sum) // 2
        if P > total_sum:
            return 0
        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]
