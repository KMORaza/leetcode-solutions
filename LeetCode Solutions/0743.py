import heapq
import sys
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        def dijkstra(source: int) -> List[int]:
            min_heap = [(0, source)]
            distances = {i: float('inf') for i in range(1, n + 1)}
            distances[source] = 0
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                if current_dist > distances[u]:
                    continue
                for v, weight in graph[u]:
                    distance = current_dist + weight
                    if distance < distances[v]:
                        distances[v] = distance
                        heapq.heappush(min_heap, (distance, v))
            return distances
        distances = dijkstra(k)
        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1
