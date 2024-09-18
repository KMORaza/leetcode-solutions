class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        for right in range(len(s)):
            freq[s[right]] += 1
            while all(freq[c] > 0 for c in 'abc'):
                freq[s[left]] -= 1
                left += 1
            count += left
        return count
