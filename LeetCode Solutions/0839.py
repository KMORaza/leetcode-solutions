class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            diff = []
            for a, b in zip(s1, s2):
                if a != b:
                    diff.append((a, b))
                    if len(diff) > 2:
                        return False
            return len(diff) == 2 and diff[0] == diff[1][::-1]
        def dfs(node: int):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        n = len(strs)
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for i in range(n):
            for j in range(i + 1, n):
                if are_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        num_groups = 0
        for i in range(n):
            if not visited[i]:
                num_groups += 1
                dfs(i)
        return num_groups
