from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            current = dp[:]
            for i in range(3):
                new_remainder = (i + num) % 3
                dp[new_remainder] = max(dp[new_remainder], current[i] + num)
        return dp[0]
