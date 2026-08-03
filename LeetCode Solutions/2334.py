class Solution:
    def validSubarraySize(self, nums, threshold):
        n = len(nums)

        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            length = right[i] - left[i] - 1
            if nums[i] > threshold / length:
                return length

        return -1