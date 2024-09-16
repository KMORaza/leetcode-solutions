from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_A = float('-inf')
        max_score = float('-inf')
        for j in range(len(values)):
            max_score = max(max_score, max_A + values[j] - j)
            max_A = max(max_A, values[j] + j)
        return max_score
