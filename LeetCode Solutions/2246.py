from typing import List
from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        max_length = 1
        def dfs(node: int) -> int:
            nonlocal max_length
            first_max = second_max = 0
            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:
                    if child_length > first_max:
                        first_max, second_max = child_length, first_max
                    elif child_length > second_max:
                        second_max = child_length
            max_length = max(max_length, first_max + second_max + 1)
            return first_max + 1
        dfs(0)
        return max_length
