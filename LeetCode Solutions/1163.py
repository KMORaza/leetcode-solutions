class Solution:
    def lastSubstring(self, s: str) -> str:
        max_suffix = s[-1]
        n = len(s)
        for i in range(n - 2, -1, -1):
            if s[i:] > max_suffix:
                max_suffix = s[i:]
        return max_suffix
