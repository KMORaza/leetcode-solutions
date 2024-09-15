from typing import List

X = int(1e9 + 7)


class Solution:
    def __init__(self):
        self.grid = []
        self.size = 0
        self.scoreMatrix = []
        self.pathCountMatrix = []

    def pathsWithMaxScore(self, grid: List[str]) -> List[int]:
        self.grid = grid
        self.size = len(grid)
        self.scoreMatrix = [[-1] * self.size for _ in range(self.size)]
        self.pathCountMatrix = [[0] * self.size for _ in range(self.size)]
        self.scoreMatrix[self.size - 1][self.size - 1] = 0
        self.pathCountMatrix[self.size - 1][self.size - 1] = 1
        for row in range(self.size - 1, -1, -1):
            for col in range(self.size - 1, -1, -1):
                self._checkAndUpdate(row, col, row + 1, col)
                self._checkAndUpdate(row, col, row, col + 1)
                self._checkAndUpdate(row, col, row + 1, col + 1)
                if self.scoreMatrix[row][col] != -1:
                    cell = self.grid[row][col]
                    if '0' <= cell <= '9':
                        self.scoreMatrix[row][col] += int(cell)
        result = [0, 0]
        if self.scoreMatrix[0][0] != -1:
            result[0] = self.scoreMatrix[0][0]
            result[1] = self.pathCountMatrix[0][0]
        return result

    def _checkAndUpdate(self, currentRow: int, currentCol: int, prevRow: int, prevCol: int):
        if prevRow >= self.size or prevCol >= self.size \
                or self.scoreMatrix[prevRow][prevCol] == -1 \
                or self.grid[currentRow][currentCol] == 'X' \
                or self.grid[currentRow][currentCol] == 'S':
            return
        if self.scoreMatrix[prevRow][prevCol] > self.scoreMatrix[currentRow][currentCol]:
            self.scoreMatrix[currentRow][currentCol] = self.scoreMatrix[prevRow][prevCol]
            self.pathCountMatrix[currentRow][currentCol] = self.pathCountMatrix[prevRow][prevCol]
        elif self.scoreMatrix[prevRow][prevCol] == self.scoreMatrix[currentRow][currentCol]:
            self.pathCountMatrix[currentRow][currentCol] = (self.pathCountMatrix[currentRow][currentCol] +
                                                            self.pathCountMatrix[prevRow][prevCol]) % X
