from typing import List
import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def find_min_distance(house: int) -> int:
            pos = bisect.bisect_left(heaters, house)
            if pos == 0:
                return abs(house - heaters[0])
            if pos == len(heaters):
                return abs(house - heaters[-1])
            return min(abs(house - heaters[pos]), abs(house - heaters[pos - 1]))
        return max(find_min_distance(house) for house in houses)
