class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        indexed_scores.sort(reverse=True, key=lambda x: x[0])
        result = [""] * n
        for rank, (s, i) in enumerate(indexed_scores):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)
        return result
