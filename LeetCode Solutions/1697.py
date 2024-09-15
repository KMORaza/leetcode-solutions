from typing import List
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        class DisjointSet:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            def find(self, u):
                if self.parent[u] != u:
                    self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
            def union(self, u, v):
                rootU = self.find(u)
                rootV = self.find(v)
                if rootU != rootV:
                    if self.rank[rootU] > self.rank[rootV]:
                        self.parent[rootV] = rootU
                    elif self.rank[rootU] < self.rank[rootV]:
                        self.parent[rootU] = rootV
                    else:
                        self.parent[rootV] = rootU
                        self.rank[rootU] += 1
        edgeList.sort(key=lambda x: x[2])
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        ds = DisjointSet(n)
        result = [False] * len(queries)
        edge_index = 0
        for query_index, (u, v, limit) in indexed_queries:
            while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
                edge_u, edge_v, edge_weight = edgeList[edge_index]
                ds.union(edge_u, edge_v)
                edge_index += 1
            if ds.find(u) == ds.find(v):
                result[query_index] = True
        return result
