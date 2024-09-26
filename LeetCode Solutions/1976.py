from collections import defaultdict
import heapq
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        x = 10**9 + 7
        dist = [float('inf')] * n
        count = [0] * n
        dist[0] = 0
        count[0] = 1
        min_heap = [(0, 0)]
        while min_heap:
            d, node = heapq.heappop(min_heap)
            if d > dist[node]:
                continue
            for neighbor, time in graph[node]:
                new_dist = d + time
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    count[neighbor] = count[node]
                    heapq.heappush(min_heap, (new_dist, neighbor))
                elif new_dist == dist[neighbor]:
                    count[neighbor] = (count[neighbor] + count[node]) % x
        return count[n-1]