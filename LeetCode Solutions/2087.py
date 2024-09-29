from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        startRow, startCol = startPos
        homeRow, homeCol = homePos
        total_cost = 0
        if startRow < homeRow:
            total_cost += sum(rowCosts[startRow + 1: homeRow + 1])
        elif startRow > homeRow:
            total_cost += sum(rowCosts[homeRow: startRow])
        if startCol < homeCol:
            total_cost += sum(colCosts[startCol + 1: homeCol + 1])
        elif startCol > homeCol:
            total_cost += sum(colCosts[homeCol: startCol])
        return total_cost
