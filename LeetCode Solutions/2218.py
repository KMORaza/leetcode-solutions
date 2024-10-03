from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            current_sum = [0] * (len(pile) + 1)
            for j in range(len(pile)):
                current_sum[j + 1] = current_sum[j] + pile[j]
            for j in range(k, 0, -1):
                for x in range(1, min(j, len(pile)) + 1):
                    dp[j] = max(dp[j], dp[j - x] + current_sum[x])
        return dp[k]