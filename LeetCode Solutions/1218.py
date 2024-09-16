from typing import List
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        max_length = 0
        for num in arr:
            dp[num] = dp[num - difference] + 1
            max_length = max(max_length, dp[num])
        return max_length
