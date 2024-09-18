class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        return mat
