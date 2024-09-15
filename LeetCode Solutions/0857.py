import heapq
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        n = len(quality)
        for i in range(n):
            ratio = wage[i] / quality[i]
            workers.append((ratio, quality[i]))
        workers.sort()
        min_heap = []
        total_quality = 0
        min_cost = float('inf')
        for ratio, q in workers:
            heapq.heappush(min_heap, -q)
            total_quality += q
            if len(min_heap) > k:
                total_quality += heapq.heappop(min_heap)
            if len(min_heap) == k:
                min_cost = min(min_cost, ratio * total_quality)
        return min_cost
