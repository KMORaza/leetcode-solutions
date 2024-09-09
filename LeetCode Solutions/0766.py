from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        m, n = len(matrix), len(matrix[0])
        def checkDiagonal(r: int, c: int) -> bool:
            val = matrix[r][c]
            while r < m and c < n:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1
            return True
        for j in range(n):
            if not checkDiagonal(0, j):
                return False
        for i in range(1, m):
            if not checkDiagonal(i, 0):
                return False
        return True
