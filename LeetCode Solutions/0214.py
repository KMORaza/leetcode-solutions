class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def computeLPSArray(s: str) -> list:
            lps = [0] * len(s)
            length = 0
            i = 1
            while i < len(s):
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        lps = computeLPSArray(combined)
        longest_palindromic_prefix_length = lps[-1]
        to_add = rev_s[:len(s) - longest_palindromic_prefix_length]
        return to_add + s