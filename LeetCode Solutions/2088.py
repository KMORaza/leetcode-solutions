class Solution:
    def countPyramids(self, pyramidGrid):
        return self.computePyramidCount(self.invertGrid(pyramidGrid)) + self.computePyramidCount(pyramidGrid)
    def computePyramidCount(self, heightMap):
        totalPyramids = 0
        rowCount = len(heightMap)
        colCount = len(heightMap[0]) if rowCount > 0 else 0
        for currentRow in range(rowCount - 2, -1, -1):
            for currentCol in range(1, colCount - 1):
                if heightMap[currentRow][currentCol] == 1:
                    heightMap[currentRow][currentCol] = min(heightMap[currentRow + 1][currentCol - 1],
                                                            heightMap[currentRow + 1][currentCol],
                                                            heightMap[currentRow + 1][currentCol + 1]) + 1
                    totalPyramids += heightMap[currentRow][currentCol] - 1
        return totalPyramids
    def invertGrid(self, originalMatrix):
        return [originalMatrix[len(originalMatrix) - i - 1][:] for i in range(len(originalMatrix))]