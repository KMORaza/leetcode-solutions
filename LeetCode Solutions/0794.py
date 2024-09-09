class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        def check_winner(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        def count_chars(board):
            x_count = sum(row.count('X') for row in board)
            o_count = sum(row.count('O') for row in board)
            return x_count, o_count
        x_count, o_count = count_chars(board)
        if o_count > x_count or x_count > o_count + 1:
            return False
        x_wins = check_winner(board, 'X')
        o_wins = check_winner(board, 'O')
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
        return True
