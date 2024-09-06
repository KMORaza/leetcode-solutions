class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = s + s
        modified_doubled_s = doubled_s[1:-1]
        return s in modified_doubled_s
