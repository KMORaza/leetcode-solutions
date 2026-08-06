class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        total_sum = sum(nums)

        if total_sum < 2 * k:
            return 0

        dp = [0] * k
        dp[0] = 1

        for num in nums:
            new_dp = dp[:]
            for j in range(k):
                if j >= num:
                    new_dp[j] = (new_dp[j] + dp[j - num]) % MOD
            dp = new_dp

        invalid_partitions = sum(dp) % MOD
        total_partitions = pow(2, n, MOD)

        result = (total_partitions - 2 * invalid_partitions) % MOD
        return result