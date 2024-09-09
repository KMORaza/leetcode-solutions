class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        mask = (1 << n) - 1
        row_mask = 0
        col_mask = 0
        for i in range(n):
            row_mask |= board[0][i] << i
            col_mask |= board[i][0] << i
        rev_row_mask = mask ^ row_mask
        rev_col_mask = mask ^ col_mask
        same_row = 0
        same_col = 0
        for i in range(n):
            cur_row_mask = 0
            cur_col_mask = 0
            for j in range(n):
                cur_row_mask |= board[i][j] << j
                cur_col_mask |= board[j][i] << j
            if cur_row_mask != row_mask and cur_row_mask != rev_row_mask:
                return -1
            if cur_col_mask != col_mask and cur_col_mask != rev_col_mask:
                return -1
            same_row += (cur_row_mask == row_mask)
            same_col += (cur_col_mask == col_mask)
        t1 = self.f(row_mask, same_row, n)
        t2 = self.f(col_mask, same_col, n)
        return -1 if t1 == -1 or t2 == -1 else t1 + t2
    def f(self, mask, cnt, n):
        ones = bin(mask).count('1')
        if n % 2 == 1:
            if abs(n - ones * 2) != 1 or abs(n - cnt * 2) != 1:
                return -1
            if ones == n // 2:
                return n // 2 - bin(mask & 0xAAAAAAAA).count('1')
            return (n // 2 + 1) - bin(mask & 0x55555555).count('1')
        else:
            if ones != n // 2 or cnt != n // 2:
                return -1
            cnt0 = n // 2 - bin(mask & 0xAAAAAAAA).count('1')
            cnt1 = n // 2 - bin(mask & 0x55555555).count('1')
            return min(cnt0, cnt1)