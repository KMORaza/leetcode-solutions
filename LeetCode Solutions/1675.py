import heapq
class Solution:
    def minimumDeviation(self, arr):
        result = float('inf')
        min_val = float('inf')
        max_heap = []
        for value in arr:
            even_value = value if value % 2 == 0 else value * 2
            min_val = min(min_val, even_value)
            heapq.heappush(max_heap, -even_value)
        while max_heap[0] % 2 == 0:
            max_value = -heapq.heappop(max_heap)
            result = min(result, max_value - min_val)
            min_val = min(min_val, max_value // 2)
            heapq.heappush(max_heap, -max_value // 2)
        return min(result, -max_heap[0] - min_val)
