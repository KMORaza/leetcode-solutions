from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(len1: int, len2: int) -> int:
            prefix_sum = [0] * (len(nums) + 1)
            for i in range(1, len(prefix_sum)):
                prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
            max_len1_sum = 0
            max_sum = 0
            for i in range(len1 + len2 - 1, len(nums)):
                max_len1_sum = max(max_len1_sum, prefix_sum[i - len2 + 1] - prefix_sum[i - len1 - len2 + 1])
                max_sum = max(max_sum, max_len1_sum + prefix_sum[i + 1] - prefix_sum[i - len2 + 1])
            return max_sum
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))
