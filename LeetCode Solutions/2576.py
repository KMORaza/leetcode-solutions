from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        j = (len(nums) + 1) // 2
        count = 0

        while i < len(nums) // 2 and j < len(nums):
            if 2 * nums[i] <= nums[j]:
                count += 2
                i += 1
                j += 1
            else:
                j += 1

        return count