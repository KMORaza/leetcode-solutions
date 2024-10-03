from collections import deque
from typing import List
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0)])
        obstacles_count = [[float('inf')] * cols for _ in range(rows)]
        obstacles_count[0][0] = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_obstacles = obstacles_count[x][y] + grid[nx][ny]
                    if new_obstacles < obstacles_count[nx][ny]:
                        obstacles_count[nx][ny] = new_obstacles
                        queue.append((nx, ny))
        return obstacles_count[rows - 1][cols - 1]
