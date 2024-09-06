class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        graph = defaultdict(dict)
        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1 / value
        for node in graph:
            graph[node][node] = 1.0
        nodes = list(graph.keys())
        for k in nodes:
            for i in nodes:
                if k in graph[i]:
                    for j in nodes:
                        if k in graph and j in graph[k]:
                            if j not in graph[i]:
                                graph[i][j] = -1
                            graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])
        results = []
        for u, v in queries:
            if u in graph and v in graph[u]:
                results.append(graph[u][v])
            else:
                results.append(-1.0)
        return results
