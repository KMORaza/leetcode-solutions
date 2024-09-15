from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_x, rook_y = i, j
                    break
        captures = 0
        for i in range(rook_x - 1, -1, -1):
            if board[i][rook_y] == 'B':
                break
            elif board[i][rook_y] == 'p':
                captures += 1
                break
        for i in range(rook_x + 1, 8):
            if board[i][rook_y] == 'B':
                break
            elif board[i][rook_y] == 'p':
                captures += 1
                break
        for j in range(rook_y - 1, -1, -1):
            if board[rook_x][j] == 'B':
                break
            elif board[rook_x][j] == 'p':
                captures += 1
                break
        for j in range(rook_y + 1, 8):
            if board[rook_x][j] == 'B':
                break
            elif board[rook_x][j] == 'p':
                captures += 1
                break
        return captures
