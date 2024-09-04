class Solution:
    def solveNQueens(self, n: int):
        def backtrack(row, columns, diag1, diag2):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1, columns, diag1, diag2)
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = '.'
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        diag1 = set()
        diag2 = set()
        backtrack(0, columns, diag1, diag2)
        return result
