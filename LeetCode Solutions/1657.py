from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1, count2 = Counter(word1), Counter(word2)
        return (set(count1.keys()) == set(count2.keys()) and
                sorted(count1.values()) == sorted(count2.values()))
