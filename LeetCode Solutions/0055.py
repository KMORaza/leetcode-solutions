class Solution:
    def canJump(self, nums):
        farthest = 0
        n = len(nums)
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        return False
