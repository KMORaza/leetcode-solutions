class Solution:
    def gridGame(self, game_board):
        num_columns = len(game_board[0])
        best_outcome = float('inf')
        total_top_row = sum(game_board[0])
        total_bottom_row = 0
        for col_index in range(num_columns):
            total_top_row -= game_board[0][col_index]
            best_outcome = min(best_outcome, max(total_top_row, total_bottom_row))
            total_bottom_row += game_board[1][col_index]
        return best_outcome