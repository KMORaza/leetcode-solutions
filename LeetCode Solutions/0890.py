from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word: str, pattern: str) -> bool:
            word_to_pattern = {}
            pattern_to_word = {}
            for w_char, p_char in zip(word, pattern):
                if word_to_pattern.get(w_char) is None:
                    word_to_pattern[w_char] = p_char
                if pattern_to_word.get(p_char) is None:
                    pattern_to_word[p_char] = w_char
                if word_to_pattern[w_char] != p_char or pattern_to_word[p_char] != w_char:
                    return False
            return True
        return [word for word in words if matches(word, pattern)]
