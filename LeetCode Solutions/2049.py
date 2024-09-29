from typing import List, DefaultDict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = DefaultDict(list)
        for child, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(child)
        subtree_size = [1] * n
        def dfs(node):
            for child in children[node]:
                dfs(child)
                subtree_size[node] += subtree_size[child]
        dfs(0)
        max_score = 0
        score_count = DefaultDict(int)
        for node in range(n):
            score = 1
            total_size = n - subtree_size[node]
            for child in children[node]:
                score *= subtree_size[child]
            if total_size > 0:
                score *= total_size
            max_score = max(max_score, score)
            score_count[score] += 1
        return score_count[max_score]
