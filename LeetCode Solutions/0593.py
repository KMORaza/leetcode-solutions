from itertools import combinations
class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def squared_distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        points = [p1, p2, p3, p4]
        distances = []
        for (p1, p2) in combinations(points, 2):
            distances.append(squared_distance(p1, p2))
        distances.sort()
        return (len(distances) == 6 and
                distances[0] == distances[1] == distances[2] == distances[3] and
                distances[4] == distances[5] and
                distances[0] > 0 and
                distances[4] > distances[0])