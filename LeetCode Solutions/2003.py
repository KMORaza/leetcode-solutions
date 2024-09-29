class Solution:
    def smallestMissingValueSubtree(self, parent_list, value_list):
        total_nodes = len(parent_list)
        output = [1] * total_nodes
        graph = [[] for _ in range(total_nodes)]
        encountered = set()
        smallest_absent = 1
        for idx in range(1, total_nodes):
            graph[parent_list[idx]].append(idx)
        target_node = self.locate_one(value_list)
        if target_node == -1:
            return output
        current = target_node
        last_node = -1
        while current != -1:
            for child in graph[current]:
                if child != last_node:
                    self.traverse(child, graph, encountered, value_list)
            encountered.add(value_list[current])
            while smallest_absent in encountered:
                smallest_absent += 1
            output[current] = smallest_absent
            last_node = current
            current = parent_list[current]
        return output
    def traverse(self, node, graph, encountered, value_list):
        encountered.add(value_list[node])
        for child in graph[node]:
            self.traverse(child, graph, encountered, value_list)
    def locate_one(self, value_list):
        for idx in range(len(value_list)):
            if value_list[idx] == 1:
                return idx
        return -1