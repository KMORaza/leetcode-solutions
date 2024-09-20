from typing import List
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        closest = float('inf')
        def calculateCost(currentCost: int, index: int):
            nonlocal closest
            if index == len(toppingCosts):
                if abs(currentCost - target) < abs(closest - target) or (
                    abs(currentCost - target) == abs(closest - target) and currentCost < closest):
                    closest = currentCost
                return
            calculateCost(currentCost, index + 1)
            calculateCost(currentCost + toppingCosts[index], index + 1)
            calculateCost(currentCost + 2 * toppingCosts[index], index + 1)
        for base in baseCosts:
            calculateCost(base, 0)
        return closest
