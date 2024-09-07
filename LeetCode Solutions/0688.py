class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1.0
        for move in range(k):
            for r in range(n):
                for c in range(n):
                    if dp[move][r][c] > 0:
                        for dr, dc in directions:
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < n and 0 <= new_c < n:
                                dp[move + 1][new_r][new_c] += dp[move][r][c] / 8.0
        probability = 0.0
        for r in range(n):
            for c in range(n):
                probability += dp[k][r][c]
        return probability
