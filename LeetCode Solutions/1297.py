from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_count = Counter()
        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1
        return max(substring_count.values(), default=0)
