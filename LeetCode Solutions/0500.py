from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            lower_word = word.lower()
            if lower_word[0] in row1:
                row = row1
            elif lower_word[0] in row2:
                row = row2
            elif lower_word[0] in row3:
                row = row3
            else:
                continue
            if all(char in row for char in lower_word):
                result.append(word)
        return result
