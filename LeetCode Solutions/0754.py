class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        numMoves = 0
        sum_moves = 0
        while True:
            numMoves += 1
            sum_moves += numMoves
            if sum_moves >= target and (sum_moves - target) % 2 == 0:
                return numMoves
