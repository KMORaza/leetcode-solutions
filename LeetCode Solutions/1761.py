from typing import List
from collections import defaultdict
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        degree = [0] * (n + 1)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1
        min_degree_sum = float('inf')
        for u in range(1, n + 1):
            for v in graph[u]:
                if v > u:
                    for w in graph[v]:
                        if w > v and w in graph[u]:
                            trio_degree_sum = degree[u] + degree[v] + degree[w] - 6
                            min_degree_sum = min(min_degree_sum, trio_degree_sum)
        return min_degree_sum if min_degree_sum != float('inf') else -1
