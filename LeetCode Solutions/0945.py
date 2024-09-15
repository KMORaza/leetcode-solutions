class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        increments = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                increment_needed = prev + 1 - nums[i]
                increments += increment_needed
                nums[i] = prev + 1
            prev = nums[i]
        return increments
