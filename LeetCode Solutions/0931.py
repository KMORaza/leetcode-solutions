from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                min_below = matrix[i + 1][j]
                if j > 0:
                    min_below = min(min_below, matrix[i + 1][j - 1])
                if j < n - 1:
                    min_below = min(min_below, matrix[i + 1][j + 1])
                matrix[i][j] += min_below
        return min(matrix[0])
