from typing import List
import itertools
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1, y1, x2, y2, x3, y3):
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
        max_area = 0
        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            area = triangleArea(x1, y1, x2, y2, x3, y3)
            max_area = max(max_area, area)
        return max_area
