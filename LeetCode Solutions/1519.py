from collections import defaultdict
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        result = [0] * n
        def dfs(node, parent):
            count = [0] * 26
            label_index = ord(labels[node]) - ord('a')
            count[label_index] += 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_count = dfs(neighbor, node)
                for i in range(26):
                    count[i] += child_count[i]
            result[node] = count[label_index]
            return count
        dfs(0, -1)
        return result
