class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            return all(c.lower() in sub and c.upper() in sub for c in set(sub))
        max_nice = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(max_nice):
                    max_nice = substring
        return max_nice
