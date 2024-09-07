class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.prefix_sum = 0
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_map = {}
    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key in self.key_map:
            old_value = self.key_map[key]
        else:
            old_value = 0
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_sum += (val - old_value)
        node.value = val
        self.key_map[key] = val
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_sum