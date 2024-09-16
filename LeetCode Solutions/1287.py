from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4
        i = 0
        while i < n:
            candidate = arr[i]
            if i + threshold < n and arr[i + threshold] == candidate:
                return candidate
            while i < n and arr[i] == candidate:
                i += 1
        return -1
