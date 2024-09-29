from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        steps = 0
        for char in count_s:
            steps += max(0, count_s[char] - count_t[char])
        for char in count_t:
            steps += max(0, count_t[char] - count_s[char])
        return steps