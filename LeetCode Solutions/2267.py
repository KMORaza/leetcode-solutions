class Solution:
    def hasValidPath(self, grid):
        height = len(grid)
        width = len(grid[0])
        memoization = [[[None] * (height + width) for _ in range(width)] for _ in range(height)]
        return self._isPathValid(grid, 0, 0, 0, memoization)
    def _isPathValid(self, grid, row, col, countDifference, memoization):
        if row == len(grid) or col == len(grid[0]):
            return False
        countDifference += 1 if grid[row][col] == '(' else -1
        if countDifference < 0:
            return False
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return countDifference == 0
        if memoization[row][col][countDifference] is not None:
            return memoization[row][col][countDifference]
        memoization[row][col][countDifference] = (self._isPathValid(grid, row + 1, col, countDifference, memoization) or
                                                   self._isPathValid(grid, row, col + 1, countDifference, memoization))
        return memoization[row][col][countDifference]
