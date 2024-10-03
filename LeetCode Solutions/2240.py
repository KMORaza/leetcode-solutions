class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        for pens in range(total // cost1 + 1):
            remaining_budget = total - pens * cost1
            max_pencils = remaining_budget // cost2
            ways += max_pencils + 1
        return ways
