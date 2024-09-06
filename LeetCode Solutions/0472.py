from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def word_break(word: str, word_set: set, mem: dict) -> bool:
            if word in mem:
                return mem[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or word_break(suffix, word_set, mem)):
                    mem[word] = True
                    return True
            mem[word] = False
            return False
        word_set = set(words)
        mem = {}
        ans = []
        for word in words:
            if word_break(word, word_set, mem):
                ans.append(word)
        return ans
