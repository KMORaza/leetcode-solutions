class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        in_stack = [False] * n
        stack_order = [-1] * n
        max_cycle = -1

        def dfs(node, order):
            nonlocal max_cycle
            if node == -1:
                return
            if in_stack[node]:
                cycle_length = order - stack_order[node]
                max_cycle = max(max_cycle, cycle_length)
                return
            if visited[node]:
                return

            visited[node] = True
            in_stack[node] = True
            stack_order[node] = order

            dfs(edges[node], order + 1)

            in_stack[node] = False

        for i in range(n):
            if not visited[i]:
                dfs(i, 0)

        return max_cycle