import heapq
from typing import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        min_heap = []
        speed_sum = 0
        max_performance = 0
        for eff, spd in engineers:
            if len(min_heap) >= k:
                speed_sum -= heapq.heappop(min_heap)
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            max_performance = max(max_performance, speed_sum * eff)
        return max_performance % (10**9 + 7)
