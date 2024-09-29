from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: (-x[0], x[1]))
        result = sorted(indexed_nums[:k], key=lambda x: x[1])
        return [num for num, _ in result]
