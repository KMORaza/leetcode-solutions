from typing import List
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        num_group1 = len(cost)
        num_group2 = len(cost[0])
        memo = [[None] * (1 << num_group2) for _ in range(num_group1)]
        minCostPerPoint = [float('inf')] * num_group2
        for j in range(num_group2):
            minCostIndex = 0
            for i in range(1, num_group1):
                if cost[i][j] < cost[minCostIndex][j]:
                    minCostIndex = i
            minCostPerPoint[j] = cost[minCostIndex][j]
        return self._calculateMinimumCost(cost, 0, 0, minCostPerPoint, memo)
    def _calculateMinimumCost(self, cost: List[List[int]], index: int, bitmask: int, minCostPerPoint: List[int], memo: List[List[int]]) -> int:
        if index == len(cost):
            total_cost = 0
            for j in range(len(cost[0])):
                if not (bitmask >> j & 1):
                    total_cost += minCostPerPoint[j]
            return total_cost
        if memo[index][bitmask] is not None:
            return memo[index][bitmask]
        min_cost = float('inf')
        for j in range(len(cost[0])):
            min_cost = min(min_cost, cost[index][j] + self._calculateMinimumCost(cost, index + 1, bitmask | (1 << j), minCostPerPoint, memo))
        memo[index][bitmask] = min_cost
        return min_cost
