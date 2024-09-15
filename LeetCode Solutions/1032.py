class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie = {}
        self.end_of_word = '#'
        self.stream = []
        for word in words:
            current = self.trie
            for ch in reversed(word):
                if ch not in current:
                    current[ch] = {}
                current = current[ch]
            current[self.end_of_word] = self.end_of_word
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        current = self.trie
        for ch in reversed(self.stream):
            if ch in current:
                current = current[ch]
                if self.end_of_word in current:
                    return True
            else:
                break
        return False
