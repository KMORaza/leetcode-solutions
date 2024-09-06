class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        total_sum = sum(nums)
        current_value = sum(i * num for i, num in enumerate(nums))
        max_value = current_value
        for i in range(1, n):
            current_value = current_value + total_sum - n * nums[-i]
            max_value = max(max_value, current_value)
        return max_value