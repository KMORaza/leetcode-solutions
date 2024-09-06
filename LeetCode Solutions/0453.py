from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        moves = sum(num - min_value for num in nums)
        return moves
