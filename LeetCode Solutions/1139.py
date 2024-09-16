from typing import List
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        h = [[0] * n for _ in range(m)]
        v = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    h[i][j] = h[i][j-1] + 1 if j > 0 else 1
                    v[i][j] = v[i-1][j] + 1 if i > 0 else 1
        max_side = 0
        for i in range(m):
            for j in range(n):
                side_length = min(h[i][j], v[i][j])
                while side_length > max_side:
                    if i - side_length + 1 >= 0 and j - side_length + 1 >= 0:
                        if h[i - side_length + 1][j] >= side_length and v[i][j - side_length + 1] >= side_length:
                            max_side = side_length
                    side_length -= 1
        return max_side * max_side
