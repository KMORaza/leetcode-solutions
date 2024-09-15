from collections import defaultdict
from typing import List
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for rod in rods:
            current_dp = list(dp.items())
            for diff, height in current_dp:
                dp[diff + rod] = max(dp[diff + rod], height)
                dp[abs(diff - rod)] = max(dp[abs(diff - rod)], height + min(rod, diff))
        return dp[0]