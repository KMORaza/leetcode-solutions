class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        mem = [[[-float('inf')] * n for _ in range(n)] for _ in range(n)]
        result = self.cherryPickupHelper(grid, 0, 0, 0, mem)
        return max(0, result)
    def cherryPickupHelper(self, grid, x1, y1, x2, mem):
        n = len(grid)
        y2 = x1 + y1 - x2
        if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
            return -1
        if grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -1
        if x1 == n - 1 and y1 == n - 1:
            return grid[x1][y1]
        if mem[x1][y1][x2] != -float('inf'):
            return mem[x1][y1][x2]
        res = -1
        for dx1, dy1, dx2, dy2 in [(1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1)]:
            next_res = self.cherryPickupHelper(grid, x1 + dx1, y1 + dy1, x2 + dx2, mem)
            if next_res != -1:
                res = max(res, next_res)
        if res != -1:
            res += grid[x1][y1]
            if x1 != x2 or y1 != y2:
                res += grid[x2][y2]
        mem[x1][y1][x2] = res
        return res
