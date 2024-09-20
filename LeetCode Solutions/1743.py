from collections import defaultdict, deque
from typing import List
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        start = next(num for num in graph if len(graph[num]) == 1)
        result = []
        queue = deque([start])
        visited = set([start])
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
