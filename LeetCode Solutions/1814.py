from typing import List
from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        x = 10**9 + 7
        count = defaultdict(int)
        total = 0
        for num in nums:
            rev = int(str(num)[::-1])
            total = (total + count[num - rev]) % x
            count[num - rev] += 1
        return total
