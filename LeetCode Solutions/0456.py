from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        max_k = float('-inf')
        for num in reversed(nums):
            if num < max_k:
                return True
            while stack and stack[-1] < num:
                max_k = stack.pop()
            stack.append(num)
        return False
