from typing import List
from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lonely_numbers = []
        for num in count:
            if count[num] == 1 and (num - 1) not in count and (num + 1) not in count:
                lonely_numbers.append(num)
        return lonely_numbers