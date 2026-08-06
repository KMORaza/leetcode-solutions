class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            count = {}
            unique_count = 0

            for j in range(i, 0, -1):
                num = nums[j - 1]
                count[num] = count.get(num, 0) + 1

                if count[num] == 1:
                    unique_count += 1
                elif count[num] == 2:
                    unique_count -= 1

                trimmed_length = (i - j + 1) - unique_count
                cost = k + trimmed_length
                dp[i] = min(dp[i], dp[j - 1] + cost)

        return dp[n]