class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        nodes = sorted([(vals[i], i) for i in range(n)])

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        result = n
        i = 0
        while i < n:
            current_val = nodes[i][0]

            j = i
            while j < n and nodes[j][0] == current_val:
                j += 1

            same_val_nodes = [nodes[k][1] for k in range(i, j)]

            for node in same_val_nodes:
                for neighbor in graph[node]:
                    if vals[neighbor] <= current_val:
                        union(node, neighbor)

            group_size = {}
            for node in same_val_nodes:
                root = find(node)
                group_size[root] = group_size.get(root, 0) + 1

            for size in group_size.values():
                if size > 1:
                    result += size * (size - 1) // 2

            i = j

        return result