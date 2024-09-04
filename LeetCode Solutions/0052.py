class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, columns, diag1, diag2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                count += backtrack(row + 1, columns, diag1, diag2)
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            return count
        columns = set()
        diag1 = set()
        diag2 = set()
        return backtrack(0, columns, diag1, diag2)
