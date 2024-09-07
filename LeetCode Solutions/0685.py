class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]
    def union_by_rank(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.id[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.id[root_v] = root_u
        else:
            self.id[root_u] = root_v
            self.rank[root_v] += 1
        return True
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        ids = [0] * (n + 1)
        node_with_two_parents = 0
        for u, v in edges:
            ids[v] += 1
            if ids[v] == 2:
                node_with_two_parents = v
                break
        if node_with_two_parents == 0:
            return self.findRedundantDirectedConnectionWithUnionFind(edges, -1)
        for i in range(n - 1, -1, -1):
            if edges[i][1] == node_with_two_parents:
                if len(self.findRedundantDirectedConnectionWithUnionFind(edges, i)) == 0:
                    return edges[i]
        raise ValueError("Connection not found!")
    def findRedundantDirectedConnectionWithUnionFind(self, edges, skipped_edge_index):
        uf = UnionFind(len(edges) + 1)
        for i in range(len(edges)):
            if i == skipped_edge_index:
                continue
            u, v = edges[i]
            if not uf.union_by_rank(u, v):
                return [u, v]
        return []
