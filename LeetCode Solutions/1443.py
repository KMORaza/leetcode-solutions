from typing import List, Dict, Set
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node: int, parent: int) -> int:
            total_time = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                time_in_subtree = dfs(neighbor, node)
                if time_in_subtree > 0 or hasApple[neighbor]:
                    total_time += time_in_subtree + 2
            return total_time
        return dfs(0, -1)
