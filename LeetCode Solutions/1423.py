from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        if k == n:
            return total_sum
        min_subarray_sum = float('inf')
        window_sum = sum(cardPoints[:n - k])
        min_subarray_sum = min(min_subarray_sum, window_sum)
        for i in range(n - k, n):
            window_sum = window_sum - cardPoints[i - (n - k)] + cardPoints[i]
            min_subarray_sum = min(min_subarray_sum, window_sum)
        max_score = total_sum - min_subarray_sum
        return max_score
