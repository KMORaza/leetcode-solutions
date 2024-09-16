from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import sys
        min_freq = [sys.maxsize] * 26
        for word in words:
            current_freq = [0] * 26
            for char in word:
                current_freq[ord(char) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], current_freq[i])
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * min_freq[i])
        return result
