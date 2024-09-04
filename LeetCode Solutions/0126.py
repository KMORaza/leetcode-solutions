from collections import deque, defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList:
            return []
        wordList = set(wordList)
        graph = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        while queue:
            current_word = queue.popleft()
            current_distance = distance[current_word]
            for next_word in self.get_neighbors(current_word, wordList):
                if next_word not in distance:
                    distance[next_word] = current_distance + 1
                    queue.append(next_word)
                if distance[next_word] == current_distance + 1:
                    graph[current_word].append(next_word)
        paths = []
        self.backtrack(beginWord, endWord, graph, [beginWord], paths)
        return paths
    def get_neighbors(self, word: str, wordList: set[str]) -> list[str]:
        neighbors = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    neighbors.append(next_word)
        return neighbors
    def backtrack(self, current_word: str, endWord: str, graph: defaultdict[list[str]], path: list[str], paths: list[list[str]]):
        if current_word == endWord:
            paths.append(list(path))
            return
        if current_word not in graph:
            return
        for neighbor in graph[current_word]:
            path.append(neighbor)
            self.backtrack(neighbor, endWord, graph, path, paths)
            path.pop()