class Solution:
    def tictactoe(self, actions):
        row_count = [[0] * 3 for _ in range(2)]
        col_count = [[0] * 3 for _ in range(2)]
        main_diag = [0, 0]
        anti_diag = [0, 0]
        for index in range(len(actions)):
            row_index = actions[index][0]
            col_index = actions[index][1]
            player = index % 2
            row_count[player][row_index] += 1
            col_count[player][col_index] += 1
            if row_index == col_index:
                main_diag[player] += 1
            if row_index + col_index == 2:
                anti_diag[player] += 1
            if (row_count[player][row_index] == 3 or
                col_count[player][col_index] == 3 or
                main_diag[player] == 3 or
                anti_diag[player] == 3):
                return "A" if player == 0 else "B"
        if len(actions) == 9:
            return "Draw"
        else:
            return "Pending"
