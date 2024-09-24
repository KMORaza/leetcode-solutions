from collections import Counter
from typing import List
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_count = Counter()
        for word in words:
            total_count.update(word)
        n = len(words)
        for count in total_count.values():
            if count % n != 0:
                return False
        return True
