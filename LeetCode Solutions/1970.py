from typing import List
from collections import deque
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1
            queue = deque()
            visited = [[False] * col for _ in range(row)]
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited[0][c] = True
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            while queue:
                x, y = queue.popleft()
                if x == row - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        left, right = 1, len(cells)
        best_day = 0
        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                best_day = mid
                left = mid + 1
            else:
                right = mid - 1
        return best_day
