from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = sum(nums[i] for i in range(0, len(nums), 2))
        odd_sum = sum(nums[i] for i in range(1, len(nums), 2))
        count = 0
        even_count = 0
        odd_count = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum -= nums[i]
            else:
                odd_sum -= nums[i]
            if even_sum + odd_count == odd_sum + even_count:
                count += 1
            if i % 2 == 0:
                even_count += nums[i]
            else:
                odd_count += nums[i]
        return count
