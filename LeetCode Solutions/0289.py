class Solution:
    def gameOfLife(self, board):
        def count_live_neighbors(x, y):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == 1 or board[nx][ny] == 2:
                        count += 1
            return count
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = -1
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
