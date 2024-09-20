class Solution:
    def maxValue(self, numElements: int, targetIndex: int, maxTotal: int) -> int:
        maxTotal -= numElements
        low, high = 0, maxTotal
        while low < high:
            midPoint = (low + high) // 2
            if self.computeTotal(numElements, targetIndex, midPoint) >= maxTotal:
                high = midPoint
            else:
                low = midPoint + 1
        return low if self.computeTotal(numElements, targetIndex, low) > maxTotal else low + 1
    def computeTotal(self, numElements: int, targetIndex: int, potentialValue: int) -> int:
        leftLimit = min(targetIndex, potentialValue - 1)
        rightLimit = min(numElements - targetIndex - 1, potentialValue)
        leftContribution = ((potentialValue - 1) + (potentialValue - 1 - leftLimit + 1)) * leftLimit // 2
        rightContribution = (potentialValue + (potentialValue - rightLimit)) * (rightLimit + 1) // 2
        return leftContribution + rightContribution
