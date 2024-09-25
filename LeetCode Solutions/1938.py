class NodeClass:
    def __init__(self):
        self.children = [None, None]
        self.frequency = 0
class BinaryTrie:
    height = 17
    def __init__(self):
        self.root = NodeClass()
    def add(self, number, value):
        current_node = self.root
        for i in range(self.height, -1, -1):
            bit = (number >> i) & 1
            if current_node.children[bit] is None:
                current_node.children[bit] = NodeClass()
            current_node = current_node.children[bit]
            current_node.frequency += value
    def retrieve(self, number):
        result = 0
        current_node = self.root
        for i in range(self.height, -1, -1):
            bit = (number >> i) & 1
            opposite_bit = bit ^ 1
            if (current_node.children[opposite_bit] is not None and
                    current_node.children[opposite_bit].frequency > 0):
                result += (1 << i)
                current_node = current_node.children[opposite_bit]
            else:
                current_node = current_node.children[opposite_bit ^ 1]
        return result
class Solution:
    def maxGeneticDifference(self, parents, queries):
        size = len(parents)
        output = [0] * len(queries)
        root_index = -1
        adjacency_list = [[] for _ in range(size)]
        for index in range(size):
            if parents[index] == -1:
                root_index = index
            else:
                adjacency_list[parents[index]].append(index)
        query_map = {}
        binary_trie = BinaryTrie()
        for idx, (node, value) in enumerate(queries):
            if node not in query_map:
                query_map[node] = []
            query_map[node].append((idx, value))
        self.traverse(root_index, binary_trie, adjacency_list, query_map, output)
        return output
    def traverse(self, node, binary_trie, adjacency_list, query_map, output):
        binary_trie.add(node, 1)
        if node in query_map:
            for idx, value in query_map[node]:
                output[idx] = binary_trie.retrieve(value)
        for child in adjacency_list[node]:
            self.traverse(child, binary_trie, adjacency_list, query_map, output)
        binary_trie.add(node, -1)
