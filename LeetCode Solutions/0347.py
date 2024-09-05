from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map = Counter(nums)
        min_heap = []
        for num, freq in frequency_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]
