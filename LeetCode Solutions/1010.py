from typing import List
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = defaultdict(int)
        pairs = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            pairs += remainder_count[complement]
            remainder_count[remainder] += 1
        return pairs
