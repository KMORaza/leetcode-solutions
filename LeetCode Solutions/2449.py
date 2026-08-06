class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda x: (x % 2, x))
        target.sort(key=lambda x: (x % 2, x))

        operations = 0
        for i in range(len(nums)):
            diff = nums[i] - target[i]
            if diff > 0:
                operations += diff // 2

        return operations