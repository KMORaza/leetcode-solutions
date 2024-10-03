class Solution:
    def maximumWhiteTiles(self, tileArray, carpetSize):
        tileArray.sort(key=lambda x: x[0])
        numTiles = len(tileArray)
        currentCoverage = 0
        bestCoverage = 0
        endPointer = 0
        for startPointer in range(numTiles):
            while endPointer < numTiles and tileArray[endPointer][1] - tileArray[startPointer][0] + 1 <= carpetSize:
                currentCoverage += tileArray[endPointer][1] - tileArray[endPointer][0] + 1
                endPointer += 1
            if endPointer < numTiles and tileArray[startPointer][0] + carpetSize > tileArray[endPointer][0]:
                bestCoverage = max(bestCoverage, currentCoverage + tileArray[startPointer][0] + carpetSize - tileArray[endPointer][0])
            else:
                bestCoverage = max(bestCoverage, currentCoverage)
            currentCoverage -= (tileArray[startPointer][1] - tileArray[startPointer][0] + 1)
        return bestCoverage