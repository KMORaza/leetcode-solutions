from typing import List
import heapq
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_xor = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix_xor[i][j] = matrix[i][j]
                if i > 0:
                    prefix_xor[i][j] ^= prefix_xor[i - 1][j]
                if j > 0:
                    prefix_xor[i][j] ^= prefix_xor[i][j - 1]
                if i > 0 and j > 0:
                    prefix_xor[i][j] ^= prefix_xor[i - 1][j - 1]
        values = []
        for i in range(m):
            for j in range(n):
                values.append(prefix_xor[i][j])
        return heapq.nlargest(k, values)[-1]
