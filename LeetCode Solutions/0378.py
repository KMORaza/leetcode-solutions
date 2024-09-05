import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        for _ in range(k):
            value, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        return value