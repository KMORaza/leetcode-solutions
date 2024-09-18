class Solution:
    def stoneGameVII(self, nums):
        length = len(nums)
        cache = [[None] * length for _ in range(length)]
        cumulative = [0] * (length + 1)
        for index in range(length):
            cumulative[index + 1] = cumulative[index] + nums[index]
        return self._helper(nums, 0, length - 1, cumulative, cache)
    def _helper(self, nums, start, end, cumulative, cache):
        if start == end:
            return 0
        if cache[start][end] is not None:
            return cache[start][end]
        left_score = cumulative[end + 1] - cumulative[start + 1] - self._helper(nums, start + 1, end, cumulative, cache)
        right_score = cumulative[end] - cumulative[start] - self._helper(nums, start, end - 1, cumulative, cache)
        cache[start][end] = max(left_score, right_score)
        return cache[start][end]
