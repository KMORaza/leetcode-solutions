from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        topological_order = []
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(topological_order) == numCourses:
            return topological_order
        else:
            return []