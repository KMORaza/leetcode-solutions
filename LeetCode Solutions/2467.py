class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        from collections import defaultdict

        n = len(amount)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [-1] * n

        def dfs_build_tree(node, par, dep):
            parent[node] = par
            depth[node] = dep
            for neighbor in graph[node]:
                if neighbor != par:
                    dfs_build_tree(neighbor, node, dep + 1)

        dfs_build_tree(0, -1, 0)

        bob_path = []
        curr = bob
        while curr != -1:
            bob_path.append(curr)
            curr = parent[curr]

        bob_time = {node: i for i, node in enumerate(bob_path)}

        max_income = float('-inf')

        def dfs_path(node, par, time, current_sum):
            nonlocal max_income

            if node in bob_time:
                bt = bob_time[node]
                if time < bt:
                    current_sum += amount[node]
                elif time == bt:
                    current_sum += amount[node] // 2
            else:
                current_sum += amount[node]

            is_leaf = True
            for neighbor in graph[node]:
                if neighbor != par:
                    is_leaf = False
                    dfs_path(neighbor, node, time + 1, current_sum)

            if is_leaf:
                max_income = max(max_income, current_sum)

        dfs_path(0, -1, 0, 0)

        return max_income