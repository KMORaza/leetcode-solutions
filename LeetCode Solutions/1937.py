class Solution:
    def maxPoints(self, dataPoints):
        width = len(dataPoints[0])
        maxValue = [0] * width
        for rowData in dataPoints:
            leftToRightMax = [0] * width
            tempMax = 0
            for colIndex in range(width):
                tempMax = max(tempMax - 1, maxValue[colIndex])
                leftToRightMax[colIndex] = tempMax
            rightToLeftMax = [0] * width
            tempMax = 0
            for colIndex in range(width - 1, -1, -1):
                tempMax = max(tempMax - 1, maxValue[colIndex])
                rightToLeftMax[colIndex] = tempMax
            for colIndex in range(width):
                maxValue[colIndex] = max(leftToRightMax[colIndex], rightToLeftMax[colIndex]) + rowData[colIndex]
        return max(maxValue)