import heapq
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        max_heap = [(-1.0, start_node)]
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        while max_heap:
            current_prob, u = heapq.heappop(max_heap)
            current_prob = -current_prob
            if u == end_node:
                return current_prob
            for v, prob in graph[u]:
                new_prob = current_prob * prob
                if new_prob > probabilities[v]:
                    probabilities[v] = new_prob
                    heapq.heappush(max_heap, (-new_prob, v))
        return 0.0
