class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0

        pairs = []
        for i in range(n - 1):
            pairs.append(weights[i] + weights[i + 1])

        pairs.sort()

        min_score = 0
        max_score = 0

        for i in range(k - 1):
            min_score += pairs[i]
            max_score += pairs[-(i + 1)]

        return max_score - min_score