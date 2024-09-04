class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.is_valid_group(row):
                return False
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_group(column):
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                sub_box = [board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                if not self.is_valid_group(sub_box):
                    return False
        return True
    def is_valid_group(self, group: list[str]) -> bool:
        seen = set()
        for value in group:
            if value != '.':
                if value in seen:
                    return False
                seen.add(value)
        return True