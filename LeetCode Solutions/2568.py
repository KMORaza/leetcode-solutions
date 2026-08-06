from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)

        ans = 1
        while ans in s:
            ans <<= 1

        return ans