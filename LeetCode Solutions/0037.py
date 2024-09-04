class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(board, row, col, num):
            for c in range(9):
                if board[row][c] == num:
                    return False
            for r in range(9):
                if board[r][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False
            return True
        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True
        solve(board)
