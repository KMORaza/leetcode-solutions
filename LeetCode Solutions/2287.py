from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_s = Counter(s)
        count_target = Counter(target)
        max_count = float('inf')
        for char in count_target:
            max_count = min(max_count, count_s[char] // count_target[char])
        return max_count
