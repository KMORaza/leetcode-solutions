from collections import deque, defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(leaves)
            remaining_nodes -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
        return list(leaves)
