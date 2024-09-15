class DisjointSet:
    def __init__(self, n):
        self.id = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            self.id[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.id[root_v] = root_u
        else:
            self.id[root_v] = root_u
            self.rank[root_u] += 1
class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        ds = DisjointSet(n)
        component_size = [0] * n
        component_malware_count = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    ds.union(i, j)
        for i in range(n):
            root = ds.find(i)
            component_size[root] += 1
        for i in initial:
            root = ds.find(i)
            component_malware_count[root] += 1
        initial.sort()
        output = initial[0]
        largest_component_size = 0
        for i in initial:
            root = ds.find(i)
            if component_size[root] > largest_component_size and component_malware_count[root] == 1:
                largest_component_size = component_size[root]
                output = i
        return output
