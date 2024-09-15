from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getCellNumber(row: int, col: int) -> int:
            if row % 2 == 0:
                return row * n + col + 1
            else:
                return row * n + (n - col)
        def getRowCol(num: int) -> (int, int):
            num -= 1
            row = num // n
            col = num % n
            if row % 2 == 1:
                col = n - 1 - col
            return (n - 1 - row, col)
        visited = set()
        queue = deque([(1, 0)])
        visited.add(1)
        while queue:
            cell, moves = queue.popleft()
            if cell == n * n:
                return moves
            for dice in range(1, 7):
                next_cell = cell + dice
                if next_cell > n * n:
                    continue
                row, col = getRowCol(next_cell)
                if board[row][col] != -1:
                    next_cell = board[row][col]
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, moves + 1))
        return -1
