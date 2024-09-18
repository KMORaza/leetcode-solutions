class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        sorted_words = sorted(words, key=len)
        result = ' '.join(sorted_words)
        result = result[0].upper() + result[1:].lower()
        return result
