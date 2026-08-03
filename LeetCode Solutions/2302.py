class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        count = 0
        left = 0
        total_sum = 0
        for right in range(n):
            total_sum += nums[right]
            while total_sum * (right - left + 1) >= k and left <= right:
                total_sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
