from typing import List
from collections import defaultdict
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort(key=lambda x: x[1])
        ride_map = defaultdict(list)
        for start, end, tip in rides:
            ride_map[end].append((start, tip))
        for end in range(1, n + 1):
            dp[end] = dp[end - 1]
            for start, tip in ride_map[end]:
                dp[end] = max(dp[end], dp[start] + (end - start) + tip)
        return dp[n]