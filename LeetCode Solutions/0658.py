from typing import List
import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect.bisect_left(arr, x)
        left, right = pos - 1, pos
        result = []
        while k > 0:
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right >= len(arr):
                result.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            k -= 1
        return sorted(result)
