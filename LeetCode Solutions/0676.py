class MagicDictionary:
    def __init__(self):
        self.words_set = set()
    def buildDict(self, dictionary):
        self.words_set = set(dictionary)
    def search(self, searchWord):
        def differs_by_one(word1, word2):
            if len(word1) != len(word2):
                return False
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1
        for word in self.words_set:
            if differs_by_one(searchWord, word):
                return True
        return False
