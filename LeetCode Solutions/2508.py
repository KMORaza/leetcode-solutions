class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        odd_degree_nodes = []
        for i in range(1, n + 1):
            if len(graph[i]) % 2 == 1:
                odd_degree_nodes.append(i)

        odd_count = len(odd_degree_nodes)

        if odd_count == 0:
            return True
        elif odd_count == 2:
            a, b = odd_degree_nodes[0], odd_degree_nodes[1]
            if b not in graph[a]:
                return True
            for i in range(1, n + 1):
                if i != a and i != b and a not in graph[i] and b not in graph[i]:
                    return True
            return False
        elif odd_count == 4:
            a, b, c, d = odd_degree_nodes
            if b not in graph[a] and d not in graph[c]:
                return True
            if c not in graph[a] and d not in graph[b]:
                return True
            if d not in graph[a] and c not in graph[b]:
                return True
            return False
        else:
            return False