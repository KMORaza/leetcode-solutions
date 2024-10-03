from typing import List
from collections import Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = Counter()
        for lst in nums:
            count.update(set(lst))
        return sorted(num for num, freq in count.items() if freq == len(nums))