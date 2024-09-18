from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        sorted_nums = sorted(nums, reverse=True)
        subsequence_sum = 0
        subsequence = []
        for num in sorted_nums:
            subsequence_sum += num
            subsequence.append(num)
            if subsequence_sum > total_sum - subsequence_sum:
                break
        return subsequence
