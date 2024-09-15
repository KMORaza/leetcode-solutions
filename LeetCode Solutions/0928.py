from collections import deque
class Solution:
    def minMalwareSpread(self, graph, initial):
        output = 0
        minimum = len(graph)
        initial.sort()
        for i in initial:
            count = self.bfs(graph, i, initial)
            if count < minimum:
                minimum = count
                output = i
        return output
    def bfs(self, graph, removed, initial):
        q = deque()
        seen = [False] * len(graph)
        seen[removed] = True
        count = 0
        for i in initial:
            if i != removed:
                q.append(i)
                seen[i] = True
        while q:
            u = q.popleft()
            count += 1
            for i in range(len(graph)):
                if seen[i]:
                    continue
                if i != u and graph[i][u] == 1:
                    q.append(i)
                    seen[i] = True
        return count
