from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        max_quality = 0
        n = len(values)
        def dfs(node, current_time, current_quality, visited):
            nonlocal max_quality
            if node == 0:
                max_quality = max(max_quality, current_quality)
            for neighbor, travel_time in graph[node]:
                if current_time + travel_time <= maxTime:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, current_time + travel_time, current_quality + values[neighbor], visited)
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, current_time + travel_time, current_quality, visited)
        visited = {0}
        dfs(0, 0, values[0], visited)
        return max_quality