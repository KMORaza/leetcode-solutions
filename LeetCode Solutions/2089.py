from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        target_indices = []
        for index, num in enumerate(nums):
            if num == target:
                target_indices.append(index)
        return target_indices
