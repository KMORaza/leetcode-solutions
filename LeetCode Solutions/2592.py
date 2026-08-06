class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0

        for j in range(n):
            if nums[j] > nums[i]:
                i += 1

        return i