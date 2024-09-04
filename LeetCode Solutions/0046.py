class Solution:
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                results.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        results = []
        backtrack(0)
        return results
