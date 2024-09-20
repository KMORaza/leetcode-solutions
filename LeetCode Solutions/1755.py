from typing import List
import bisect
class Solution:
    def minAbsDifference(self, arr: List[int], target: int) -> int:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        min_diff = float('inf')
        left_sums = []
        right_sums = []
        self.calculate_sums(left_arr, 0, 0, left_sums)
        self.calculate_sums(right_arr, 0, 0, right_sums)
        right_sums.sort()
        for left_sum in left_sums:
            required = target - left_sum
            index = bisect.bisect_left(right_sums, required)
            if index < len(right_sums):
                min_diff = min(min_diff, abs(target - left_sum - right_sums[index]))
            if index > 0:
                min_diff = min(min_diff, abs(target - left_sum - right_sums[index - 1]))
        return min_diff
    def calculate_sums(self, nums: List[int], idx: int, current_sum: int, sums: List[int]) -> None:
        if idx == len(nums):
            sums.append(current_sum)
            return
        self.calculate_sums(nums, idx + 1, current_sum + nums[idx], sums)
        self.calculate_sums(nums, idx + 1, current_sum, sums)
