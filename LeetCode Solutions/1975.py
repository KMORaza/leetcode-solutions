from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    negative_count += 1
                total_sum += abs(num)
                min_abs_value = min(min_abs_value, abs(num))
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_value
