from typing import List
MOD = 10**9 + 7
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total_sum = 0
        power_of_2 = [1] * n
        for i in range(1, n):
            power_of_2[i] = (power_of_2[i - 1] * 2) % MOD
        for i in range(n):
            max_contribution = power_of_2[i]
            min_contribution = power_of_2[n - i - 1]
            total_sum = (total_sum + (nums[i] * max_contribution - nums[i] * min_contribution)) % MOD
        return total_sum
