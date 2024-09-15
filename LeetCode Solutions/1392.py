class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while (j > 0 and s[i] != s[j]):
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        longest_prefix_suffix_length = pi[-1]
        if longest_prefix_suffix_length == n:
            longest_prefix_suffix_length = pi[longest_prefix_suffix_length - 1]
        return s[:longest_prefix_suffix_length]
