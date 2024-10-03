from typing import List
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            for dx in range(-r, r + 1):
                dy_limit = int((r**2 - dx**2)**0.5)
                for dy in range(-dy_limit, dy_limit + 1):
                    points.add((x + dx, y + dy))
        return len(points)
