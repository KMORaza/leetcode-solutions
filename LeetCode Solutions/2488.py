class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_idx = nums.index(k)

        left_counts = {}
        left_counts[0] = 1
        balance = 0

        for i in range(k_idx - 1, -1, -1):
            if nums[i] < k:
                balance -= 1
            else:
                balance += 1
            left_counts[balance] = left_counts.get(balance, 0) + 1

        result = 0
        balance = 0

        for i in range(k_idx, n):
            if nums[i] < k:
                balance -= 1
            elif nums[i] > k:
                balance += 1

            result += left_counts.get(-balance, 0)
            result += left_counts.get(-balance + 1, 0)

        return result