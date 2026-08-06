import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0

        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            score += max_val
            heapq.heappush(max_heap, -((max_val + 2) // 3))

        return score