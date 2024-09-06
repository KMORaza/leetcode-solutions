class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct_nums = set(nums)
        sorted_nums = sorted(distinct_nums, reverse=True)
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        else:
            return sorted_nums[0]