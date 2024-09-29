from typing import List
class Solution:
    def countElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        count = 0
        for num in nums:
            if num > min_num and num < max_num:
                count += 1
        return count