from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max1, max2 = float('-inf'), float('-inf')
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
