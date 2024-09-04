from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: set[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i+1:]
                    if next_word == endWord:
                        return level + 1
                    if next_word in wordList and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        return 0
