from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        p_count = Counter(p)
        s_count = Counter()
        result = []
        p_len = len(p)
        s_len = len(s)
        for i in range(s_len):
            s_count[s[i]] += 1
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1
            if s_count == p_count:
                result.append(i - p_len + 1)
        return result
