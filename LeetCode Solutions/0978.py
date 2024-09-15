from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        if n == 1:
            return 1
        max_len = 1
        inc_len = dec_len = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc_len = dec_len + 1
                dec_len = 1
            elif arr[i] < arr[i - 1]:
                dec_len = inc_len + 1
                inc_len = 1
            else:
                inc_len = dec_len = 1
            max_len = max(max_len, inc_len, dec_len)
        return max_len
