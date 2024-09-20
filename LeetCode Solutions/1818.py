from typing import List
class Solution:
    def minAbsoluteSumDiff(self, arrayA: List[int], arrayB: List[int]) -> int:
        x = 10**9 + 7
        totalDiff = 0
        maxImprovement = 0
        sortedArrayA = sorted(arrayA)
        for valueA, valueB in zip(arrayA, arrayB):
            currentDiff = abs(valueA - valueB)
            totalDiff += currentDiff
            closestIndex = self.binarySearch(sortedArrayA, valueB)
            if closestIndex < len(sortedArrayA):
                maxImprovement = max(maxImprovement, currentDiff - abs(sortedArrayA[closestIndex] - valueB))
            if closestIndex > 0:
                maxImprovement = max(maxImprovement, currentDiff - abs(sortedArrayA[closestIndex - 1] - valueB))
        return (totalDiff - maxImprovement) % x
    def binarySearch(self, sortedArray: List[int], target: int) -> int:
        low, high = 0, len(sortedArray)
        while low < high:
            mid = (low + high) // 2
            if sortedArray[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
