from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        result = []
        for col in range(cols):
            current_col = col
            for row in range(rows):
                direction = grid[row][current_col]
                if direction == 1:
                    if current_col == cols - 1 or grid[row][current_col + 1] == -1:
                        current_col = -1
                        break
                    current_col += 1
                else:
                    if current_col == 0 or grid[row][current_col - 1] == 1:
                        current_col = -1
                        break
                    current_col -= 1
            result.append(current_col)
        return result
