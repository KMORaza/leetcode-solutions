from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i - 1][j - 1] +
                                prefix[i - 1][j] +
                                prefix[i][j - 1] -
                                prefix[i - 1][j - 1])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                r2 = min(m - 1, i + k)
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)
                result[i][j] = (prefix[r2 + 1][c2 + 1] -
                                prefix[r1][c2 + 1] -
                                prefix[r2 + 1][c1] +
                                prefix[r1][c1])
        return result
