from typing import List
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum(num for num, freq in count.items() if freq == 1)
