from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]
        total_cost = 0
        visited = set()
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            total_cost += cost
            visited.add(u)
            for v in range(n):
                if v not in visited:
                    distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (distance, v))
        return total_cost
