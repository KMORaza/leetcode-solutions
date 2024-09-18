import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        distance_x = xCenter - nearest_x
        distance_y = yCenter - nearest_y
        distance_squared = distance_x * distance_x + distance_y * distance_y
        return distance_squared <= radius * radius
