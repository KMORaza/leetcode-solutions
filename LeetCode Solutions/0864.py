from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        start_x, start_y = -1, -1
        total_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                elif 'a' <= grid[i][j] <= 'f':
                    total_keys += 1
        queue = deque([(start_x, start_y, 0, 0)])
        visited = set((start_x, start_y, 0))
        while queue:
            x, y, moves, keys = queue.popleft()
            if keys == (1 << total_keys) - 1:
                return moves
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    if cell == '#':
                        continue
                    new_keys = keys
                    if 'a' <= cell <= 'f':
                        new_keys |= 1 << (ord(cell) - ord('a'))
                    elif 'A' <= cell <= 'F':
                        if not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, moves + 1, new_keys))
        return -1
