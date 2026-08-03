from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest_length = 0
        current_length = 0
        for num in nums:
            if num == max_val:
                current_length += 1
            else:
                if current_length > longest_length:
                    longest_length = current_length
                current_length = 0
        if current_length > longest_length:
            longest_length = current_length
        return longest_length
