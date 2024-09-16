from collections import Counter
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0
        for word in words:
            word_count = Counter(word)
            can_form = True
            for char in word_count:
                if word_count[char] > chars_count.get(char, 0):
                    can_form = False
                    break
            if can_form:
                total_length += len(word)
        return total_length
