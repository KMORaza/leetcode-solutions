class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        totalCells = 0
        catPos = 0
        mousePos = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '#':
                    totalCells += 1
                if grid[r][c] == 'C':
                    catPos = self.encode(r, c, cols)
                elif grid[r][c] == 'M':
                    mousePos = self.encode(r, c, cols)
        memo = [[[None] * (totalCells * 2) for _ in range(rows * cols)] for _ in range(rows * cols)]
        return self.dfs(grid, catPos, mousePos, 0, catJump, mouseJump, rows, cols, totalCells, memo)
    def dfs(self, grid: list[str], catPos: int, mousePos: int, turn: int, catJump: int,
            mouseJump: int, rows: int, cols: int, totalCells: int, memo: list[list[list[bool]]]) -> bool:
        if turn == totalCells * 2:
            return False
        if memo[catPos][mousePos][turn] is not None:
            return memo[catPos][mousePos][turn]
        if turn % 2 == 0:
            r, c = divmod(mousePos, cols)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                for j in range(mouseJump + 1):
                    nr, nc = r + dx * j, c + dy * j
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        break
                    if grid[nr][nc] == '#':
                        break
                    if grid[nr][nc] == 'F':
                        return self.setMemoAndReturn(memo, catPos, mousePos, turn, True)
                    if self.dfs(grid, catPos, self.encode(nr, nc, cols), turn + 1, catJump, mouseJump, rows, cols, totalCells, memo):
                        return self.setMemoAndReturn(memo, catPos, mousePos, turn, True)
            return self.setMemoAndReturn(memo, catPos, mousePos, turn, False)
        else:
            r, c = divmod(catPos, cols)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                for j in range(catJump + 1):
                    nr, nc = r + dx * j, c + dy * j
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        break
                    if grid[nr][nc] == '#':
                        break
                    if grid[nr][nc] == 'F':
                        return self.setMemoAndReturn(memo, catPos, mousePos, turn, False)
                    nextCatPos = self.encode(nr, nc, cols)
                    if nextCatPos == mousePos:
                        return self.setMemoAndReturn(memo, catPos, mousePos, turn, False)
                    if not self.dfs(grid, nextCatPos, mousePos, turn + 1, catJump, mouseJump, rows, cols, totalCells, memo):
                        return self.setMemoAndReturn(memo, catPos, mousePos, turn, False)
            return self.setMemoAndReturn(memo, catPos, mousePos, turn, True)
    def encode(self, r: int, c: int, cols: int) -> int:
        return r * cols + c
    def setMemoAndReturn(self, memo: list[list[list[bool]]], catPos: int, mousePos: int, turn: int, value: bool) -> bool:
        memo[catPos][mousePos][turn] = value
        return value