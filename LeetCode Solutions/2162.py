class Solution:
    def minCostSetTime(self, startingDigit: int, travelCost: int, pressCost: int, targetDuration: int) -> int:
        hours = targetDuration // 60
        minutes = targetDuration % 60
        return min(
            self.computeEntryCost(hours, minutes, startingDigit, travelCost, pressCost),
            self.computeEntryCost(hours - 1, minutes + 60, startingDigit, travelCost, pressCost)
        )
    def computeEntryCost(self, hourPart: int, minutePart: int, previousKey: int, travelCost: int, pressCost: int) -> int:
        if hourPart < 0 or hourPart > 99 or minutePart < 0 or minutePart > 99:
            return float('inf')
        timeComponents = [hourPart // 10, hourPart % 10, minutePart // 10, minutePart % 10]
        nonZeroIndex = 0
        while nonZeroIndex < 4 and timeComponents[nonZeroIndex] == 0:
            nonZeroIndex += 1
        totalExpense = 0
        for i in range(nonZeroIndex, 4):
            if timeComponents[i] != previousKey:
                totalExpense += travelCost
            totalExpense += pressCost
            previousKey = timeComponents[i]
        return totalExpense