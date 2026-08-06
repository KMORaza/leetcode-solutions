class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        moves = [None] * (n * n)

        for i in range(n):
            for j in range(n):
                moves[grid[i][j]] = (i, j)

        if moves[0] != (0, 0):
            return False

        for i in range(1, n * n):
            prev_r, prev_c = moves[i - 1]
            curr_r, curr_c = moves[i]

            dr = abs(curr_r - prev_r)
            dc = abs(curr_c - prev_c)

            if not ((dr == 2 and dc == 1) or (dr == 1 and dc == 2)):
                return False

        return True