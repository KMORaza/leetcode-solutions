from typing import List
from bisect import bisect_left
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        x = 10**9 + 7
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        power_of_two = [1] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            power_of_two[i] = (power_of_two[i - 1] * 2) % x
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + power_of_two[right - left]) % x
                left += 1
            else:
                right -= 1
        return count
