from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(d: int) -> int:
            return sum(math.ceil(num / d) for num in nums)
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if compute_sum(mid) <= threshold:
                high = mid
            else:
                low = mid + 1
        return low
