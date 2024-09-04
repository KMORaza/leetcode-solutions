class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        def backtrack(x, y, node, path):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False 
            if not (0 <= x < m and 0 <= y < n):
                return
            temp = board[x][y]
            if temp not in node.children:
                return
            board[x][y] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                backtrack(nx, ny, node.children[temp], path + temp)
            board[x][y] = temp
        m, n = len(board), len(board[0])
        result = set()
        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie.root, "")
        return list(result)