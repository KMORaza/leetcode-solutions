from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        previous_sorted = ""
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != previous_sorted:
                result.append(word)
                previous_sorted = sorted_word
        return result