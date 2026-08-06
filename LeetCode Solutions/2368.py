class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        restricted_set = set(restricted)
        visited = set()

        def dfs(node):
            if node in visited or node in restricted_set:
                return 0
            visited.add(node)
            count = 1
            for neighbor in graph[node]:
                count += dfs(neighbor)
            return count

        return dfs(0)