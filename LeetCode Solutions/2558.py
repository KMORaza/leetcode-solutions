import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_gifts = -heapq.heappop(max_heap)
            remaining = int(max_gifts ** 0.5)
            heapq.heappush(max_heap, -remaining)

        return -sum(max_heap)