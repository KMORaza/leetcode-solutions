from typing import List, Deque
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r: int, c: int):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        stack.append((x + dx, y + dy))
        def bfs():
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dx, c + dy
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                                q.append((nr, nc, 1))
                                grid[nr][nc] = 3
            while q:
                r, c, dist = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            return dist
                        if grid[nr][nc] == 0:
                            q.append((nr, nc, dist + 1))
                            grid[nr][nc] = 3
        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
        return bfs()
