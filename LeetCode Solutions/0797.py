from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, path: List[int]):
            path.append(node)
            if node == len(graph) - 1:
                result.append(path.copy())
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path)
            path.pop()
        result = []
        dfs(0, [])
        return result
