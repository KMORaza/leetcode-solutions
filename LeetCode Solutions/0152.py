class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * max_product, num * min_product)
            min_product = min(num, num * max_product, num * min_product)
            max_product = temp_max
            result = max(result, max_product)
        return result
