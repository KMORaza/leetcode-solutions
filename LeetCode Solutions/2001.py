from collections import defaultdict
from math import gcd
from typing import List
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        aspect_ratio_count = defaultdict(int)
        for width, height in rectangles:
            divisor = gcd(width, height)
            reduced_ratio = (width // divisor, height // divisor)
            aspect_ratio_count[reduced_ratio] += 1
        count = 0
        for n in aspect_ratio_count.values():
            if n > 1:
                count += n * (n - 1) // 2
        return count
