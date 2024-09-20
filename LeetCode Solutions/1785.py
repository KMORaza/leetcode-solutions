from typing import List
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        difference = abs(current_sum - goal)
        return (difference + limit - 1) // limit
