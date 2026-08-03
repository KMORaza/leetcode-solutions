class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        components = []

        for i in range(n):
            if not visited[i]:
                size = 0
                queue = deque([i])
                visited[i] = True

                while queue:
                    node = queue.popleft()
                    size += 1

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                components.append(size)

        total_pairs = n * (n - 1) // 2
        reachable_pairs = 0

        for size in components:
            reachable_pairs += size * (size - 1) // 2

        return total_pairs - reachable_pairs