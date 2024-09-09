class WordFilter:
    def __init__(self, words):
        self.word_map = {}
        self.words = words
        for index, word in enumerate(words):
            length = len(word)
            for i in range(length):
                prefix = word[:i+1]
                for j in range(length):
                    suffix = word[j:]
                    self.word_map[(prefix, suffix)] = index
    def f(self, pref, suff):
        return self.word_map.get((pref, suff), -1)
