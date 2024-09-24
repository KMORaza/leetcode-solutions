class Solution:
    def reductionOperations(self, inputArray):
        operationCount = 0
        inputArray.sort()
        for currentIndex in range(len(inputArray) - 1, 0, -1):
            if inputArray[currentIndex] != inputArray[currentIndex - 1]:
                operationCount += len(inputArray) - currentIndex
        return operationCount
