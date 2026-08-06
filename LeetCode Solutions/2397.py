class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        for i in range(m):
            for j in range(n):
                rows[i] |= mat[i][j] << j

        max_covered = 0
        for mask in range(1 << n):
            if bin(mask).count('1') != cols:
                continue

            covered = 0
            for i in range(m):
                if (rows[i] & mask) == rows[i]:
                    covered += 1

            max_covered = max(max_covered, covered)

        return max_covered