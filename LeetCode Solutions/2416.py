from collections import defaultdict
from typing import List
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        current = self.root
        for char in word:
            current = current.children[char]
            current.count += 1
    def get_prefix_score(self, word: str) -> int:
        current = self.root
        score = 0
        for char in word:
            current = current.children[char]
            score += current.count
        return score
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = []
        for word in words:
            score = trie.get_prefix_score(word)
            result.append(score)
        return result