from collections import defaultdict
from typing import List
class Solution:
    def checkWays(self, connections: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        node_degrees = defaultdict(int)
        edge_existence = defaultdict(lambda: defaultdict(bool))
        for start, end in connections:
            if end not in adjacency_list[start]:
                adjacency_list[start].append(end)
            if start not in adjacency_list[end]:
                adjacency_list[end].append(start)
            node_degrees[start] += 1
            node_degrees[end] += 1
            edge_existence[start][end] = True
            edge_existence[end][start] = True
        for node in adjacency_list:
            adjacency_list[node].sort(key=lambda x: -node_degrees[x])
        root_node = self.findRoot(node_degrees, len(adjacency_list))
        if root_node == -1:
            return 0
        self.hasAlternativeConnections = False
        if not self.depthFirstSearch(adjacency_list, root_node, node_degrees, edge_existence, set(), set()):
            return 0
        return 2 if self.hasAlternativeConnections else 1
    def findRoot(self, node_degrees: defaultdict(int), total_nodes: int) -> int:
        for node, degree in node_degrees.items():
            if degree == total_nodes - 1:
                return node
        return -1
    def depthFirstSearch(self, adjacency_list: defaultdict(list), current_node: int, node_degrees: defaultdict(int),
            edge_existence: defaultdict(lambda: defaultdict(bool)), visited_ancestors: set, visited_nodes: set) -> bool:
        visited_nodes.add(current_node)
        if not all(edge_existence[current_node][ancestor] for ancestor in visited_ancestors):
            return False
        visited_ancestors.add(current_node)
        for neighbor in adjacency_list[current_node]:
            if neighbor in visited_nodes:
                continue
            if node_degrees[neighbor] == node_degrees[current_node]:
                self.hasAlternativeConnections = True
            if not self.depthFirstSearch(adjacency_list, neighbor, node_degrees, edge_existence, visited_ancestors, visited_nodes):
                return False
        visited_ancestors.remove(current_node)
        return True
