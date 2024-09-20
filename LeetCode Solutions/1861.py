from collections import deque
class Solution:
    def rotateTheBox(self, grid):
        height = len(grid)
        width = len(grid[0])
        rotated_grid = [['' for _ in range(height)] for _ in range(width)]
        for h in range(height):
            for w in range(width):
                rotated_grid[w][height - h - 1] = grid[h][w]
        for w in range(height):
            available_spaces = deque()
            for h in range(width - 1, -1, -1):
                if rotated_grid[h][w] == '*':
                    available_spaces.clear()
                elif rotated_grid[h][w] == '.':
                    available_spaces.append(h)
                elif available_spaces:
                    rotated_grid[available_spaces.popleft()][w] = '#'
                    rotated_grid[h][w] = '.'
                    available_spaces.append(h)
        return rotated_grid
