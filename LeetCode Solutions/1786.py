from typing import List
import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        min_heap = [(0, n)]
        while min_heap:
            d, node = heapq.heappop(min_heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                if dist[neighbor] > d + weight:
                    dist[neighbor] = d + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        y = 10**9 + 7
        dp = [0] * (n + 1)
        dp[n] = 1
        nodes_sorted_by_distance = sorted(range(1, n + 1), key=lambda x: dist[x])
        for node in nodes_sorted_by_distance:
            for neighbor, weight in graph[node]:
                if dist[node] > dist[neighbor]:
                    dp[node] = (dp[node] + dp[neighbor]) % y
        return dp[1]
