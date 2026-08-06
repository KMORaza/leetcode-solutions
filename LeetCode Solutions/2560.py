class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_k_houses_with_max_value(max_val):
            # DP to find max number of houses we can rob with max value constraint
            n = len(nums)
            dp = [0] * n

            if nums[0] <= max_val:
                dp[0] = 1

            if n > 1:
                dp[1] = 1 if nums[1] <= max_val else dp[0]

            for i in range(2, n):
                take = 0
                if nums[i] <= max_val:
                    take = 1 + dp[i - 2]
                skip = dp[i - 1]
                dp[i] = max(take, skip)

            return dp[n - 1] >= k

        left, right = min(nums), max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_rob_k_houses_with_max_value(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result