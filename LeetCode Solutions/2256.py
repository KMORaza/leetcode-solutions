from typing import List
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        min_diff = float('inf')
        min_index = -1
        left_sum = 0
        for i in range(n):
            left_sum += nums[i]
            left_avg = left_sum // (i + 1)
            right_avg = (total_sum - left_sum) // (n - i - 1) if i < n - 1 else 0
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                min_index = i
        return min_index
