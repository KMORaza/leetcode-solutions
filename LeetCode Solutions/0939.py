from typing import List
from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(tuple(point) for point in points)
        min_area = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)
        return min_area if min_area != float('inf') else 0
