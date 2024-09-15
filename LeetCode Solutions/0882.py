import heapq
from typing import List, Tuple
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, intermediate_nodes in edges:
            graph[u].append((v, intermediate_nodes))
            graph[v].append((u, intermediate_nodes))
        dist = [maxMoves + 1] * n
        dist[0] = 0
        min_heap = [(0, 0)]
        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            if d >= maxMoves:
                break
            for v, w in graph[u]:
                if d + w + 1 < dist[v]:
                    dist[v] = d + w + 1
                    heapq.heappush(min_heap, (dist[v], v))
        total_reachable_nodes = sum(1 for d in dist if d <= maxMoves)
        reachable_nodes_via_edges = 0
        for u, v, intermediate_nodes in edges:
            reachable_from_u = maxMoves - dist[u] if dist[u] <= maxMoves else 0
            reachable_from_v = maxMoves - dist[v] if dist[v] <= maxMoves else 0
            reachable_nodes_via_edges += min(reachable_from_u + reachable_from_v, intermediate_nodes)
        return total_reachable_nodes + reachable_nodes_via_edges
