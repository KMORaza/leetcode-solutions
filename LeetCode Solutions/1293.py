from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, k, 0)])
        visited = [[[False] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        visited[0][0][k] = True
        while queue:
            r, c, obstacles_left, dist = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_obstacles_left = obstacles_left - grid[nr][nc]
                    if new_obstacles_left >= 0 and not visited[nr][nc][new_obstacles_left]:
                        visited[nr][nc][new_obstacles_left] = True
                        queue.append((nr, nc, new_obstacles_left, dist + 1))
        return -1
