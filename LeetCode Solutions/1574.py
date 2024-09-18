from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        right = n - 1
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1
        min_length = right
        for i in range(left + 1):
            while right < n and arr[i] > arr[right]:
                right += 1
            min_length = min(min_length, right - (i + 1))
        return min_length
