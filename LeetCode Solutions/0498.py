from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}
        for i in range(m):
            for j in range(n):
                diag = i + j
                if diag not in diagonals:
                    diagonals[diag] = []
                diagonals[diag].append(mat[i][j])
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(reversed(diagonals.get(k, [])))
            else:
                result.extend(diagonals.get(k, []))
        return result
