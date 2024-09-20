from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        stack = []
        max_sum = 0
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                left = stack[-1] if stack else -1
                max_sum = max(max_sum, nums[j] * (prefix_sum[i] - prefix_sum[left + 1]))
            stack.append(i)
        while stack:
            j = stack.pop()
            left = stack[-1] if stack else -1
            max_sum = max(max_sum, nums[j] * (prefix_sum[n] - prefix_sum[left + 1]))
        return max_sum % (10**9 + 7)
