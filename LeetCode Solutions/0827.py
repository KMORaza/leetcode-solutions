from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(x, y, index):
            stack = [(x, y)]
            size = 0
            while stack:
                cx, cy = stack.pop()
                if (cx < 0 or cy < 0 or cx >= n or cy >= n or grid[cx][cy] != 1):
                    continue
                grid[cx][cy] = index
                size += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((cx + dx, cy + dy))
            return size
        island_index = 2
        island_size = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_index)
                    island_size[island_index] = size
                    island_index += 1
        max_island_size = max(island_size.values(), default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    potential_size = 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            island_label = grid[nx][ny]
                            if island_label not in seen:
                                potential_size += island_size[island_label]
                                seen.add(island_label)
                    max_island_size = max(max_island_size, potential_size)
        return max_island_size
