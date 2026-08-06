class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n

        for i in range(n):
            score[edges[i]] += i

        max_score = max(score)
        for i in range(n):
            if score[i] == max_score:
                return i