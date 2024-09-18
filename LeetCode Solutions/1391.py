class Solution:
    def hasValidPath(self, maze):
        rows, cols = len(maze), len(maze[0])
        expanded_grid = [[False] * (cols * 3) for _ in range(rows * 3)]
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 1:
                    expanded_grid[r * 3 + 1][c * 3 + 0] = True
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 2] = True
                elif maze[r][c] == 2:
                    expanded_grid[r * 3 + 0][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                    expanded_grid[r * 3 + 2][c * 3 + 1] = True
                elif maze[r][c] == 3:
                    expanded_grid[r * 3 + 1][c * 3 + 0] = True
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                    expanded_grid[r * 3 + 2][c * 3 + 1] = True
                elif maze[r][c] == 4:
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 2] = True
                    expanded_grid[r * 3 + 2][c * 3 + 1] = True
                elif maze[r][c] == 5:
                    expanded_grid[r * 3 + 0][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 0] = True
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                elif maze[r][c] == 6:
                    expanded_grid[r * 3 + 0][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 1] = True
                    expanded_grid[r * 3 + 1][c * 3 + 2] = True
        return self.explore(expanded_grid, 1, 1)
    def explore(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if not grid[x][y]:
            return False
        if x == len(grid) - 2 and y == len(grid[0]) - 2:
            return True
        grid[x][y] = False
        return (self.explore(grid, x + 1, y) or self.explore(grid, x - 1, y) or
                self.explore(grid, x, y + 1) or self.explore(grid, x, y - 1))
