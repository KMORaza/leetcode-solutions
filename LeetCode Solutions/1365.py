from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_to_index = {}
        for index, num in enumerate(sorted_nums):
            if num not in num_to_index:
                num_to_index[num] = index
        result = [num_to_index[num] for num in nums]
        return result
