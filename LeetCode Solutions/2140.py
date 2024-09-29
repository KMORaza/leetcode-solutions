class Solution:
    def mostPoints(self, queries):
        size = len(queries)
        scores = [0] * (size + 1)
        for idx in range(size - 1, -1, -1):
            value = queries[idx][0]
            energy = queries[idx][1]
            next_position = idx + energy + 1
            future_score = scores[next_position] if next_position < size else 0
            scores[idx] = max(value + future_score, scores[idx + 1])
        return scores[0]
