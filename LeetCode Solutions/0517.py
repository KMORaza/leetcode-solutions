class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        if total_dresses % n != 0:
            return -1
        target = total_dresses // n
        max_moves = 0
        current_balance = 0
        for dresses in machines:
            imbalance = dresses - target
            current_balance += imbalance
            max_moves = max(max_moves, abs(current_balance), imbalance)
        return max_moves

