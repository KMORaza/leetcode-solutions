class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict
        class DisjointSet:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            row_map[r].append(i)
            col_map[c].append(i)
        ds = DisjointSet(len(stones))
        for indices in row_map.values():
            for i in range(1, len(indices)):
                ds.union(indices[0], indices[i])
        for indices in col_map.values():
            for i in range(1, len(indices)):
                ds.union(indices[0], indices[i])
        unique_roots = set(ds.find(i) for i in range(len(stones)))
        num_components = len(unique_roots)
        return len(stones) - num_components
