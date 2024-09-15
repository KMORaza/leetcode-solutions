import math
from typing import List
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def calculate_angle(x1, y1, x2, y2):
            return math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles = []
        same_location_points = 0
        for (x, y) in points:
            if (x, y) == tuple(location):
                same_location_points += 1
            else:
                angle_from_location = calculate_angle(location[0], location[1], x, y)
                angles.append(angle_from_location)
        angles.sort()
        angles += [a + 360 for a in angles]
        max_visible = 0
        j = 0
        for i in range(len(angles) // 2):
            while j < len(angles) and angles[j] <= angles[i] + angle:
                j += 1
            max_visible = max(max_visible, j - i)
        return max_visible + same_location_points
