from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        min_sum = 0
        max_stack = []
        for i in range(n):
            while max_stack and nums[max_stack[-1]] < nums[i]:
                j = max_stack.pop()
                left = max_stack[-1] if max_stack else -1
                max_sum += nums[j] * (i - j) * (j - left)
            max_stack.append(i)
        while max_stack:
            j = max_stack.pop()
            left = max_stack[-1] if max_stack else -1
            max_sum += nums[j] * (n - j) * (j - left)
        min_stack = []
        for i in range(n):
            while min_stack and nums[min_stack[-1]] > nums[i]:
                j = min_stack.pop()
                left = min_stack[-1] if min_stack else -1
                min_sum += nums[j] * (i - j) * (j - left)
            min_stack.append(i)
        while min_stack:
            j = min_stack.pop()
            left = min_stack[-1] if min_stack else -1
            min_sum += nums[j] * (n - j) * (j - left)
        return max_sum - min_sum