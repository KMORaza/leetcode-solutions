class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            matrix[r1][c1] += 1
            if c2 + 1 < n:
                matrix[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                matrix[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                matrix[r2 + 1][c2 + 1] += 1

        for i in range(n):
            for j in range(n):
                if i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j - 1]
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i - 1][j - 1]

        return matrix