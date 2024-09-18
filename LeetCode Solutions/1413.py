class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumulative_sum = 0
        min_cumulative_sum = float('inf')
        for num in nums:
            cumulative_sum += num
            min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)
        return max(1 - min_cumulative_sum, 1)
