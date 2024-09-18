class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                for k in range(min(len(s) - i, len(t) - j)):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        count += 1
                    elif diff > 1:
                        break
        return count
