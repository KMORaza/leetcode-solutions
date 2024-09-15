from typing import List
from math import gcd
from functools import reduce
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        overall_gcd = reduce(gcd, nums)
        return overall_gcd == 1
