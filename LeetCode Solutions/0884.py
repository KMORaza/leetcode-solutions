from collections import Counter
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        count1 = Counter(words1)
        count2 = Counter(words2)
        result = []
        for word in count1:
            if count1[word] == 1 and word not in count2:
                result.append(word)
        for word in count2:
            if count2[word] == 1 and word not in count1:
                result.append(word)
        return result
