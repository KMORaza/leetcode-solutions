class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        prev = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                parts = (nums[i] + prev - 1) // prev
                operations += parts - 1
                prev = nums[i] // parts

        return operations