from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            total_kids = sum(candy // mid for candy in candies)
            if total_kids >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
