from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [float('inf')] * (last_day + 1)
        dp[0] = 0
        day_set = set(days)
        for day in range(1, last_day + 1):
            if day in day_set:
                dp[day] = min(
                    dp[max(day - 1, 0)] + costs[0],
                    dp[max(day - 7, 0)] + costs[1],
                    dp[max(day - 30, 0)] + costs[2]
                )
            else:
                dp[day] = dp[day - 1]
        return dp[last_day]
