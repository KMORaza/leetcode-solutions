class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {num: i + 1 for i, num in enumerate(sorted_unique)}
        return [rank[num] for num in arr]
