from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
        result = []
        min_heap = []
        time = 0
        i = 0
        while i < len(tasks) or min_heap:
            if not min_heap:
                time = max(time, tasks[i][0])
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            duration, index = heapq.heappop(min_heap)
            result.append(index)
            time += duration
        return result
