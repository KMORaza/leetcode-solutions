from typing import List
from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == len(nums) // 2:
                return num
