class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken_set = set(brokenLetters)
        valid_word_count = 0
        for word in words:
            if not any(letter in broken_set for letter in word):
                valid_word_count += 1
        return valid_word_count