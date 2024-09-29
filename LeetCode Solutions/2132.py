class Solution:
    def possibleToStamp(self, canvas, stampHeight: int, stampWidth: int) -> bool:
        totalRows = len(canvas)
        totalCols = len(canvas[0])
        PrefixSum = [[0] * (totalCols + 1) for _ in range(totalRows + 1)]
        StampingWays = [[0] * (totalCols + 1) for _ in range(totalRows + 1)]
        canPlace = [[0] * totalCols for _ in range(totalRows)]
        for row in range(totalRows):
            for col in range(totalCols):
                PrefixSum[row + 1][col + 1] = (PrefixSum[row + 1][col] +
                                                 PrefixSum[row][col + 1] -
                                                 PrefixSum[row][col] + canvas[row][col])
                if row + 1 >= stampHeight and col + 1 >= stampWidth:
                    topLeftRow = row - stampHeight + 1
                    topLeftCol = col - stampWidth + 1
                    if (PrefixSum[row + 1][col + 1] -
                        PrefixSum[topLeftRow][col + 1] -
                        PrefixSum[row + 1][topLeftCol] +
                        PrefixSum[topLeftRow][topLeftCol] == 0):
                        canPlace[row][col] = 1
        for row in range(totalRows):
            for col in range(totalCols):
                StampingWays[row + 1][col + 1] = (StampingWays[row + 1][col] +
                                                    StampingWays[row][col + 1] -
                                                    StampingWays[row][col] + canPlace[row][col])
        for row in range(totalRows):
            for col in range(totalCols):
                if canvas[row][col] == 0:
                    bottomRightRow = min(row + stampHeight, totalRows)
                    bottomRightCol = min(col + stampWidth, totalCols)
                    if (StampingWays[bottomRightRow][bottomRightCol] -
                        StampingWays[row][bottomRightCol] -
                        StampingWays[bottomRightRow][col] +
                        StampingWays[row][col] == 0):
                        return False
        return True
