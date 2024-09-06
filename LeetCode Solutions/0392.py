class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len == 0:
            return True
        s_ptr, t_ptr = 0, 0
        while t_ptr < t_len:
            if s_ptr < s_len and s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == s_len
