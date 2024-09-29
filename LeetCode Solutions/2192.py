from typing import List
class Solution:
    def getAncestors(self, total_nodes: int, edges_list: List[List[int]]) -> List[List[int]]:
        ancestors_collection = [[] for _ in range(total_nodes)]
        graph_representation = [[] for _ in range(total_nodes)]
        for source, destination in edges_list:
            graph_representation[source].append(destination)
        for current_node in range(total_nodes):
            self._explore_ancestors(graph_representation, current_node, current_node, [False] * total_nodes, ancestors_collection)
        return ancestors_collection
    def _explore_ancestors(self, graph_representation: List[List[int]], node: int, ancestor_node: int, visited_nodes: List[bool], ancestors_collection: List[List[int]]):
        visited_nodes[node] = True
        for neighbor_node in graph_representation[node]:
            if visited_nodes[neighbor_node]:
                continue
            ancestors_collection[neighbor_node].append(ancestor_node)
            self._explore_ancestors(graph_representation, neighbor_node, ancestor_node, visited_nodes, ancestors_collection)
