from collections import deque
from typing import List
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        max_y_minus_x = deque()
        max_y_plus_x = deque()
        for x, y in points:
            while max_y_minus_x and x - max_y_minus_x[0][0] > k:
                max_y_minus_x.popleft()
            if max_y_minus_x:
                max_value = max(max_value, y + x + max_y_minus_x[0][1])
            while max_y_minus_x and max_y_minus_x[-1][1] <= y - x:
                max_y_minus_x.pop()
            max_y_minus_x.append((x, y - x))
            while max_y_plus_x and x - max_y_plus_x[0][0] > k:
                max_y_plus_x.popleft()
            if max_y_plus_x:
                max_value = max(max_value, y - x + max_y_plus_x[0][1])
            while max_y_plus_x and max_y_plus_x[-1][1] <= y + x:
                max_y_plus_x.pop()
            max_y_plus_x.append((x, y + x))
        return max_value
