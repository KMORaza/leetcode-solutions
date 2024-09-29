from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        window_sum = 0
        if n < 2 * k + 1:
            return result
        for i in range(2 * k + 1):
            window_sum += nums[i]
        result[k] = window_sum // (2 * k + 1)
        for i in range(2 * k + 1, n):
            window_sum += nums[i] - nums[i - (2 * k + 1)]
            result[i - k] = window_sum // (2 * k + 1)
        return result
