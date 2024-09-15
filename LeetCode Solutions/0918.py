from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane_max_subarray(arr):
            max_sum = float('-inf')
            current_sum = 0
            for num in arr:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        def kadane_min_subarray(arr):
            min_sum = float('inf')
            current_sum = 0
            for num in arr:
                current_sum = min(num, current_sum + num)
                min_sum = min(min_sum, current_sum)
            return min_sum
        max_kadane = kadane_max_subarray(nums)
        total_sum = sum(nums)
        min_kadane = kadane_min_subarray(nums)
        if max_kadane < 0:
            return max_kadane
        max_circular = total_sum - min_kadane
        return max(max_kadane, max_circular)
