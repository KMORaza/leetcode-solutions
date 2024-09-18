from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        words_set = set(words)
        for word in words:
            for other in words_set:
                if word != other and word in other:
                    substrings.add(word)
                    break
        return list(substrings)

