import math
from typing import List
class Solution:
    def minSpeedOnTime(self, distances: List[int], max_hour: float) -> int:
        result = -1
        left, right = 1, int(10**7)
        while left <= right:
            mid = (left + right) // 2
            if self.calculate_time(distances, max_hour, mid) > max_hour:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result
    def calculate_time(self, distances: List[int], max_hour: float, velocity: int) -> float:
        total_time = 0
        for i in range(len(distances) - 1):
            total_time += math.ceil(distances[i] / velocity)
        total_time += distances[-1] / velocity
        return total_time
