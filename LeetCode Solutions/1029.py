from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = [(cost[0] - cost[1], cost[0], cost[1]) for cost in costs]
        differences.sort()
        total_cost = 0
        n = len(costs) // 2
        for i in range(n):
            total_cost += differences[i][1]
        for i in range(n, len(differences)):
            total_cost += differences[i][2]
        return total_cost
