class NodeClass:
    def __init__(self):
        self.branches = [None] * 2
        self.total_entries = 0
class Solution:
    def countPairs(self, data_list, lower_bound, upper_bound):
        total_pairs = 0
        for value in data_list:
            total_pairs += self.queryCount(value, upper_bound + 1) - self.queryCount(value, lower_bound)
            self.addValue(value)
        return total_pairs
    max_height = 14
    def __init__(self):
        self.root_node = NodeClass()
    def addValue(self, value):
        current = self.root_node
        for bit_position in range(self.max_height, -1, -1):
            bit_digit = (value >> bit_position) & 1
            if current.branches[bit_digit] is None:
                current.branches[bit_digit] = NodeClass()
            current = current.branches[bit_digit]
            current.total_entries += 1
    def queryCount(self, value, limit):
        count = 0
        current = self.root_node
        for bit_position in range(self.max_height, -1, -1):
            bit_digit = (value >> bit_position) & 1
            limit_bit = (limit >> bit_position) & 1
            if limit_bit == 1:
                if current.branches[bit_digit] is not None:
                    count += current.branches[bit_digit].total_entries
                current = current.branches[bit_digit ^ 1]
            else:
                current = current.branches[bit_digit]
            if current is None:
                break
        return count
