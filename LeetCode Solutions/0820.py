class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def minimumLengthEncoding(self, words):
        root = TrieNode()
        for word in words:
            current = root
            for char in reversed(word):
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
        return self.calculateEncodingLengthDFS(root, 1)
    def calculateEncodingLengthDFS(self, node, depth):
        is_leaf = True
        total_length = 0
        for child in node.children.values():
            is_leaf = False
            total_length += self.calculateEncodingLengthDFS(child, depth + 1)
        if is_leaf:
            total_length += depth
        return total_length