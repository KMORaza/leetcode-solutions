from typing import List
import bisect
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            left = bisect.bisect_left(arr2, num - d)
            right = bisect.bisect_left(arr2, num + d + 1)
            if left == right:
                count += 1
        return count
