from typing import List
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank
