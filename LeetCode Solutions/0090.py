class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            results.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        nums.sort()
        results = []
        backtrack(0, [])
        return results