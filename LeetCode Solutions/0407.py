import heapq
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        min_heap = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        water_trapped = 0
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_height = max(heightMap[nx][ny], height)
                    water_trapped += new_height - heightMap[nx][ny]
                    heapq.heappush(min_heap, (new_height, nx, ny))
        return water_trapped