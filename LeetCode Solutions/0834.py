from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        subtree_size = [0] * n
        distance = [0] * n
        result = [0] * n

        def dfs1(node: int, parent: int):
            subtree_size[node] = 1
            total_distance = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_distance = dfs1(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]
                total_distance += child_distance + subtree_size[neighbor]
            distance[node] = total_distance
            return total_distance

        def dfs2(node: int, parent: int):
            result[node] = distance[node]
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                distance[neighbor] = distance[node] + (n - 2 * subtree_size[neighbor])
                dfs2(neighbor, node)

        dfs1(0, -1)
        dfs2(0, -1)
        return result
