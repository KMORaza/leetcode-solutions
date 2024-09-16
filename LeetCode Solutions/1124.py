from typing import List
from collections import defaultdict
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = 0
        max_length = 0
        first_occurrence = {0: -1}
        for i, h in enumerate(hours):
            if h > 8:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            if prefix_sum > 0:
                max_length = i + 1
            else:
                if prefix_sum - 1 in first_occurrence:
                    max_length = max(max_length, i - first_occurrence[prefix_sum - 1])
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
        return max_length
