from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_length = 0
        count = 0
        for length, width in rectangles:
            square_side = min(length, width)
            if square_side > max_length:
                max_length = square_side
                count = 1
            elif square_side == max_length:
                count += 1
        return count
