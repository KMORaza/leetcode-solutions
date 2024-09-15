from typing import List
import heapq
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        def kruskal(edges, n, skip_edge=None, force_edge=None):
            parent = list(range(n))
            rank = [0] * n
            total_weight = 0
            edge_count = 0
            if force_edge is not None:
                u, v, weight = force_edge
                union(parent, rank, u, v)
                total_weight += weight
                edge_count += 1
            for i, (u, v, weight) in enumerate(edges):
                if i == skip_edge:
                    continue
                if find(parent, u) != find(parent, v):
                    union(parent, rank, u, v)
                    total_weight += weight
                    edge_count += 1
            if edge_count == n - 1:
                return total_weight
            return float('inf')
        edges = sorted(enumerate(edges), key=lambda x: x[1][2])
        edge_list = [e[1] for e in edges]
        original_mst_weight = kruskal(edge_list, n)
        critical_edges = []
        pseudo_critical_edges = []
        for i, edge in enumerate(edge_list):
            if kruskal(edge_list, n, skip_edge=i) > original_mst_weight:
                critical_edges.append(edges[i][0])
            else:
                if kruskal(edge_list, n, force_edge=edge) == original_mst_weight:
                    pseudo_critical_edges.append(edges[i][0])
        return [critical_edges, pseudo_critical_edges]
