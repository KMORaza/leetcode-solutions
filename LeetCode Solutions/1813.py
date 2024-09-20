class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        while words1 and words1[0] == words2[0]:
            words1.pop(0)
            words2.pop(0)
        while words1 and words1[-1] == words2[-1]:
            words1.pop()
            words2.pop()
        return len(words1) == 0
