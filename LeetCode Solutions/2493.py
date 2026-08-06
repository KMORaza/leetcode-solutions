class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def is_bipartite(start_node):
            color = {}
            queue = deque([start_node])
            color[start_node] = 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False, {}
            return True, color

        def bfs_max_depth(start_node):
            visited = set()
            queue = deque([(start_node, 0)])
            visited.add(start_node)
            max_depth = 0

            while queue:
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))

            return max_depth + 1

        visited_global = set()
        total_groups = 0

        for i in range(1, n + 1):
            if i not in visited_global:
                is_bipart, coloring = is_bipartite(i)

                if not is_bipart:
                    return -1

                component_nodes = set()
                queue = deque([i])
                component_nodes.add(i)
                visited_global.add(i)

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in component_nodes:
                            component_nodes.add(neighbor)
                            visited_global.add(neighbor)
                            queue.append(neighbor)

                max_groups_in_component = 0
                for node in component_nodes:
                    groups = bfs_max_depth(node)
                    max_groups_in_component = max(max_groups_in_component, groups)

                total_groups += max_groups_in_component

        return total_groups