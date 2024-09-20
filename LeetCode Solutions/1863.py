from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        total_subsets = 1 << n
        for i in range(total_subsets):
            subset_xor = 0
            for j in range(n):
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        return total_sum
