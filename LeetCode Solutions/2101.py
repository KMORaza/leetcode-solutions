from typing import List
import math
from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, _ = bombs[j]
                    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if distance <= r1:
                        graph[i].append(j)
        def dfs(bomb_index: int, visited: set) -> int:
            visited.add(bomb_index)
            count = 1
            for neighbor in graph[bomb_index]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count
        max_detonated = 0
        for i in range(n):
            visited = set()
            detonated_count = dfs(i, visited)
            max_detonated = max(max_detonated, detonated_count)
        return max_detonated
