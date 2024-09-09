from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays_with_max_at_most(max_val: int) -> int:
            count = 0
            start = 0
            for end in range(len(nums)):
                if nums[end] > max_val:
                    start = end + 1
                count += end - start + 1
            return count
        count_right = count_subarrays_with_max_at_most(right)
        count_left = count_subarrays_with_max_at_most(left - 1)
        return count_right - count_left
