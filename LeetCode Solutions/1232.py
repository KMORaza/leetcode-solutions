from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        dx = x2 - x1
        dy = y2 - y1
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x1) * dy != (y - y1) * dx:
                return False
        return True
