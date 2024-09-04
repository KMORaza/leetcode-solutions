class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i: int, j: int, word_index: int) -> bool:
            if word_index == len(word):
                return True
            if (i < 0 or i >= len(board) or
                j < 0 or j >= len(board[0]) or
                board[i][j] != word[word_index]):
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = (dfs(i + 1, j, word_index + 1) or
                     dfs(i - 1, j, word_index + 1) or
                     dfs(i, j + 1, word_index + 1) or
                     dfs(i, j - 1, word_index + 1))
            board[i][j] = temp
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
