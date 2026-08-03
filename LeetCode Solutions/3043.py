class TreeLeaf:
    def __init__(self):
        self.descendants = [None] * 10
class DigitalTrie:
    def __init__(self):
        self.root_leaf = TreeLeaf()
    def insert_number(self, num_str: str) -> None:
        current_leaf = self.root_leaf
        for digit in num_str:
            position = int(digit)
            if current_leaf.descendants[position] is None:
                current_leaf.descendants[position] = TreeLeaf()
            current_leaf = current_leaf.descendants[position]
    def count_matching_prefix(self, num_str: str) -> int:
        match_length = 0
        current_leaf = self.root_leaf
        for digit in num_str:
            position = int(digit)
            if current_leaf.descendants[position] is None:
                break
            current_leaf = current_leaf.descendants[position]
            match_length += 1
        return match_length
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        max_prefix_length = 0
        trie_structure = DigitalTrie()
        for number in arr1:
            trie_structure.insert_number(str(number))
        for number in arr2:
            max_prefix_length = max(max_prefix_length, trie_structure.count_matching_prefix(str(number)))
        return max_prefix_length
