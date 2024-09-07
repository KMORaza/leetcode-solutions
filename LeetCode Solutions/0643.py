from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum / k
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            current_average = window_sum / k
            max_average = max(max_average, current_average)
        return max_average