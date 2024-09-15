from collections import Counter
from itertools import combinations
class Solution:
    def maxScoreWords(self, words, letters, score):
        letter_score = {chr(ord('a') + i): score[i] for i in range(26)}
        def calculate_word_score(word):
            return sum(letter_score[c] for c in word)
        def backtrack(index, current_count, current_score):
            if index == len(words):
                return current_score
            max_score = backtrack(index + 1, current_count, current_score)
            word = words[index]
            word_count = Counter(word)
            if all(current_count[c] >= word_count[c] for c in word_count):
                for c in word_count:
                    current_count[c] -= word_count[c]
                max_score = max(max_score,
                                backtrack(index + 1, current_count, current_score + calculate_word_score(word)))
                for c in word_count:
                    current_count[c] += word_count[c]
            return max_score
        letter_count = Counter(letters)
        return backtrack(0, letter_count, 0)
