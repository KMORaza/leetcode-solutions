from typing import List
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        first_occurrence = {}
        last_occurrence = {}
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            freq[num] += 1
        degree = max(freq.values())
        min_length = float('inf')
        for num in freq:
            if freq[num] == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
        return min_length
