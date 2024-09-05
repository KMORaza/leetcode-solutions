class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patches = 0
        coverage = 0
        index = 0
        m = len(nums)
        while coverage < n:
            if index < m and nums[index] <= coverage + 1:
                coverage += nums[index]
                index += 1
            else:
                coverage += coverage + 1
                patches += 1
        return patches
