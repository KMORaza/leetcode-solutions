from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest