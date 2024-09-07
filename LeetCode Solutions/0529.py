from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def count_mines(r: int, c: int) -> int:
            count = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count
        def reveal(r: int, c: int):
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'E':
                return
            mine_count = count_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    reveal(nr, nc)
        m, n = len(board), len(board[0])
        clickr, clickc = click
        if board[clickr][clickc] == 'M':
            board[clickr][clickc] = 'X'
        else:
            reveal(clickr, clickc)
        return board
