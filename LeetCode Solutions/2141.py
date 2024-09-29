from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_capacity = sum(batteries)
        left, right = 0, total_capacity // n
        while left < right:
            mid = (left + right + 1) // 2
            total_power_needed = mid * n
            power_provided = sum(min(battery, mid) for battery in batteries)
            if power_provided >= total_power_needed:
                left = mid
            else:
                right = mid - 1
        return left