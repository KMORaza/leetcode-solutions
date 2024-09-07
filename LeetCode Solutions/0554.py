from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        for row in wall:
            edge_position = 0
            for width in row[:-1]:
                edge_position += width
                edge_count[edge_position] += 1
        total_rows = len(wall)
        max_edges = max(edge_count.values(), default=0)
        return total_rows - max_edges
