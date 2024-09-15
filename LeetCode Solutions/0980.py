class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start = end = None
        empty_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                if grid[r][c] != -1:
                    empty_count += 1
        def dfs(r, c, path_length):
            if (r, c) == end:
                return 1 if path_length == empty_count else 0
            temp = grid[r][c]
            grid[r][c] = -1
            total_paths = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    total_paths += dfs(nr, nc, path_length + 1)
            grid[r][c] = temp
            return total_paths
        if not start or not end:
            return 0
        return dfs(start[0], start[1], 1)