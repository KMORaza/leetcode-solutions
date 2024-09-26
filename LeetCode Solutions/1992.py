from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        visited = [[False] * cols for _ in range(rows)]
        farmland = []
        def dfs(r: int, c: int) -> (int, int):
            nonlocal min_row, min_col, max_row, max_col
            if r < 0 or r >= rows or c < 0 or c >= cols or land[r][c] == 0 or visited[r][c]:
                return
            visited[r][c] = True
            min_row, min_col = min(min_row, r), min(min_col, c)
            max_row, max_col = max(max_row, r), max(max_col, c)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and not visited[i][j]:
                    min_row, min_col, max_row, max_col = i, j, i, j
                    dfs(i, j)
                    farmland.append([min_row, min_col, max_row, max_col])
        return farmland
