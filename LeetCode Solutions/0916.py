from collections import Counter
from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def get_max_freq(words):
            max_freq = Counter()
            for word in words:
                freq = Counter(word)
                for char, count in freq.items():
                    if max_freq[char] < count:
                        max_freq[char] = count
            return max_freq
        required_freq = get_max_freq(words2)
        def is_universal(word):
            word_freq = Counter(word)
            for char, count in required_freq.items():
                if word_freq[char] < count:
                    return False
            return True
        result = [word for word in words1 if is_universal(word)]
        return result
