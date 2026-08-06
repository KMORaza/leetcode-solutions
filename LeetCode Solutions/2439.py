class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        max_avg = 0

        for i, num in enumerate(nums):
            total += num
            avg = (total + i) // (i + 1)
            max_avg = max(max_avg, avg)

        return max_avg