from typing import List
from collections import deque, defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        result = list(range(n))
        for person in topo_order:
            for richer_person in graph[person]:
                if quiet[result[person]] < quiet[result[richer_person]]:
                    result[richer_person] = result[person]
        return result

