from typing import List
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums)}
        for old_num, new_num in operations:
            index = index_map[old_num]
            nums[index] = new_num
            del index_map[old_num]
            index_map[new_num] = index
        return nums