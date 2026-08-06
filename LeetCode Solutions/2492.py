class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        min_score = float('inf')

        def dfs(city):
            nonlocal min_score
            visited.add(city)

            for neighbor, weight in graph[city]:
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(1)
        return min_score