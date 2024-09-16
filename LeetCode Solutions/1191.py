class Solution:
    def kConcatenationMaxSum(self, nums, repeats):
        X = 1000000007
        effective_size = len(nums) * (1 if repeats == 1 else 2)
        total = sum(nums)
        def max_subarray_sum(arr, length):
            max_sum = 0
            current_sum = 0
            for i in range(length):
                value = arr[i % len(arr)]
                current_sum = max(value, current_sum + value)
                max_sum = max(max_sum, current_sum)
            return max_sum
        if total > 0 and repeats > 2:
            return (max_subarray_sum(nums, effective_size) + total * (repeats - 2)) % X
        return max_subarray_sum(nums, effective_size) % X
