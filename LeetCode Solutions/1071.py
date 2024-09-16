import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def can_form(s, base):
            return base * (len(s) // len(base)) == s
        len1, len2 = len(str1), len(str2)
        gcd_length = math.gcd(len1, len2)
        candidate = str1[:gcd_length]
        if can_form(str1, candidate) and can_form(str2, candidate):
            return candidate
        else:
            return ""
