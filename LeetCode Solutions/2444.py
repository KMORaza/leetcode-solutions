class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        result = 0
        min_pos = max_pos = -1
        left = 0

        for right in range(n):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                min_pos = max_pos = -1
                continue

            if nums[right] == minK:
                min_pos = right
            if nums[right] == maxK:
                max_pos = right

            if min_pos != -1 and max_pos != -1:
                result += max(0, min(min_pos, max_pos) - left + 1)

        return result