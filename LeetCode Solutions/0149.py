from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        def compute_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return (float('inf'), p1[0])
            if dy == 0:
                return (0, p1[1])
            g = gcd(dx, dy)
            return (dy // g, dx // g)
        n = len(points)
        if n <= 1:
            return n
        max_points = 0
        for i in range(n):
            slopes = defaultdict(int)
            overlap = 0
            current_max = 0
            for j in range(n):
                if i != j:
                    if points[i] == points[j]:
                        overlap += 1
                    else:
                        slope = compute_slope(points[i], points[j])
                        slopes[slope] += 1
                        current_max = max(current_max, slopes[slope])
            max_points = max(max_points, current_max + overlap + 1)
        return max_points
