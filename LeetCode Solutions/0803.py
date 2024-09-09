class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols + 1))
        size = [1] * (rows * cols + 1)
        def find_root(x: int) -> int:
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]
        def merge(a: int, b: int):
            rootA = find_root(a)
            rootB = find_root(b)
            if rootA != rootB:
                size[rootB] += size[rootA]
                parent[rootA] = rootB
        grid_snapshot = [row[:] for row in grid]
        for r, c in hits:
            grid_snapshot[r][c] = 0
        dummy_root = rows * cols
        for j in range(cols):
            if grid_snapshot[0][j] == 1:
                merge(j, dummy_root)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(1, rows):
            for j in range(cols):
                if grid_snapshot[i][j] == 1:
                    if grid_snapshot[i - 1][j] == 1:
                        merge(i * cols + j, (i - 1) * cols + j)
                    if j > 0 and grid_snapshot[i][j - 1] == 1:
                        merge(i * cols + j, i * cols + j - 1)
        fall_counts = [0] * len(hits)
        for k in range(len(hits) - 1, -1, -1):
            r, c = hits[k]
            if grid[r][c] == 0:
                continue
            grid_snapshot[r][c] = 1
            initial_roof_size = size[find_root(dummy_root)]
            if r == 0:
                merge(c, dummy_root)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid_snapshot[nr][nc] == 1:
                    merge(r * cols + c, nr * cols + nc)
            new_roof_size = size[find_root(dummy_root)]
            fall_counts[k] = max(0, new_roof_size - initial_roof_size - 1)
        return fall_counts
