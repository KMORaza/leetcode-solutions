from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining_capacities = [capacity[i] - rocks[i] for i in range(len(capacity))]
        remaining_capacities.sort()
        filled_bags = 0
        for remaining in remaining_capacities:
            if additionalRocks >= remaining:
                additionalRocks -= remaining
                filled_bags += 1
            else:
                break
        return filled_bags