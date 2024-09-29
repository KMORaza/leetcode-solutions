from typing import List
import collections
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(start):
            queue = collections.deque([start])
            distances = {start: 0}
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in distances:
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            return distances
        distances = bfs(0)
        max_time = 0
        for i in range(1, len(patience)):
            round_trip_time = distances[i] * 2
            wait_time = (round_trip_time - 1) // patience[i] * patience[i]
            total_time = round_trip_time + wait_time
            max_time = max(max_time, total_time)
        return max_time + 1