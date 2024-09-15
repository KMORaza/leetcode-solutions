from typing import List
import math
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def encode_point(x: int, y: int) -> int:
            return x * 40001 + y
        num_points = len(points)
        encoded_points = set()
        for point in points:
            encoded_points.add(encode_point(point[0], point[1]))
        smallest_area = float('inf')
        for i in range(num_points):
            x1, y1 = points[i]
            for j in range(num_points):
                if j != i:
                    x2, y2 = points[j]
                    for k in range(j + 1, num_points):
                        if k != i:
                            x3, y3 = points[k]
                            x4 = x2 - x1 + x3
                            y4 = y2 - y1 + y3
                            if encode_point(x4, y4) in encoded_points:
                                if (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) == 0:
                                    width_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
                                    height_squared = (x3 - x1) ** 2 + (y3 - y1) ** 2
                                    area = math.sqrt(width_squared * height_squared)
                                    smallest_area = min(smallest_area, area)
        return 0 if smallest_area == float('inf') else smallest_area
