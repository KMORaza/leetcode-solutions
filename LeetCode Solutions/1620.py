from typing import List
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = 0
        best_coordinate = [0, 0]
        for x in range(51):
            for y in range(51):
                quality = 0
                for tx, ty, q in towers:
                    distance = ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5
                    if distance <= radius:
                        quality += q // (1 + distance)
                if quality > max_quality:
                    max_quality = quality
                    best_coordinate = [x, y]
                elif quality == max_quality:
                    if (x < best_coordinate[0] or
                        (x == best_coordinate[0] and y < best_coordinate[1])):
                        best_coordinate = [x, y]
        return best_coordinate
