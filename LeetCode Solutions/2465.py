class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        left, right = 0, len(nums) - 1

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            averages.add(avg)
            left += 1
            right -= 1

        return len(averages)