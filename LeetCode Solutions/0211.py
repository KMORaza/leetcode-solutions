class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.root)
    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.is_end_of_word
        first_char = word[0]
        remaining_word = word[1:]
        if first_char == '.':
            for child in node.children.values():
                if self._search_in_node(remaining_word, child):
                    return True
        else:
            if first_char in node.children:
                return self._search_in_node(remaining_word, node.children[first_char])
        return False