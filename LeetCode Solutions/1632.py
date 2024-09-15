from collections import defaultdict
from typing import List, Dict, Tuple
class DisjointSet:
    def __init__(self):
        self.parent = {}
    def find_root(self, x: int) -> int:
        if self.parent.get(x, x) == x:
            return x
        self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]
    def unite(self, x: int, y: int) -> None:
        self.parent.setdefault(x, x)
        self.parent.setdefault(y, y)
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
    def get_components(self) -> Dict[int, List[int]]:
        component_map = defaultdict(list)
        for x in self.parent.keys():
            root_x = self.find_root(x)
            component_map[root_x].append(x)
        return component_map
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * cols for _ in range(rows)]
        value_to_positions = defaultdict(list)
        current_rank = [0] * (rows + cols)
        for i in range(rows):
            for j in range(cols):
                value = matrix[i][j]
                value_to_positions[value].append((i, j))
        for value, positions in sorted(value_to_positions.items()):
            ds = DisjointSet()
            for i, j in positions:
                ds.unite(i, j + rows)
            for component in ds.get_components().values():
                max_rank = max(current_rank[i] for i in component)
                for i in component:
                    current_rank[i] = max_rank + 1
            for i, j in positions:
                result[i][j] = current_rank[i]
        return result
