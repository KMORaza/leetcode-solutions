class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0

        def dfs(v, parent):
            nonlocal ans

            max_path_with_v = price[v]
            max_path_without_v = 0

            for u in graph[v]:
                if u != parent:
                    sub_max_with, sub_max_without = dfs(u, v)

                    ans = max(ans, max_path_with_v + sub_max_without)
                    ans = max(ans, max_path_without_v + sub_max_with)

                    max_path_with_v = max(max_path_with_v, sub_max_with + price[v])
                    max_path_without_v = max(max_path_without_v, sub_max_without + price[v])

            return max_path_with_v, max_path_without_v

        dfs(0, -1)
        return ans