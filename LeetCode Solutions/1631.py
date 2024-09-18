from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(0, 0, 0)]
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            if x == rows - 1 and y == cols - 1:
                return effort
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    current_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    if current_effort < efforts[nx][ny]:
                        efforts[nx][ny] = current_effort
                        heapq.heappush(min_heap, (current_effort, nx, ny))
        return -1
