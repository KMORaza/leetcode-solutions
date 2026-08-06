from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        for i in range(n):
            l = bisect_left(nums, lower - nums[i], i + 1)
            r = bisect_right(nums, upper - nums[i], i + 1)
            ans += r - l

        return ans