class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        n = len(isConnected)
        visited = [False] * n
        num_provinces = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                num_provinces += 1
        return num_provinces
