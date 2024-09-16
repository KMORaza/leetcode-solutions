from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        mismatch_count = sum(1 for original, sorted_ in zip(heights, sorted_heights) if original != sorted_)
        return mismatch_count
