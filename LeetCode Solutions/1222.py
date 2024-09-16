from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        queens_set = set(tuple(q) for q in queens)
        result = []
        king_x, king_y = king
        for dx, dy in directions:
            x, y = king_x, king_y
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queens_set:
                    result.append([x, y])
                    break
        return result
