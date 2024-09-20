from typing import List, defaultdict
from collections import deque
class Solution:
    def largestPathValue(self, c: str, e: List[List[int]]) -> int:
        n = len(c)
        max_value = 0
        processed_count = 0
        graph = defaultdict(list)
        in_degree = [0] * n
        color_count = [[0] * 26 for _ in range(n)]
        for u, v in e:
            graph[u].append(v)
            in_degree[v] += 1
        q = deque(i for i in range(n) if in_degree[i] == 0)
        while q:
            current = q.popleft()
            processed_count += 1
            max_value = max(max_value, color_count[current][ord(c[current]) - ord('a')] + 1)
            color_count[current][ord(c[current]) - ord('a')] += 1
            for neighbor in graph[current]:
                for i in range(26):
                    color_count[neighbor][i] = max(color_count[neighbor][i], color_count[current][i])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        return max_value if processed_count == n else -1
