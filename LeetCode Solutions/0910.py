from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        min_num = nums[0]
        max_num = nums[-1]
        initial_range = max_num - min_num
        smallest_range = initial_range
        for i in range(len(nums) - 1):
            current_range = max(nums[-1] - k, nums[i] + k) - min(nums[0] + k, nums[i + 1] - k)
            smallest_range = min(smallest_range, current_range)
        return smallest_range
