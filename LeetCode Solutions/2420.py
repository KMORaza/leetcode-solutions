class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 2 * k + 1:
            return []

        left_decreasing = [1] * n
        right_increasing = [1] * n

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left_decreasing[i] = left_decreasing[i - 1] + 1
            else:
                left_decreasing[i] = 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right_increasing[i] = right_increasing[i + 1] + 1
            else:
                right_increasing[i] = 1

        result = []
        for i in range(k, n - k):
            if left_decreasing[i - 1] >= k and right_increasing[i + 1] >= k:
                result.append(i)

        return result