from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        rank = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for eq in equations:
            if eq[1] == '=':
                union(eq[0], eq[3])
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]):
                    return False
        return True
