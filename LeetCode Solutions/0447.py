from collections import defaultdict
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def squared_distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        total_boomerangs = 0
        for i in range(len(points)):
            distance_count = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dist = squared_distance(points[i], points[j])
                    distance_count[dist] += 1
            for count in distance_count.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
        return total_boomerangs
