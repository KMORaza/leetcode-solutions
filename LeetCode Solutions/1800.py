from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum
