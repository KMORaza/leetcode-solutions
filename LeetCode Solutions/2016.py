from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = float('inf')
        max_diff = -1
        for num in nums:
            if num < min_value:
                min_value = num
            elif num > min_value:
                max_diff = max(max_diff, num - min_value)
        return max_diff if max_diff > 0 else -1