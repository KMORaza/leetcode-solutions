from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique_nums = []
        for num in nums:
            if not unique_nums or unique_nums[-1] != num:
                unique_nums.append(num)
        count = 0
        n = len(unique_nums)
        for i in range(1, n - 1):
            if (unique_nums[i] > unique_nums[i - 1] and unique_nums[i] > unique_nums[i + 1]) or \
               (unique_nums[i] < unique_nums[i - 1] and unique_nums[i] < unique_nums[i + 1]):
                count += 1
        return count