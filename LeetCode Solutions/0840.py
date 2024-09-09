class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagicSquare(subgrid):
            nums = [subgrid[i][j] for i in range(3) for j in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            magic_sum = 15
            if not all(sum(subgrid[i]) == magic_sum for i in range(3)):
                return False
            if not all(sum(subgrid[i][j] for i in range(3)) == magic_sum for j in range(3)):
                return False
            if not (sum(subgrid[i][i] for i in range(3)) == magic_sum and
                    sum(subgrid[i][2 - i] for i in range(3)) == magic_sum):
                return False
            return True
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                subgrid = [grid[i + x][j:j + 3] for x in range(3)]
                if isMagicSquare(subgrid):
                    count += 1
        return count
