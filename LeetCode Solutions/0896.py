from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums:
            return True
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing
