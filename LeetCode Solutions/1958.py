from typing import List
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opponent = 'W' if color == 'B' else 'B'
        directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            found_opponent = False
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == opponent:
                    found_opponent = True
                elif board[r][c] == color and found_opponent:
                    return True
                else:
                    break
                r += dr
                c += dc
        return False