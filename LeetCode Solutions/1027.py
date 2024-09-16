from typing import List
from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [defaultdict(int) for _ in range(len(nums))]
        max_length = 1
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j][d] + 1
                max_length = max(max_length, dp[i][d] + 1)
        return max_length
