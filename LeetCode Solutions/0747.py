from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = -1
        max_index = -1
        for i, num in enumerate(nums):
            if num > max_value:
                max_value = num
                max_index = i
        for i, num in enumerate(nums):
            if i != max_index and max_value < 2 * num:
                return -1
        return max_index
