class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for char in word1:
            count1[ord(char) - ord('a')] += 1
        for char in word2:
            count2[ord(char) - ord('a')] += 1
        for i in range(26):
            if abs(count1[i] - count2[i]) > 3:
                return False
        return True
