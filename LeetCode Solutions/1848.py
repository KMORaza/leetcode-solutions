from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')
        found = False
        for i, num in enumerate(nums):
            if num == target:
                found = True
                min_distance = min(min_distance, abs(i - start))
        return min_distance if found else -1
