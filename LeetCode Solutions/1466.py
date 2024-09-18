from typing import List
from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))
        def dfs(node: int, parent: int) -> int:
            count = 0
            for neighbor, needs_reversal in graph[node]:
                if neighbor != parent:
                    if needs_reversal:
                        count += 1
                    count += dfs(neighbor, node)
            return count
        return dfs(0, -1)
