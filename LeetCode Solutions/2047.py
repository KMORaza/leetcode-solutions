import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        valid_count = 0
        for word in words:
            if self.isValid(word):
                valid_count += 1
        return valid_count
    def isValid(self, word: str) -> bool:
        if word[-1] in ".,!":
            word = word[:-1]
        if re.search(r'[^a-zA-Z\-]', word):
            return False
        if word.count('-') > 1:
            return False
        if '-' in word:
            parts = word.split('-')
            if len(parts) != 2 or not all(part.isalpha() for part in parts):
                return False
        return True
