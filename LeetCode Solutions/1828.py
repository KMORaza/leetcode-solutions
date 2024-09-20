from typing import List
import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for qx, qy, qr in queries:
            count = 0
            for px, py in points:
                distance_squared = (px - qx) ** 2 + (py - qy) ** 2
                if distance_squared <= qr ** 2:
                    count += 1
            result.append(count)
        return result
