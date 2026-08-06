class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(edges, k):
            from collections import defaultdict, deque
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1

            queue = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)

            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            return result if len(result) == k else []

        row_order = topological_sort(rowConditions, k)
        if not row_order:
            return []

        col_order = topological_sort(colConditions, k)
        if not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = row_pos[num], col_pos[num]
            matrix[r][c] = num

        return matrix