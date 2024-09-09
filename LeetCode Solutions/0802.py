from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        indegree = [0] * n
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u] += 1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe_nodes = []
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for prev_node in reverse_graph[node]:
                indegree[prev_node] -= 1
                if indegree[prev_node] == 0:
                    queue.append(prev_node)
        return sorted(safe_nodes)
