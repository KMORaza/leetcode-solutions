from typing import List
from math import gcd
from functools import reduce
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        present = [False] * (max_num + 1)
        for num in nums:
            present[num] = True
        unique_gcds = set()
        for g in range(1, max_num + 1):
            current_gcd = 0
            for multiple in range(g, max_num + 1, g):
                if present[multiple]:
                    current_gcd = gcd(current_gcd, multiple)
            if current_gcd == g:
                unique_gcds.add(g)
        return len(unique_gcds)
