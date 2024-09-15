class Solution:
    def isPrintable(self, targetGrid):
        from collections import defaultdict
        colorBoundingBox = {}
        numRows = len(targetGrid)
        numCols = len(targetGrid[0])
        for row in range(numRows):
            for col in range(numCols):
                color = targetGrid[row][col]
                if color not in colorBoundingBox:
                    colorBoundingBox[color] = [row, col, row, col]
                else:
                    boundingBox = colorBoundingBox[color]
                    boundingBox[0] = min(boundingBox[0], row)
                    boundingBox[1] = min(boundingBox[1], col)
                    boundingBox[2] = max(boundingBox[2], row)
                    boundingBox[3] = max(boundingBox[3], col)
        adjacencyList = defaultdict(set)
        for color in colorBoundingBox:
            for row in range(colorBoundingBox[color][0], colorBoundingBox[color][2] + 1):
                for col in range(colorBoundingBox[color][1], colorBoundingBox[color][3] + 1):
                    if targetGrid[row][col] != color:
                        adjacencyList[color].add(targetGrid[row][col])
        colorVisitState = {}
        def hasCycle(currentColor):
            if colorVisitState.get(currentColor, 0) == 1:
                return True
            if colorVisitState.get(currentColor, 0) == 2:
                return False
            colorVisitState[currentColor] = 1
            if currentColor in adjacencyList:
                for neighborColor in adjacencyList[currentColor]:
                    if hasCycle(neighborColor):
                        return True
            colorVisitState[currentColor] = 2
            return False
        for color in colorBoundingBox:
            if hasCycle(color):
                return False
        return True