from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
        return result
