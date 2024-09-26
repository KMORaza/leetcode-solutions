from typing import List
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        return gcd(min_num, max_num)
