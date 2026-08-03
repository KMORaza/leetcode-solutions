class Solution:
    def checkXMatrix(self, grid):
        n = len(grid)

        for i in range(n):
            for j in range(n):
                is_diagonal = (i == j) or (i + j == n - 1)
                if is_diagonal:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True