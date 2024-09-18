from typing import List
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]
        nums.sort()
        freq = freq[:n]
        freq.sort()
        result = sum(x * y for x, y in zip(nums, freq)) % (10**9 + 7)
        return result
