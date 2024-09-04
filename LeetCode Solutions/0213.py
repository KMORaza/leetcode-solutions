class Solution:
    def rob(self, nums):
        def rob_linear(nums):
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        n = len(nums)
        if n == 1:
            return nums[0]
        max_amount_1 = rob_linear(nums[:-1])
        max_amount_2 = rob_linear(nums[1:])
        return max(max_amount_1, max_amount_2)
