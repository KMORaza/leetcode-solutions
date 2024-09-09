from typing import List
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        if xor_sum == 0:
            return True
        return len(nums) % 2 == 0
