from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        min_heap = []
        idx = 0
        for query, original_index in sorted_queries:
            while idx < len(intervals) and intervals[idx][0] <= query:
                start, end = intervals[idx]
                heapq.heappush(min_heap, (end - start + 1, end))
                idx += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            result[original_index] = min_heap[0][0] if min_heap else -1
        return result
