import math
from typing import List
class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def dist(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        def points_within_circle(center, radius, points):
            count = 0
            for px, py in points:
                if (px - center[0]) ** 2 + (py - center[1]) ** 2 <= radius ** 2 + 1e-9:
                    count += 1
            return count
        max_points = 1
        n = len(darts)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = darts[i], darts[j]
                d = dist(p1, p2)
                if d > 2 * r:
                    continue
                mid_x = (p1[0] + p2[0]) / 2
                mid_y = (p1[1] + p2[1]) / 2
                angle = math.acos(d / (2 * r))
                length = math.sqrt(r ** 2 - (d / 2) ** 2)
                dx = (p1[1] - p2[1]) / d
                dy = (p2[0] - p1[0]) / d
                center1 = (mid_x + length * dx, mid_y + length * dy)
                center2 = (mid_x - length * dx, mid_y - length * dy)
                max_points = max(max_points, points_within_circle(center1, r, darts))
                max_points = max(max_points, points_within_circle(center2, r, darts))
        return max_points
