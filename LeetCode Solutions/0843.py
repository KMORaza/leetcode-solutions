class Solution:
    def findSecretWord(self, wordlist, master):
        word_set = set(wordlist)
        while word_set:
            guess = self.most_overlap_word(word_set)
            matches = master.guess(guess)
            if matches == 6:
                return
            word_set = {word for word in word_set if self.matches(word, guess) == matches}
    def most_overlap_word(self, candidates):
        counts = [[0] * 26 for _ in range(6)]
        for s in candidates:
            for i, char in enumerate(s):
                counts[i][ord(char) - ord('a')] += 1
        max_score = 0
        overlap_word = ""
        for s in candidates:
            score = sum(counts[i][ord(char) - ord('a')] for i, char in enumerate(s))
            if score > max_score:
                max_score = score
                overlap_word = s
        return overlap_word
    def matches(self, a, b):
        return sum(1 for x, y in zip(a, b) if x == y)
