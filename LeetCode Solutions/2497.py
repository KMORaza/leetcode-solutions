class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]

        for a, b in edges:
            if vals[b] > 0:
                graph[a].append(vals[b])
            if vals[a] > 0:
                graph[b].append(vals[a])

        for i in range(n):
            graph[i].sort(reverse=True)
            graph[i] = graph[i][:k]

        max_sum = float('-inf')

        for i in range(n):
            current_sum = vals[i]
            for j in range(len(graph[i])):
                current_sum += graph[i][j]
            max_sum = max(max_sum, current_sum)

        return max_sum