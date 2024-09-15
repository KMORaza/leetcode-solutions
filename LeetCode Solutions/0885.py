from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        dir_idx = 0
        steps = 0
        leg_length = 1
        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(leg_length):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r += directions[dir_idx][0]
                    c += directions[dir_idx][1]
                dir_idx = (dir_idx + 1) % 4
            leg_length += 1
        return result
