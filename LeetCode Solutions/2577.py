from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m == 1 and n == 1:
            return 0

        if (m == 1 or grid[0][1] > 1) and (n == 1 or grid[1][0] > 1):
            return -1

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return time

            if time > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    arrive = time + 1

                    if arrive < grid[nr][nc]:
                        diff = grid[nr][nc] - arrive

                        if diff % 2 == 0:
                            arrive = grid[nr][nc]
                        else:
                            arrive = grid[nr][nc] + 1

                    if arrive < dist[nr][nc]:
                        dist[nr][nc] = arrive
                        heapq.heappush(heap, (arrive, nr, nc))

        return -1