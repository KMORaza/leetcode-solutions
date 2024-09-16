from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        max_val = 0
        for sign1 in [1, -1]:
            for sign2 in [1, -1]:
                max_temp = float('-inf')
                min_temp = float('inf')
                for i in range(n):
                    value = sign1 * arr1[i] + sign2 * arr2[i] + i
                    max_temp = max(max_temp, value)
                    min_temp = min(min_temp, value)
                max_val = max(max_val, max_temp - min_temp)
        return max_val
