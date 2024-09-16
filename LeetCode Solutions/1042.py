from typing import List
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        result = [0] * n
        for garden in range(1, n + 1):
            used_colors = set(result[adj - 1] for adj in graph[garden])
            for color in range(1, 5):
                if color not in used_colors:
                    result[garden - 1] = color
                    break
        return result