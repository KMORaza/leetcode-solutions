from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithCapacity(capacity: int) -> bool:
            current_load = 0
            required_days = 1
            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = weight
                    if required_days > days:
                        return False
                else:
                    current_load += weight
            return True
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if canShipWithCapacity(mid):
                high = mid
            else:
                low = mid + 1
        return low
