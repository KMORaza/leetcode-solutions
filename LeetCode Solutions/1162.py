from typing import List
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        visited = [[False] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited[r][c] = True
        if len(queue) == 0 or len(queue) == rows * cols:
            return -1
        max_distance = -1
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
                    max_distance = max(max_distance, grid[nr][nc] - 1)
        return max_distance
