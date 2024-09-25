from bisect import bisect_right
from typing import List
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        result = []
        for obstacle in obstacles:
            pos = bisect_right(dp, obstacle)
            if pos == len(dp):
                dp.append(obstacle)
            else:
                dp[pos] = obstacle
            result.append(pos + 1)
        return result