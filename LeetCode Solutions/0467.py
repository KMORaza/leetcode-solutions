class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len = [0] * 26
        cur_len = 0
        for i in range(len(s)):
            if i == 0 or (ord(s[i]) - ord(s[i - 1]) == 1) or (s[i - 1] == 'z' and s[i] == 'a'):
                cur_len += 1
            else:
                cur_len = 1
            max_len[ord(s[i]) - ord('a')] = max(max_len[ord(s[i]) - ord('a')], cur_len)
        return sum(max_len)