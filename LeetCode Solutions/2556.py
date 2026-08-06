class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m + n <= 2:
            return False

        reachable = [[False] * n for _ in range(m)]
        reachable[m - 1][n - 1] = True
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    continue
                if r + 1 < m and reachable[r + 1][c]:
                    reachable[r][c] = True
                if c + 1 < n and reachable[r][c + 1]:
                    reachable[r][c] = True

        if not reachable[0][0]:
            return True

        diag = [0] * (m + n - 1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and reachable[r][c]:
                    fwd = [[False] * n for _ in range(m)]
                    break
            else:
                continue
            break

        forward = [[False] * n for _ in range(m)]
        forward[0][0] = True
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 or not forward[r][c]:
                    continue
                if r + 1 < m and grid[r + 1][c] == 1:
                    forward[r + 1][c] = True
                if c + 1 < n and grid[r][c + 1] == 1:
                    forward[r][c + 1] = True

        for r in range(m):
            for c in range(n):
                if forward[r][c] and reachable[r][c]:
                    diag[r + c] += 1

        for d in range(1, m + n - 2):
            if diag[d] <= 1:
                return True
        return False