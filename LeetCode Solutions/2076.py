class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ds = DisjointSet(n)
        res = []
        active_requests = []
        for a, b in requests:
            can_grant = True
            ds.union(a, b)
            for x, y in restrictions:
                if ds.find(x) == ds.find(y):
                    can_grant = False
                    break
            if can_grant:
                res.append(True)
                active_requests.append((a, b))
            else:
                res.append(False)
                ds = DisjointSet(n)
                for x, y in active_requests:
                    ds.union(x, y)
        return res
