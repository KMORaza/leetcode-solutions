from typing import List
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def canReach(time: int) -> bool:
            if grid[0][0] > time or grid[n - 1][n - 1] > time:
                return False
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= time:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        low, high = 0, n * n - 1
        while low < high:
            mid = (low + high) // 2
            if canReach(mid):
                high = mid
            else:
                low = mid + 1
        return low
