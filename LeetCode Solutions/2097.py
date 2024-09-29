from collections import defaultdict, deque
class Solution:
    def validArrangement(self, pairs):
        path = []
        connections = defaultdict(deque)
        outgoing_edges = defaultdict(int)
        incoming_edges = defaultdict(int)
        for origin, target in pairs:
            connections[origin].append(target)
            outgoing_edges[origin] += 1
            incoming_edges[target] += 1
        initial_node = self.determine_start_node(connections, outgoing_edges, incoming_edges, pairs)
        self.perform_eulerian_traversal(connections, initial_node, path)
        path.reverse()
        return path
    def determine_start_node(self, connections, outgoing_edges, incoming_edges, pairs):
        for vertex in connections:
            if outgoing_edges[vertex] - incoming_edges[vertex] == 1:
                return vertex
        return pairs[0][0]
    def perform_eulerian_traversal(self, connections, current_vertex, path):
        stack = connections[current_vertex]
        while stack:
            next_vertex = stack.pop()
            self.perform_eulerian_traversal(connections, next_vertex, path)
            path.append([current_vertex, next_vertex])