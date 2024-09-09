class Solution:
    def bestRotation(self, nums):
        n = len(nums)
        rotate = [0] * n
        for i in range(n):
            rotate[(i - nums[i] + 1 + n) % n] -= 1
        for i in range(1, n):
            rotate[i] += rotate[i - 1] + 1
        max_value = float('-inf')
        max_index = 0
        for i in range(n):
            if rotate[i] > max_value:
                max_value = rotate[i]
                max_index = i
        return max_index
