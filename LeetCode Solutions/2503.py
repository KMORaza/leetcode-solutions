class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        from collections import defaultdict

        m, n = len(grid), len(grid[0])
        result = [0] * len(queries)

        indexed_queries = [(queries[i], i) for i in range(len(queries))]
        indexed_queries.sort()

        visited = [[False] * n for _ in range(m)]
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        count = 0

        for threshold, original_idx in indexed_queries:
            while pq and pq[0][0] < threshold:
                val, x, y = heapq.heappop(pq)

                if visited[x][y]:
                    continue

                visited[x][y] = True
                count += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heapq.heappush(pq, (grid[nx][ny], nx, ny))

            result[original_idx] = count

        return result