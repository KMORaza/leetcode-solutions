from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        peak = 0
        while peak < n - 1 and arr[peak] < arr[peak + 1]:
            peak += 1
        if peak == 0 or peak == n - 1:
            return False
        while peak < n - 1 and arr[peak] > arr[peak + 1]:
            peak += 1
        return peak == n - 1
