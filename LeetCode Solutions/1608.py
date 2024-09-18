from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(num >= x for num in nums) == x:
                return x
        return -1
