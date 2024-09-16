class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY
        for a, b in zip(s1, s2):
            union(a, b)
        smallest_rep = {}
        for char in parent:
            root = find(char)
            if root not in smallest_rep or char < smallest_rep[root]:
                smallest_rep[root] = char
        result = ''.join(smallest_rep[find(char)] for char in baseStr)
        return result
