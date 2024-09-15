class Solution:
    def regionsBySlashes(self, grid):
        size = len(grid)
        expanded_grid = [[0] * (size * 3) for _ in range(size * 3)]
        for row in range(size):
            for col in range(size):
                if grid[row][col] == '/':
                    expanded_grid[row * 3][col * 3 + 2] = 1
                    expanded_grid[row * 3 + 1][col * 3 + 1] = 1
                    expanded_grid[row * 3 + 2][col * 3] = 1
                elif grid[row][col] == '\\':
                    expanded_grid[row * 3][col * 3] = 1
                    expanded_grid[row * 3 + 1][col * 3 + 1] = 1
                    expanded_grid[row * 3 + 2][col * 3 + 2] = 1
        region_count = 0
        for x in range(size * 3):
            for y in range(size * 3):
                if expanded_grid[x][y] == 0:
                    self._explore_region(expanded_grid, x, y)
                    region_count += 1
        return region_count
    def _explore_region(self, expanded_grid, x, y):
        if x < 0 or x >= len(expanded_grid) or y < 0 or y >= len(expanded_grid[0]):
            return
        if expanded_grid[x][y] != 0:
            return
        expanded_grid[x][y] = 2
        self._explore_region(expanded_grid, x + 1, y)
        self._explore_region(expanded_grid, x - 1, y)
        self._explore_region(expanded_grid, x, y + 1)
        self._explore_region(expanded_grid, x, y - 1)
