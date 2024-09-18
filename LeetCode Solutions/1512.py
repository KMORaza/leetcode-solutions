from typing import List
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        good_pairs = 0
        for count in frequency.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        return good_pairs
