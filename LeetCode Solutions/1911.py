class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0
        for num in nums:
            even_sum = max(even_sum, odd_sum + num)
            odd_sum = max(odd_sum, even_sum - num)
        return even_sum
