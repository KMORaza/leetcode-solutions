from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def canComplete(trips_per_time):
            return sum(trips_per_time // t for t in time) >= totalTrips
        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if canComplete(mid):
                right = mid
            else:
                left = mid + 1
        return left