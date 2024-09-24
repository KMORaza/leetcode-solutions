from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            x = bin(mask).count('1')
            if x > n:
                continue
            for j in range(n):
                if mask & (1 << j) == 0:
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + (nums1[x] ^ nums2[j]))
        return dp[(1 << n) - 1]

