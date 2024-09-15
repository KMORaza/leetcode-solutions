class NodeClass:
    def __init__(self):
        self.edges = [None] * 2
class BinaryTrieClass:
    def __init__(self, max_bit):
        self.bit_limit = max_bit
        self.root = NodeClass()
    def add_number(self, value):
        current = self.root
        for bit_position in range(self.bit_limit, -1, -1):
            bit = (value >> bit_position) & 1
            if current.edges[bit] is None:
                current.edges[bit] = NodeClass()
            current = current.edges[bit]
    def compute_max_xor(self, value):
        max_xor_value = 0
        current = self.root
        for bit_position in range(self.bit_limit, -1, -1):
            bit = (value >> bit_position) & 1
            alternate_bit = bit ^ 1
            if current.edges[alternate_bit] is not None:
                max_xor_value |= (1 << bit_position)
                current = current.edges[alternate_bit]
            elif current.edges[bit] is not None:
                current = current.edges[bit]
            else:
                return 0
        return max_xor_value
class Solution:
    def maximizeXor(self, numbers, queries_list):
        results = [-1] * len(queries_list)
        max_number_in_numbers = max(numbers)
        max_number_in_query = max(query[0] for query in queries_list)
        bit_limit = int(max(max_number_in_numbers, max_number_in_query).bit_length()) - 1
        trie = BinaryTrieClass(bit_limit)
        numbers.sort()
        sorted_queries = self.prepare_sorted_queries(queries_list)
        i = 0
        for query_index, x, m in sorted_queries:
            while i < len(numbers) and numbers[i] <= m:
                trie.add_number(numbers[i])
                i += 1
            if i > 0 and numbers[i - 1] <= m:
                results[query_index] = trie.compute_max_xor(x)
        return results
    def prepare_sorted_queries(self, queries_list):
        sorted_queries = [(i, query[0], query[1]) for i, query in enumerate(queries_list)]
        sorted_queries.sort(key=lambda query: query[2])
        return sorted_queries
