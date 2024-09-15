class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * n
        low = [-1] * n
        visited = [False] * n
        bridges = []
        time = [0]
        def dfs(u: int, parent: int):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent:
                    low[u] = min(low[u], disc[v])
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
        return bridges
