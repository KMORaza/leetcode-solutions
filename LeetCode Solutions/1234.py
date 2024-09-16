from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_freq = n // 4
        count = Counter(s)
        if all(count[char] == target_freq for char in 'QWER'):
            return 0
        min_len = n
        start = 0
        for end in range(n):
            count[s[end]] -= 1
            while all(count[char] <= target_freq for char in 'QWER'):
                min_len = min(min_len, end - start + 1)
                count[s[start]] += 1
                start += 1
        return min_len
