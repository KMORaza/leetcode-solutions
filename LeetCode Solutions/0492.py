import math
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        min_diff = float('inf')
        best_length, best_width = 0, 0
        for width in range(1, int(math.sqrt(area)) + 1):
            if area % width == 0:
                length = area // width
                if length >= width:
                    if length - width < min_diff:
                        min_diff = length - width
                        best_length, best_width = length, width
        return [best_length, best_width]
