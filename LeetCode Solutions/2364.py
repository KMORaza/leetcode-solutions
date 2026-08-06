class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2

        diff_count = {}
        for i, num in enumerate(nums):
            diff = num - i
            diff_count[diff] = diff_count.get(diff, 0) + 1

        good_pairs = 0
        for count in diff_count.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2

        return total_pairs - good_pairs