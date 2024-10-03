class Node:
    def __init__(self, begin, finish, highest_char, start_char, end_char, longest_seq, start_length, end_length, left_child=None, right_child=None):
        self.begin = begin
        self.finish = finish
        self.highest_char = highest_char
        self.start_char = start_char
        self.end_char = end_char
        self.longest_seq = longest_seq
        self.start_length = start_length
        self.end_length = end_length
        self.left_child = left_child
        self.right_child = right_child
class Tree:
    def __init__(self, data):
        self.root_node = self.create_tree(data, 0, len(data) - 1)
    def create_tree(self, data, begin, finish):
        if begin == finish:
            return Node(begin, finish, data[begin], data[begin], data[begin], 1, 1, 1)
        midpoint = (begin + finish) // 2
        left_child = self.create_tree(data, begin, midpoint)
        right_child = self.create_tree(data, midpoint + 1, finish)
        return self.combine_nodes(left_child, right_child)
    def modify_tree(self, current_node, index, char):
        if current_node.begin == index and current_node.finish == index:
            current_node.highest_char = char
            current_node.start_char = char
            current_node.end_char = char
            return current_node
        midpoint = (current_node.begin + current_node.finish) // 2
        if index <= midpoint:
            updated_left = self.modify_tree(current_node.left_child, index, char)
            return self.combine_nodes(updated_left, current_node.right_child)
        else:
            updated_right = self.modify_tree(current_node.right_child, index, char)
            return self.combine_nodes(current_node.left_child, updated_right)
    def combine_nodes(self, left_child, right_child):
        highest_char = max(left_child.highest_char, right_child.highest_char)
        longest_seq = max(left_child.longest_seq, right_child.longest_seq)
        if left_child.end_char == right_child.start_char:
            combined_length = left_child.end_length + right_child.start_length
            if combined_length > longest_seq:
                highest_char = left_child.end_char
                longest_seq = combined_length
        start_char = left_child.start_char
        start_length = left_child.start_length
        if left_child.begin + start_length == right_child.begin and left_child.start_char == right_child.start_char:
            start_length += right_child.start_length
        end_char = right_child.end_char
        end_length = right_child.end_length
        if right_child.finish - end_length == left_child.finish and right_child.end_char == left_child.end_char:
            end_length += left_child.end_length
        return Node(left_child.begin, right_child.finish, highest_char, start_char, end_char, longest_seq, start_length, end_length, left_child, right_child)
    def retrieve_max_length(self):
        return self.root_node.longest_seq
class Solution:
    def longestRepeating(self, s, query_characters, query_indices):
        result = []
        segment_tree = Tree(s)
        for i in range(len(query_indices)):
            segment_tree.root_node = segment_tree.modify_tree(segment_tree.root_node, query_indices[i], query_characters[i])
            result.append(segment_tree.retrieve_max_length())
        return result