from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)
        while low < high:
            mid = (low + high) // 2
            stores_needed = sum((q + mid - 1) // mid for q in quantities)
            if stores_needed <= n:
                high = mid
            else:
                low = mid + 1
        return low