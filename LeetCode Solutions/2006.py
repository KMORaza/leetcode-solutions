from typing import List
from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = Counter(nums)
        for num in num_count:
            if num + k in num_count:
                count += num_count[num] * num_count[num + k]
        return count
