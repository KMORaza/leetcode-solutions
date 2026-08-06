class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = -1

        for num in nums:
            current = num
            streak = 0

            while current in num_set:
                streak += 1
                current = current * current
                if current > 10 ** 5:
                    break

            if streak >= 2:
                max_streak = max(max_streak, streak)

        return max_streak