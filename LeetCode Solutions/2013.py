from collections import defaultdict
from typing import List
class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
    def count(self, point: List[int]) -> int:
        x, y = point
        total_squares = 0
        point_items = list(self.points.items())
        for (px, py), count in point_items:
            if px != x and abs(px - x) == abs(py - y):
                total_squares += count * self.points[(x, py)] * self.points[(px, y)]
        return total_squares
