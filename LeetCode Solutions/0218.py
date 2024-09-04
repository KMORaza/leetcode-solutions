import heapq
from collections import Counter
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))
        events.sort()
        max_heap = [0]
        height_count = Counter()
        height_count[0] = 1
        prev_max_height = 0
        result = []
        for x, height in events:
            if height < 0:
                height_count[-height] += 1
                heapq.heappush(max_heap, height)
            else:
                height_count[height] -= 1
            while max_heap and height_count[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            current_max_height = -max_heap[0]
            if current_max_height != prev_max_height:
                result.append([x, current_max_height])
                prev_max_height = current_max_height
        return result
