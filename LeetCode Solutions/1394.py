from collections import Counter
from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        max_lucky = -1
        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)
        return max_lucky
